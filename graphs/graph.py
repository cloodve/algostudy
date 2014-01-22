from collections import deque


def build_graph(inputGraph):
    """
    Just a helper function to get an adjacency list of ints from strings.

    """
    
    outputGraph = {}

    # Expected format of graph is "<vertex>: <vertex1> <vertex2> ... <vertexN>"
    # Let's start by reading the graph into data structure
    for line in inputGraph:
        startVertex, connectedVerticies = line.split(':')
        for v in connectedVerticies.strip().split(' '):
            outputGraph.setdefault(int(startVertex), []).append(int(v))

    return outputGraph
    

def BFS(inputGraph, startingVertex):
    """
    BFS is best implemented using a deque. Nodes to be explored next are added
    to the back of the deque. Nodes to directly explore next are pulled of the 
    front.

    """


    searchPath = []
    graph = {}

    graph = build_graph(inputGraph)
    
    q = deque()
    q.appendleft(startingVertex)
    searchPath.append(startingVertex)
    
    while q:
        v = q.pop()
        
        # Explore Vs verticies
        for endVertex in graph[v]:
            if endVertex not in searchPath:
                searchPath.append(endVertex)
                q.appendleft(endVertex)

 
    return searchPath
         
searchPath = []
def run_DFS(inputGraph, startingVertex):

    searchPath.append(startingVertex)

    for endVertex in inputGraph[startingVertex]:
        if endVertex not in searchPath:
            run_DFS(inputGraph, endVertex)

    return searchPath

def DFS(inputGraph, startingVertex):
    """
    DFS is best used with a stack. That way you can add to the top explored items
    and pop them off the top of the stack.

    """

    graph = {}

    graph = build_graph(inputGraph)

    return run_DFS(graph, startingVertex)


                         


