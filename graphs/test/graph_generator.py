import random
import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: python {0} <#Verticies> <Optional:#ofEdges>".format(sys.argv[0])
        exit()

    # Start with a connected graph (numVerticies = numEdges), 
    # if it is to be acyclic, we'll fix after everything connected
    numOfEdges = int(sys.argv[1]) - 1
    verticies = [x for x in range(int(sys.argv[1]))]
   
    numOfIncidences = {}
    adjacencyList = {}
    while numOfEdges >= 1 and verticies >= 2:
        
        # Randomly select 2 veritices
        randomVerticies = random.sample(verticies, 2) 

        if randomVerticies[0] not in adjacencyList:
            adjacencyList[randomVerticies[0]] = []
            numOfIncidences[randomVerticies[0]] = 0

        if randomVerticies[1] not in adjacencyList:
            adjacencyList[randomVerticies[1]] = []
            numOfIncidences[randomVerticies[1]] = 0

        # Dont allow cycles
        if (randomVerticies[0] in adjacencyList[randomVerticies[1]] or
            randomVerticies[1] in adjacencyList[randomVerticies[0]]):
            # a single connection through graph
            continue 
        elif (numOfIncidences[randomVerticies[0]] == 1 and 
              numOfIncidences[randomVerticies[1]] == 1 and
              len(verticies) == 1):
            continue

 
        
        adjacencyList[randomVerticies[0]].append(randomVerticies[1])
        numOfIncidences[randomVerticies[0]] += 1
        
        if numOfIncidences[randomVerticies[0]] == 2:
            verticies.remove(randomVerticies[0])

        
        adjacencyList[randomVerticies[1]].append(randomVerticies[0])
        numOfIncidences[randomVerticies[1]] += 1
        
        if numOfIncidences[randomVerticies[1]] == 2:
            verticies.remove(randomVerticies[1])

        numOfEdges -= 1

    numOfNewEdges = 0
    if len(sys.argv) > 2:
        numOfNewEdges = int(sys.argv[2]) - (int(sys.argv[1]) - 1)

    # Start adding cycles
    while numOfNewEdges > 0:
        verticies = random.sample(adjacencyList.keys(), 2)
        adjacencyList[verticies[0]].append(verticies[1])
        adjacencyList[verticies[1]].append(verticies[0])
        numOfNewEdges -= 1
        

    for vertex, adjacent in adjacencyList.iteritems():
        print "{0}: {1}".format(str(vertex), " ".join(map(str, adjacent)))

   
    








