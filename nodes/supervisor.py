# supervisor.py placeholder
from typing import TypedDict

class State(TypedDict):
    query: str
    response: str

def route(state: State) -> str:
    q = state["query"].lower()
    # simple keyword rules for now
    if any(token in q for token in ["compare", "trend"]):
        return "comparison"
    if "review" in q or "customer" in q:
        return "deepdive"
    return "fallback"