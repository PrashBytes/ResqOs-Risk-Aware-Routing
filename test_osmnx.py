import osmnx as ox

# --------------------------------
# 1. Build 2 km x 2 km road graph
# --------------------------------
center_point = (13.04, 80.23)   # T. Nagar region (lat, lon)

G = ox.graph_from_point(
    center_point,
    dist=1000,              # meters
    dist_type="bbox",
    network_type="drive"
)

print("Graph created.")
print("Number of nodes:", len(G.nodes))
print("Number of edges:", len(G.edges))

# --------------------------------
# 2. Save map image
# --------------------------------
fig, ax = ox.plot_graph(
    G,
    show=False,
    save=True,
    filepath="tnagar_2km_roads.png"
)
print("Saved map image: tnagar_2km_roads.png")

# --------------------------------
# 3. Save full graph as GraphML
# --------------------------------
ox.io.save_graphml(G, filepath="tnagar_2km.graphml")
print("Saved GraphML file: tnagar_2km.graphml")

# --------------------------------
# 4. Export edges with partner's attributes
#    using utils_graph.graph_to_gdfs so u,v become columns
# --------------------------------
from osmnx import utils_graph

_, edges = utils_graph.graph_to_gdfs(
    G,
    nodes=False,
    edges=True,
    node_geometry=False,
    fill_edge_geometry=True
)

print("Edge columns:", list(edges.columns))

# Build the table
edges_out = edges[["osmid", "u", "v", "length", "highway"]].copy()
edges_out.rename(
    columns={
        "osmid": "edge_id",
        "u": "source_node",
        "v": "target_node",
        "highway": "road_type",
    },
    inplace=True,
)

edges_out.to_json("tnagar_edges.json", orient="records")
edges_out.to_csv("tnagar_edges.csv", index=False)

print("Saved tnagar_edges.json and tnagar_edges.csv")
