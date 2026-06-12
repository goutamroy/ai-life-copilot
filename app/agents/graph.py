from langgraph.graph import END
from langgraph.graph import StateGraph

from app.agents.state import AgentState

from app.agents.supervisor_agent import supervisor_agent
from app.agents.memory_agent import memory_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.answer_agent import answer_agent
from app.agents.validation_agent import validation_agent


graph = StateGraph(AgentState)

graph.add_node("supervisor", supervisor_agent)
graph.add_node("memory", memory_agent)
graph.add_node("retrieval", retrieval_agent)
graph.add_node("validation", validation_agent)
graph.add_node("answer", answer_agent)

graph.set_entry_point("supervisor")


def route_decision(state: AgentState):

    route = state["route"]

    if route == "memory":
        return "memory"

    if route == "validation":
        return "validation"

    return "retrieval"


graph.add_conditional_edges(
    "supervisor",
    route_decision,
    {
        "memory": "memory",
        "validation": "validation",
        "retrieval": "retrieval"
    }
)

graph.add_edge("memory", "answer")
graph.add_edge("retrieval", "answer")
graph.add_edge("validation", "answer")

graph.add_edge("answer", END)

agent_graph = graph.compile()

def build_graph():
    return agent_graph