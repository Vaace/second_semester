import networkx as nx
import matplotlib.pyplot as plt


graph_raw = dict()

input = open('graph.txt', 'r')

nodes = int(input.readline().rstrip())
num_vertex = int(input.readline().rstrip())


#_____________Creating empty graph for several nodes

for i in range(nodes):
	graph_raw[str(i)] = {}	




#_____________Reading  graph___________________
for i in range(num_vertex):
	temp = input.readline().rstrip().split()
	
	graph_raw[temp[0]][temp[1]] = {'weight':1}
input.close()	



#_____________Draw graph_______________________
graph = nx.Graph(graph_raw)

elarge = [(u,v) for (u,v,d) in graph.edges(data=True) if d['weight'] >0.5]
esmall = [(u,v) for (u,v,d) in graph.edges(data=True) if d['weight'] <=0.5]

pos = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph,pos,node_size=600)

nx.draw_networkx_edges(graph, pos, edgelist = elarge, width=6)
nx.draw_networkx_edges(graph, pos, edgelist = esmall, width=6,alpha=0.5,edge_color='b',style='dashed')

nx.draw_networkx_labels(graph,pos,font_size=20,font_family='sans-serif')

plt.axis('off')

plt.show()
