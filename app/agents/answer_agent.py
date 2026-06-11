from app.services.bedrock_llm_service import get_llm

from app.services.rag_prompt_service import (
    RAG_PROMPT
)


def answer_agent(state):

    print("Answer Agent Executed")
    print("Using AWS Bedrock Claude")

    llm = get_llm()

    prompt = RAG_PROMPT.format(
        chat_history=state["chat_history"],
        context=state["context"],
        question=state["question"]
    )

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state