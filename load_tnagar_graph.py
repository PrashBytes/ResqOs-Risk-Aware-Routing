import os
import osmnx as ox

CACHE_DIR = "cache"
GRAPHML_PATH = os.path.join(CACHE_DIR, "tnagar_2km.graphml")


def load_tnagar_graph():
    print("Loading T. Nagar graph from GraphML...")
    G = ox.load_graphml(GRAPHML_PATH)
    print(f"Loaded graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    return G


if __name__ == "__main__":
    G = load_tnagar_graph()
