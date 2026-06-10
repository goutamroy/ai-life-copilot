from app.services.memory_service import (
    MemoryService
)


def memory_agent(
    state,
    db,
    conversation_id
):
    history = (
        MemoryService.get_recent_messages(
            db=db,
            conversation_id=conversation_id
        )
    )

    print("Memory Agent Executed")
    print(history)
    
    state["chat_history"] = history

    return state