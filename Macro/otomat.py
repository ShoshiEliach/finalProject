import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from(["A", "B", "C", "D"])

# Add edges to the graph
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])

# Define the initial state and final states
initial_state = "A"
final_states = {"D"}

# Define a function to simulate the automaton on the graph
def simulate_automaton(graph, initial_state, final_states):
    current_state = initial_state
    path = [current_state]

    while current_state not in final_states:
        neighbors = list(graph.neighbors(current_state))
        if not neighbors:
            break
        current_state = neighbors[0]
        path.append(current_state)

    return path

# Simulate the automaton on the graph
path_taken = simulate_automaton(G, initial_state, final_states)

# Print the path taken by the automaton
print("Path taken by the automaton:", path_taken)
