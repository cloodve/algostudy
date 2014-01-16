import sys
import os.path
import random

try:
    from graph import BFS
    from graph import DFS
except ImportError:
    print "Unable to load BFS, please set PYTHONPATH"
    exit()

if __name__ == "__main__":
    
    if len(sys.argv) < 1:
        print "usage: {0} <testfile>".format(sys.argv[0])
        exit()

    if not os.path.isfile(sys.argv[1]):
        print "{0} is not a file".format(sys.argv[1])
        exit()

    # Read in graph and chose a random vertex 
    availableVerticies = []
    fileLines = None
    with open(sys.argv[1]) as f:
        fileLines = f.readlines()
        for line in fileLines:
            vertex = int(line.split(':')[0])
            availableVerticies.append(vertex)

    if fileLines:
        choice = random.choice(availableVerticies)
        verticies = BFS(fileLines, choice)

        dfsVerts = DFS(fileLines, choice)
