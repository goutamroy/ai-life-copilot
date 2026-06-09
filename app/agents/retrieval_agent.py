from app.services.retrieval_service import RetrievalService


def retrieval_agent(state, db, user_id):

    result = RetrievalService.retrieve_context(
        db=db,
        question=state["question"],
        user_id=user_id
    )

    state["context"] = result["context"]
    state["chunk_ids"] = result["chunk_ids"]

    return state