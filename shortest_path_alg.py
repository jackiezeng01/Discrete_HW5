from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges: dictionary of all possible next nodes where a given node is the key
        Ex: {X: ['A', 'B', 'C']}
        self.weights: dict with all the weights between two nodes with the tuple of the two nodes as the key
        Ex: {('X', 'A'): 7}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        '''
        Add a bidirectional edge
        '''
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


def dijsktra_alg(graph, initial, end):
    """
    Inputs: graph, inital vertex, end vertex
    Returns: shortest path
    """
    # shortest paths is a dict of nodes whose value is a tuple of (previous node, weight)
    # This dictionary updates if a shorter path than the one in the dictionary is available 
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    # Set of visited nodes
    visited = set()
    
    # Keep looping as long until we reach the destination node
    while current_node != end:
        # Add this node to the set of visited nodes
        visited.add(current_node)
        # Adjacent nodes to current node
        destinations = graph.edges[current_node]
        # Get the distance from the inital node to the current node
        weight_to_current_node = shortest_paths[current_node][1]

        # Loop through each of the adjacent nodes
        for next_node in destinations:
            # Find the weight to this adjacent node
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            # Add the node to the dictionary of shortest path if its not there already
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            # If node is already in the shortest path dict, update it is there is a shorter path available
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        # Create a list of next destinations: the next node cannot be already visited
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

if __name__ == "__main__":

    graph = Graph()

    edges = [
        # ('X', 'A', 7),
        # ('X', 'B', 2),
        # ('X', 'C', 3),
        # ('X', 'E', 4),
        # ('A', 'B', 3),
        # ('A', 'D', 4),
        # ('B', 'D', 4),
        # ('B', 'H', 5),
        # ('C', 'L', 2),
        # ('D', 'F', 1),
        # ('F', 'H', 3),
        # ('G', 'H', 2),
        # ('G', 'Y', 2),
        # ('I', 'J', 6),
        # ('I', 'K', 4),
        # ('I', 'L', 4),
        # ('J', 'L', 1),
        # ('K', 'Y', 5),
    ]

    for edge in edges:
        graph.add_edge(*edge)

    path = dijsktra_alg(graph, 'X', 'Y')
    print(path)

