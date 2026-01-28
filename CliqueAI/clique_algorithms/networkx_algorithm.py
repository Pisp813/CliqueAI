import networkx as nx
import time
from CliqueAI.protocol import MaximumCliqueOfLambdaGraph


def networkx_algorithm(number_of_nodes: int, adjacency_list: list[list[int]]) -> list[int]:
    num_nodes = number_of_nodes
    adjacency_list = adjacency_list
    dict_of_lists = {i: adjacency_list[i] for i in range(num_nodes)}
    graph = build_graph(number_of_nodes, adjacency_list)
    return max_clique_dfs(graph, time_limit=0.8)


def build_graph(num_nodes, adjacency_list):
    G = nx.Graph()
    for i in range(num_nodes):
        for j in adjacency_list[i]:
            G.add_edge(i, j)
    return G

def max_clique_dfs(G: nx.Graph, time_limit=None):
    max_clique = []
    start_time = time.time()

    def expand(clique, candidates):
        nonlocal max_clique

        # Optional timeout (very important)
        if time_limit and time.time() - start_time > time_limit:
            return

        # Pruning
        if len(clique) + len(candidates) <= len(max_clique):
            return

        if not candidates:
            if len(clique) > len(max_clique):
                max_clique = list(clique)
            return

        for v in list(candidates):
            expand(
                clique + [v],
                candidates.intersection(G.neighbors(v))
            )
            candidates.remove(v)

    expand([], set(G.nodes))
    return max_clique
