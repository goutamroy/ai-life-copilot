from langchain_core.prompts import PromptTemplate


RAG_PROMPT = PromptTemplate.from_template(
    """
Conversation History:
{chat_history}

Context:
{context}

Question:
{question}

Answer using the context and conversation history.
"""
)