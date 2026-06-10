from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.state import RAGState
from app.agents.retrieval_agent import retrieval_agent
from app.agents.answer_agent import answer_agent
from app.agents.memory_agent import memory_agent
from app.agents.validation_agent import (
    validation_agent
)


def build_graph(db, user_id, conversation_id):

    workflow = StateGraph(RAGState)

    workflow.add_node(
        "memory",
        lambda state: memory_agent(
            state,
            db,
            conversation_id
        )
    )

    workflow.add_node(
        "retrieval",
        lambda state: retrieval_agent(
            state,
            db,
            user_id
        )
    )

    workflow.add_node(
        "answer",
        answer_agent
    )

    workflow.add_node(
        "validation",
        validation_agent
    )

    workflow.set_entry_point(
        "memory"
    )

    workflow.add_edge(
        "memory",
        "retrieval"
    )

    workflow.add_edge(
        "retrieval",
        "answer"
    )

    workflow.add_edge(
        "answer",
        "validation"
    )

    workflow.add_edge(
        "validation",
        END
    )

    return workflow.compile()