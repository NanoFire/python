import networkx as nx
import matplotlib.pyplot as plt

graph = {
    "A": [["B", 2], ["C", 5], ["I", 1]],
    "B": [["C", 1], ["D", 3]],
    "C": [["E", 2]],
    "D": [["F", 4]],
    "E": [["D", 1], ["F", 3]],
    "F": [["G", 2], ["H", 1]],
    "G": [["I", 3]],
    "H": [["I", 2]],
    "I": []
}

save = ["A"]
save_all = [["A", 0]]
start = "A"
end = "H"
same = 0
G = nx.DiGraph()

def draw_graph():
    pos = {
        "A": (-2, 2),
        "B": (1, 1),
        "C": (2, 2),
        "I": (0, -1),
        "D": (-1, -2),
        "F": (1, -2),
        "E": (-1, -3),
        "G": (1, -3),
        "H": (0, -4)
    }

    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge[0], weight=edge[1])

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Modify this part to only draw the solution path
    path_edges = [(save[i], save[i+1]) for i in range(len(save)-1)]
    nx.draw(G, pos=pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    nx.draw_networkx_edges(G, pos=pos, edgelist=path_edges, edge_color='r', width=2)
    plt.show()

def hello(key):
    global same
    minimum = None
    for i in graph[key]:
        if minimum is None or i[1] < minimum[1]:
            minimum = i
    
    if minimum is not None:
        same = same + minimum[1]
        minimum[1] = same + minimum[1]
        
    return minimum

def ucs(key):
    global same
    min_item = hello(key)
    if key == "A":
        same = 0
    
    if min_item is not None:
        save.append(min_item[0])
        save_all.append(min_item)
        graph[key].remove(min_item)
        G.add_edge(key, min_item[0], weight=min_item[1])
        if min_item[0] == end:
            print(f"Goal reached: {save} same is  : {same}")
            print(save_all)
            draw_graph()
        else:
            ucs(min_item[0])
    else:
        print(f"No minimum value found for key '{key}'.")
        if key == "A":
            print(graph)
        else:
            ucs(start)

ucs(start)
