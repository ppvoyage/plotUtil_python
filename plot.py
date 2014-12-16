import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    nodes = set([n1 for n1, n2, n3 in graph] + [n2 for n1, n2,n3 in graph])

    G = nx.Graph()

    for node in nodes:
        G.add_node(node)

    for edge in graph:
        G.add_edge(edge[0], edge[1], weight = edge[2])

    pos = nx.fruchterman_reingold_layout(G)
    nx.draw(G, pos, node_size = 2)
    edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    # show graph
    plt.show()

# draw example

# parse
transaction = {}
graph = []

f = open('./data/TxIn.log','r')
for i in range(1000):
    line = f.readline()
    if line == '':
        break
    data = [value for value in line.split(',')]
    txid = data[0]
    txIn = data[6][:-1]
    
    if txid not in transaction:
        transaction[txid] = [txIn];
    else:
        transaction[txid].append(txIn);
    
    #print txid, txIn
    
f = open('./data/TxOut.log','r')
for i in range(1000):
    line = f.readline()
    if line == '':
        break
    data = [value for value in line.split(',')]
    txid = data[0]
    amount = data[5][:4]
    txout = data[2]
    
    if txid in transaction:
        txIn = transaction[txid]
        for i in txIn:
            graph.append([i, txout, amount])
    #print txout

#for i in range(1000):
#    graph.append([i, i + 1, 1])
draw_graph(graph)
