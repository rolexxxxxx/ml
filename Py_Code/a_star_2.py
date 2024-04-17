def find_neighbors(graph, node):
    lst = []
    for i in range(0,len(graph[node])):
        if graph[node][i] > 0:
            lst.append([i, graph[node][i]])
    return lst

def a_star(graph, heuristics, start, destination):

    g_n = 0.0
    queue = [[0.0, start, [start]]]
    while queue:
        queue.sort()        
        current_pair = queue.pop(0)
        current_node, path = current_pair[1], current_pair[2]
        g_n = 0.0
        for i in range(0,len(path)-1):
            g_n += float(graph[path[i]][path[i+1]])

        if current_node == destination:
            print(f"The cost is {g_n}")
            return path
        
        neighbors = find_neighbors(graph, current_node)
        for neighbor in neighbors:
            temp = float(g_n) + float(neighbor[1]) + float(heuristics[neighbor[0]])
            queue.append([temp, neighbor[0], path + [neighbor[0]]])
 
graph = [[0,2,3,0,0,0,0,0],
         [0,0,0,3,0,0,0,0],
         [0,0,0,1,3,0,0,0],
         [0,0,0,0,1,3,0,0],
         [0,0,0,0,0,0,2,0],
         [0,0,0,0,0,0,0,2],
         [0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0]]

heuristics = [6.0,4.0,4.0,4.0,3.5,1.0,1.0,0.0]

letters = {0:'S', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G'}

start = 5

destination =  6

path = a_star(graph, heuristics, start, destination)

if path:
    print(f"Path from {letters[start]} to {letters[destination]} by A*: ", end = '')
    for i in range(0,len(path)):
        if i != len(path)-1:
            print(f"{letters[path[i]]} -> ", end = '')
    print(letters[path[-1]])
else:
    print(f"No path found from {letters[start]} to {letters[destination]} by A*")

