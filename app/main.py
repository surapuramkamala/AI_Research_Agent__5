from fastapi import FastAPI, HTTPException

from app.models import (
    ResearchRequest,
    ApprovalRequest
)

from app.agent import (
    run_research,
    approve_research,
    RESEARCH_STORE
)


app = FastAPI(
    title="AI Research Agent",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message":
        "AI Research Agent is running"
    }


@app.post("/research")
def research(
    request: ResearchRequest
):

    state = run_research(
        request.topic
    )

    return {
        "research_id":
        state["research_id"],

        "status":
        state["status"],

        "plan":
        state["plan"],

        "sources_found":
        len(state["sources"]),

        "summary":
        state["summary"],

        "fact_checks":
        state["fact_checks"],

        "critic_feedback":
        state["critic_feedback"],

        "error": state.get("error")
    }


@app.post(
    "/research/{research_id}/approval"
)
def human_approval(
    research_id: str,
    request: ApprovalRequest
):

    try:

        state = approve_research(
            research_id,
            request.approved,
            request.comments or ""
        )

        return {
            "research_id":
            state["research_id"],

            "status":
            state["status"],

            "final_report":
            state["final_report"]
        }

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@app.get(
    "/research/{research_id}/trace"
)
def get_trace(
    research_id: str
):

    state = RESEARCH_STORE.get(
        research_id
    )

    if not state:

        raise HTTPException(
            status_code=404,
            detail="Research not found"
        )

    return {
        "research_id":
        research_id,

        "trace":
        state["execution_trace"]
    }