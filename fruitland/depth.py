import networkx as nx
import matplotlib.pyplot as plt

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

def dfs(G, start, called):
	
	called.add(start)
	for neighbour in G[start]:
		if neighbour not in called:
			deep_g.add_edge(start,neighbour, weight=0.9)
			dfs(G, neighbour,called)



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
graph = nx.Graph(graph_raw)


#_________Body of program__
deep_g = nx.Graph()
dfs(graph, '0', set())
Draw_Graph(deep_g)




