from typing import Dict, Any
from datetime import datetime
import uuid


def create_research_state(topic: str) -> Dict[str, Any]:

    return {
        "research_id": str(uuid.uuid4()),

        "topic": topic,

        "plan": [],

        "search_queries": [],

        "sources": [],

        "research_notes": [],

        "summary": "",

        "fact_checks": [],

        "critic_feedback": [],

        "final_report": "",

        "status": "created",

        "human_approved": False,

        "human_comments": "",

        "execution_trace": [],

        "retry_count": {},

        "created_at": datetime.now().isoformat()
    }


def add_trace(
    state: Dict[str, Any],
    step: str,
    status: str,
    details: Any
):

    trace = {
        "timestamp": datetime.now().isoformat(),
        "step": step,
        "status": status,
        "details": details
    }

    state["execution_trace"].append(trace)