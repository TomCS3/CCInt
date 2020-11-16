"""
Route Between Nodes: Given a directed graph, design an algorithm to find 
out whether there is a route between two nodes.
"""

graph = {

}

visited = []
queue = []
def BFS(visited, graph, node1, node2):
    if node1 == node2:
        return True
    
    visited.append(node1)
    queue.append(node1)

    while queue:
        cur_node = queue.pop(0)
        for neighbour in graph[cur_node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
    
    
