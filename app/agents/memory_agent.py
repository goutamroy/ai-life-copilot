from app.services.memory_service import (
    MemoryService
)


def memory_agent(state):

    print("Memory Agent Executed")

    history = (
        MemoryService.get_recent_messages(
            db=state["db"],
            conversation_id=state["conversation_id"]
        )
    )

    state["memory"] = history

    return state