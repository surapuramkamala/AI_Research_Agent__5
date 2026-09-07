{
  "topic": "Impact of AI agents on software engineering"
}

Architecture:
                    ┌──────────────┐
                    │     User     │
                    │Research Topic│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Planner    │
                    │ Break topic  │
                    │ into tasks   │
                    └──────┬───────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    Web Search     │
                 │ Multiple sources  │
                 │ Retry on failure  │
                 └────────┬──────────┘
                          │
                          ▼
                 ┌───────────────────┐
                 │     Research      │
                 │ Extract evidence  │
                 │ Store sources     │
                 └────────┬──────────┘
                          │
                          ▼
                 ┌───────────────────┐
                 │   Summarization   │
                 │ Structured notes  │
                 └────────┬──────────┘
                          │
                          ▼
                 ┌───────────────────┐
                 │   Fact Checking   │
                 │ Cross-reference   │
                 │ sources           │
                 └────────┬──────────┘
                          │
                          ▼
                 ┌───────────────────┐
                 │      Critic       │
                 │ Detect gaps /     │
                 │ unsupported claims│
                 └────────┬──────────┘
                          │
                 ┌────────┴─────────┐
                 │                  │
                 ▼                  ▼
          Needs More Research    Approved
                 │                  │
                 └───────┐          ▼
                         │   ┌───────────────┐
                         └──►│ Human Approval│
                             └───────┬───────┘
                                     │
                              Approve│Reject
                                     │
                                     ▼
                             ┌───────────────┐
                             │ Final Report  │
                             └───────────────┘