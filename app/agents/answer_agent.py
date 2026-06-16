from botocore.exceptions import ClientError

from app.services.bedrock_llm_service import get_llm
from app.services.rag_prompt_service import RAG_PROMPT


def answer_agent(state):

    print("Answer Agent Executed")
    print("State Keys:", list(state.keys()))

    llm = get_llm()

    prompt = RAG_PROMPT.format(
        chat_history=state.get("memory", ""),
        context=state.get("context", ""),
        question=state["question"]
    )

    try:

        response = llm.invoke(prompt)

        state["answer"] = response.content

    except ClientError as e:

        error_message = str(e)

        print("========== BEDROCK ERROR ==========")
        print(error_message)
        print("===================================")

        state["answer"] = (
            f"Bedrock service error: {error_message}"
        )

    except Exception as e:

        error_message = str(e)

        print("========== UNKNOWN LLM ERROR ==========")
        print(error_message)
        print("=======================================")

        state["answer"] = (
            f"LLM error: {error_message}"
        )

    return state