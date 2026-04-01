import networkx as nx

def build_transaction_graph(transactions):
    """
    Build a graph: accounts as nodes, transactions as edges
    """
    G = nx.Graph()
    for txn in transactions:
        src = txn["account"]
        dst = txn.get("recipient", txn["account"])
        G.add_edge(src, dst, amount=txn["amount"])
    return G

def detect_suspicious_rings(graph):
    """
    Identify small densely connected clusters (potential mule rings)
    """
    clusters = [c for c in nx.connected_components(graph) if len(c) > 2]
    return clusters
