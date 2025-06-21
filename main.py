# main.py placeholder

from agent_graph import graph
from nodes.supervisor import State

def run_cli():
    """
    Simple CLI for interacting with the Supervisor agent.
    Type 'exit' or 'quit' to stop the loop.
    """
    print("Supervisor Agent CLI. Type 'exit' or 'quit' to exit.")
    while True:
        query = input("Query> ")
        if query.strip().lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        # Initialize state with the incoming query
        state: State = {"query": query, "response": ""}

        # Invoke the LangGraph workflow
        out_state = graph.invoke(state)

        # Print the resulting response
        response = out_state.get("response")
        print(f"Response: {response}\n")


if __name__ == "__main__":
    run_cli()
