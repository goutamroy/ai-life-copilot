from app.agents.state import AgentState

from app.services.llm_service import (
    LLMService
)

from app.services.provider_factory import (
    ProviderFactory
)


def load_memory_node(
    state: AgentState
):

    print(
        "Loading memory node executed"
    )

    return state


def generate_response_node(
    state: AgentState
):

    print(
        "Generate response node executed"
    )

    llm = LLMService(
        ProviderFactory.get_provider()
    )

    prompt = f"""
Conversation Context:

{state['context']}

Current Message:

{state['user_message']}
"""

    response = llm.chat(
        prompt
    )

    state["response"] = response

    return state