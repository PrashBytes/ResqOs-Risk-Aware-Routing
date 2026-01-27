import pandas as pd
import networkx as nx


def build_graph_from_edges():
    edges = pd.read_csv("cache/tnagar_edges_with_risk.csv")

    G = nx.DiGraph()

    for _, row in edges.iterrows():
        u = row["u"]
        v = row["v"]
        cost = row["effective_cost"]
        length = row.get("length", 1.0)
        risk = row.get("risk_score", 0.0)

        G.add_edge(
            u, v,
            effective_cost=cost,
            length=length,
            risk_score=risk,
            edge_id=row.get("edge_id", None),
            name=row.get("name", "")
        )

    return G


def compute_safe_path(G, source, target):
    path_nodes = nx.shortest_path(
        G,
        source=source,
        target=target,
        weight="effective_cost"
    )
    total_cost = nx.shortest_path_length(
        G,
        source=source,
        target=target,
        weight="effective_cost"
    )
    return path_nodes, total_cost


if __name__ == "__main__":
    G = build_graph_from_edges()

    source = 247074856
    target = 248697312

    path, cost = compute_safe_path(G, source, target)
    print("Safe path (nodes):", path)
    print("Total effective cost:", cost)

    print("\nSegments travelled:")
    for u, v in zip(path, path[1:]):
        data = G[u][v]
        edge_id = data.get("edge_id", "")
        name = data.get("name", "")
        print(f"{u} -> {v} | edge_id: {edge_id} | street/junction: {name}")

