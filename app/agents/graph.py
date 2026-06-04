from langgraph.graph import StateGraph
from langgraph.graph import END

from app.agents.state import AgentState

from app.agents.nodes import (
    load_memory_node,
    generate_response_node
)


def build_graph():

    workflow = StateGraph(
        AgentState
    )

    workflow.add_node(
        "load_memory",
        load_memory_node
    )

    workflow.add_node(
        "generate_response",
        generate_response_node
    )

    workflow.set_entry_point(
        "load_memory"
    )

    workflow.add_edge(
        "load_memory",
        "generate_response"
    )

    workflow.add_edge(
        "generate_response",
        END
    )

    return workflow.compile()