import networkx as nx
import matplotlib.pyplot as plt
import random

def Draw_Graph(deep_g):
	elarge = [(u,v) for (u,v,d) in deep_g.edges(data=True) if d['weight'] >0.5]
	esmall = [(u,v) for (u,v,d) in deep_g.edges(data=True) if d['weight'] <=0.5]
	pos = nx.spring_layout(deep_g)
	nx.draw_networkx_nodes(deep_g,pos,node_size=600)
	nx.draw_networkx_edges(deep_g, pos, edgelist = elarge, width=6)
	nx.draw_networkx_edges(deep_g, pos, edgelist = esmall, width=6,alpha=0.5,edge_color='b',style='dashed')
	nx.draw_networkx_labels(deep_g,pos,font_size=20,font_family='sans-serif')
	plt.axis('off')
	plt.show()

def dejkstra(G, start):
    shortest_path = {vertex:float('+inf') for vertex in G}
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + G[current][neighbour]
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path
                


graph_raw = dict()
innput = open('graph.txt', 'r')
nodes = int(innput.readline().rstrip())
num_vertex = int(innput.readline().rstrip())



#_____________Creating empty graph for several nodes

for i in range(nodes):
	graph_raw[str(i)] = {}	

#_____________Reading  graph___________________
for i in range(num_vertex):
	temp = innput.readline().rstrip().split()
	
	graph_raw[temp[0]][temp[1]] = {'weight':1}
innput.close()	
graph = nx.Graph(graph_raw)




#_________Body of program__
start_node = input()
end_node = input()
print(dejkstra(graph, start_node)[end_node])

Draw_Graph(graph)
