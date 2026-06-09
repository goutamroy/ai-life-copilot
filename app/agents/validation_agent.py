def validation_agent(state):

    answer = state["answer"]

    if not answer:
        state["answer"] = (
            "I could not find that information "
            "in the uploaded documents."
        )

    return state