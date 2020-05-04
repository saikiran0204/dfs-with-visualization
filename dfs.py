from turtle import *
from random import randrange
from sys import setrecursionlimit
setrecursionlimit(10**6)

def matrix_to_graph(list1, length):
	g = dict()
	for i in range(length):
		g[i] = []
	for index in range(length):
		for i in range(length):
			if list1[index][i] == 1 and index != i:
				g[index].append(i)
	return g

position = {}
def draw(g):
	global position
	penup()
	visted = []

	#sets position for nodes and writes it
	for i in g.keys():
		a = True
		while a:
			a = False
			x = randrange(-400, 400)
			y = randrange(-200, 200)
			for j in position.keys():
				if 10000 > (position[j][0]-x)**2 + (position[j][1]-y)**2:
					a = True
					break 
		setposition(x, y)
		position[i] = [x, y]
		write(i)

	#draw edges
	for i in g.keys():
		visted.append(i)
		for j in g[i]:
			if j not in visted:
				penup()
				setposition(position[i][0], position[i][1])
				pendown()
				setposition(position[j][0], position[j][1])

visted = []
def dfs(graph, start, first):
	global visted, position
	penup()
	setposition(position[first])
	pendown()
	visted.append(start)
	setposition(position[start])
	print(start)
	for i in graph[start]:
		if i not in visted:
			dfs(graph, i, start)


	


number_of_nodes = int(input("Enter number of nodes:"))
print("Enter adjacency matrix")
graph = []
for i in range(number_of_nodes):
	temp = [int(x) for x in input().split()]
	graph.append(list(temp))
graph = matrix_to_graph(graph, number_of_nodes)
draw(graph)
pencolor("green")
pensize(5)
dfs(graph, 0, 0)
mainloop()
