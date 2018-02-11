def dfs(graph, start):
	stack = [start]
	visited = []

	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			neighbors = sorted(graph[node], reverse=True)

			for item in neighbors:
				if item not in visited:
					stack.append(item)


	return visited






def bfs(graph, start):
	queue = []
	visited = []

	queue.append(start)

	while queue:
		node = queue.pop(0)

		if node not in visited:
			visited.append(node)
			neighbors = graph[node]

			for item in neighbors:
				queue.append(item)
	return visited

def bfs_shortest_path(graph, start, goal):
	queue = []
	visited = []

	queue.append([start])

	if start == goal:
		return "That was easy! Start = goal"

	while queue:
		path = queue.pop(0)
		last_node = path[-1]
		if last_node not in visited:
			neighbors = graph[last_node]
			for item in neighbors:
				new_path = list(path)
				new_path.append(item)
				queue.append(new_path)
				if item == goal:
					return new_path
			visited.append(last_node)

	return "No connecting path exists!"



graph = {1:[2,3],
		
		 2:[4,5],
		 3:[6],
		 4:[],
		 5:[6],
		 6:[]}

print bfs(graph, 1)

