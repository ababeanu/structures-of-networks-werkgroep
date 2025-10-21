import networkx as nx
import random as rn
rn.seed(9)

G1 = nx.erdos_renyi_graph(10, 0.4, 2, False)
G2 = nx.erdos_renyi_graph(20, 0.1, 4, False)
G = nx.union(G1, G2, rename=("1", "2"))
G = nx.convert_node_labels_to_integers(G)

ids = rn.sample(list(range(1000)),len(list(G.nodes)))

mapping = {}

i=0
for x in (list(G.nodes)):
    mapping.update({x: ids[i]})
    i=i+1

G = nx.relabel_nodes(G, mapping)

adjacency = {}

for i in ids:
    adjacency.update({i: list(G.neighbors(i))})

def my_friends(node_id):
    node_adjacency = adjacency.get(node_id)
    if node_adjacency != None:
        print("my id is " + str(node_id) + " and the ids of my friends are: " + str(node_adjacency)[1:-1])
    else:
        print("there is nobody with id " + str(node_id))
