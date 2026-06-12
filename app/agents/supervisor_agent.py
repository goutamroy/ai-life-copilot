from app.agents.state import AgentState


def supervisor_agent(state: AgentState):

    print("Supervisor Agent Executed")

    question = state["question"].lower()

    if "previous" in question:
        route = "memory"

    elif "discuss" in question:
        route = "memory"

    elif "verify" in question:
        route = "validation"

    elif "source" in question:
        route = "validation"

    else:
        route = "retrieval"

    print(f"Supervisor Agent Route: {route}")

    state["route"] = route

    return state