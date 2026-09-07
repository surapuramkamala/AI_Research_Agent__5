from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class ResearchRequest(BaseModel):
    topic: str


class ApprovalRequest(BaseModel):
    approved: bool
    comments: Optional[str] = None


class ResearchResponse(BaseModel):
    research_id: str
    status: str
    message: str
    data: Dict[str, Any]