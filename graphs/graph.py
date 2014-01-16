from collections import deque


def build_graph(inputGraph):
    
    outputGraph = {}

    # Expected format of graph is "<vertex>: <vertex1> <vertex2> ... <vertexN>"
    # Let's start by reading the graph into data structure
    for line in inputGraph:
        startVertex, connectedVerticies = line.split(':')
        for v in connectedVerticies.strip().split(' '):
            outputGraph.setdefault(int(startVertex), []).append(int(v))

    return outputGraph
    

def BFS(inputGraph, startingVertex):

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
    print "Starting with " + str(startingVertex)

    for endVertex in inputGraph[startingVertex]:
        if endVertex not in searchPath:
            print "Exploring" + str(endVertex)
            run_DFS(inputGraph, endVertex)

    return searchPath

def DFS(inputGraph, startingVertex):

    graph = {}

    graph = build_graph(inputGraph)

    return run_DFS(graph, startingVertex)


                         


