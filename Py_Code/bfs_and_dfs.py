def find_neighbors(graph, node):
    lst = []
    for i in range(0,len(graph[node])):
        if graph[node][i] == 1:
            lst.append(i)
    return lst


def bfs(graph, start, destination):
    visited = set()
    queue = [(start, [start])]

    while queue:

        current_node, path = queue.pop(0)

        if current_node == destination:
            return path

        if current_node not in visited:
            visited.add(current_node)
            neighbors = find_neighbors(graph, current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

def dfs(graph, start, destination):
    visited = set()
    stack = [(start, [start])]

    while stack:
        
        current_node, path = stack.pop(-1)
        
        if current_node == destination:
            return path

        if current_node not in visited:
            visited.add(current_node)
            neighbors = find_neighbors(graph, current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

graph = [[0,1,0,1,0,0,0],[1,0,1,1,0,1,0],[0,1,0,1,1,1,0],[1,1,1,0,1,0,0],[0,0,1,1,0,0,1],[0,1,1,0,0,0,0],[0,0,0,0,1,0,0]]

start_vertex = int(input('Enter start: '))
destination_vertex = int(input('Enter destination: '))

path = dfs(graph, start_vertex, destination_vertex)

if path:
    print(f"Path from {start_vertex} to {destination_vertex} by DFS: {path}")
else:
    print(f"No path found from {start_vertex} to {destination_vertex} by DFS")

path = bfs(graph, start_vertex, destination_vertex)

if path:
    print(f"Path from {start_vertex} to {destination_vertex} by BFS: {path}")
else:
    print(f"No path found from {start_vertex} to {destination_vertex} by BFS")
