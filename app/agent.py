import json
import os

from app.state import (
    create_research_state,
    add_trace
)

from app.agents.planner import create_plan
from app.agents.researcher import perform_research
from app.agents.summarizer import summarize_research
from app.agents.fact_checker import fact_check
from app.agents.critic import critique_research
from app.agents.final_report import (
    generate_final_report
)


RESEARCH_STORE = {}


def save_trace(state):

    os.makedirs(
        "app/traces",
        exist_ok=True
    )

    file_path = (
        f"app/traces/"
        f"{state['research_id']}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            state["execution_trace"],
            file,
            indent=4
        )


def run_research(topic: str):

    state = create_research_state(topic)

    RESEARCH_STORE[
        state["research_id"]
    ] = state

    try:

        # -------------------------
        # PLANNER
        # -------------------------

        add_trace(
            state,
            "planner",
            "started",
            "Creating research plan"
        )

        plan = create_plan(topic)

        state["plan"] = (
            plan.get(
                "research_questions",
                []
            )
        )

        state["search_queries"] = (
            plan.get(
                "search_queries",
                []
            )
        )

        add_trace(
            state,
            "planner",
            "completed",
            plan
        )


        # -------------------------
        # RESEARCH
        # -------------------------

        add_trace(
            state,
            "research",
            "started",
            "Searching web"
        )

        state = perform_research(state)

        add_trace(
            state,
            "research",
            "completed",
            {
                "sources_found":
                len(state["sources"])
            }
        )


        # -------------------------
        # SUMMARIZATION
        # -------------------------

        add_trace(
            state,
            "summarization",
            "started",
            "Summarizing research"
        )

        state = summarize_research(state)

        add_trace(
            state,
            "summarization",
            "completed",
            "Summary generated"
        )


        # -------------------------
        # FACT CHECKING
        # -------------------------

        add_trace(
            state,
            "fact_checking",
            "started",
            "Validating claims"
        )

        state = fact_check(state)

        add_trace(
            state,
            "fact_checking",
            "completed",
            "Fact checks completed"
        )


        # -------------------------
        # CRITIC
        # -------------------------

        add_trace(
            state,
            "critic",
            "started",
            "Reviewing research quality"
        )

        state = critique_research(state)

        add_trace(
            state,
            "critic",
            "completed",
            "Critic review completed"
        )


        # -------------------------
        # WAIT FOR HUMAN
        # -------------------------

        state["status"] = (
            "waiting_for_human_approval"
        )

        add_trace(
            state,
            "human_approval",
            "waiting",
            "Awaiting human decision"
        )

        save_trace(state)

        return state

    except Exception as error:

        error_message = (
            f"{type(error).__name__}: {str(error)}"
        )

        print(
            f"\n[WORKFLOW FAILED] "
            f"{error_message}"
        )

        state["status"] = "failed"

        state["error"] = error_message

        add_trace(
            state,
            "workflow",
            "failed",
            error_message
        )

        save_trace(state)

        return state
def approve_research(
    research_id: str,
    approved: bool,
    comments: str = ""
):
    # Get the existing research state
    state = RESEARCH_STORE.get(research_id)

    if not state:
        raise ValueError("Research ID not found")

    # Save human decision
    state["human_approved"] = approved
    state["human_comments"] = comments

    # -----------------------------------
    # HUMAN REJECTS THE RESEARCH
    # -----------------------------------
    if not approved:

        state["status"] = "rejected"

        add_trace(
            state,
            "human_approval",
            "rejected",
            comments
        )

        save_trace(state)

        return state

    # -----------------------------------
    # HUMAN APPROVES THE RESEARCH
    # -----------------------------------

    add_trace(
        state,
        "human_approval",
        "approved",
        comments
    )

    # Change status
    state["status"] = "generating_final_report"

    # Generate final report ONLY after approval
    state = generate_final_report(state)

    # Mark research as completed
    state["status"] = "completed"

    add_trace(
        state,
        "final_report",
        "completed",
        "Final report generated successfully"
    )

    # Save execution trace
    save_trace(state)

    return state