


def legal_coord(coord, size):
	if coord >=0 and coord < size:
		return True
	else:
		return False


def generate_legal_moves(x, y, size):
	new_moves = []
	move_off_sets = [(-1,-2), (-1,2), (-2,-1), (-2, 1), (1,-2), (1,2), (2, -1), (2, 1)]


	for i in move_off_sets:
		new_x = x + i[0]
		new_y = y + i[1]

		if legal_coord(new_x, size) and legal_coord(new_y, size):
			new_moves.append((new_x, new_y))
	return new_moves




def create_graph(size):
	graph = {}
	for i in range(size):
		for j in range(size):
			moves = generate_legal_moves(i, j, size)
			node_ids = [k[0] + k[1]*size for k in moves]

			graph[i + size*j] = node_ids 



	return graph



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



print bfs_shortest_path(create_graph(5), 0, 23)


