# agent_graph.py placeholder
from langgraph.graph import StateGraph
from nodes.supervisor import route
from nodes.comparison_stub import comparison_agent
from nodes.deepdive_stub import deepdive_agent
from nodes.fallback_stub import fallback_agent
from nodes.supervisor import State, route

graph = StateGraph(State)
graph.add_node("supervisor", lambda s: {"next": route(s)})
graph.add_conditional_edges("supervisor", lambda s: route(s), {
    "comparison": "comparison",
    "deepdive": "deepdive",
    "fallback": "fallback"
})
graph.add_node("comparison", comparison_agent)
graph.add_node("deepdive", deepdive_agent)
graph.add_node("fallback", fallback_agent)
graph.set_entry_point("supervisor")

# Compile into a Runnable, overwriting `graph`
graph = graph.compile()