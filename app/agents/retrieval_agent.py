from app.services.retrieval_service import RetrievalService


def retrieval_agent(state):

    print("Retrieval Agent Executed")

    result = RetrievalService.retrieve_context(
        db=state["db"],
        question=state["question"],
        user_id=state["user_id"]
    )

    state["context"] = result["context"]
    state["chunk_ids"] = result["chunk_ids"]

    return state