import pandas as pd

def print_record_summary():
    edges = pd.read_csv("cache/tnagar_edges.csv")
    hazards = pd.read_csv("cache/hazard_tnagar_real.csv")
    edges_risk = pd.read_csv("cache/tnagar_edges_with_risk.csv")

    print("=== Stage 1: Data collection ===")
    print(f"Edges (tnagar_edges.csv): {len(edges)} records")
    print(f"Hazard rows (hazard_tnagar_real.csv): {len(hazards)} records")

    print("\n=== Stage 3–4: Fuzzy + risk ===")
    print(f"Edges with risk (tnagar_edges_with_risk.csv): {len(edges_risk)} records")
    print("Columns now include:", list(edges_risk.columns))

if __name__ == "__main__":
    print_record_summary()
