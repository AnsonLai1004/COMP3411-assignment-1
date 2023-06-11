def find_path(neighbour_fn,
			  start,
			  goal,
			  visited,
			  reachable = lambda pos: True,
			  depth = 100000):
	#The reachable function returns true if the given node is not blocked by a wall.


	"""
	#TODO: 
	Returns the path between two nodes as a list of nodes using depth first search.
	If no path can be found, an empty list is returned.
	
	"""
	if start == goal:
		return [start]
	if depth == 0:
		return []

	visited.append(start)
	for adj in neighbour_fn(start):
		if adj not in visited and reachable(adj):
			path = find_path(neighbour_fn, adj, goal, visited, reachable, depth - 1)
			if len(path) > 0:
				return [start] + path

	return []

def iddfs(neighbour_fn, start, goal, reachable_fn, max_depth):
	for i in range(max_depth):
		path = find_path(neighbour_fn, start, goal, [], reachable_fn, i)
		if len(path) > 0:
			return path
	return []

