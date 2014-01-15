
class Heap(object):
    def __init__(self, objects=None):
        if objects:
            pass # TODO: implement heap if all the objects passed in
        else:
            self.heap = [] 

    def insert(self, number):
        
        self.heap.append(number) 

        # Check its parents and move up
        insertIndex = len(self.heap)
        while ((insertIndex-1) > 0 and 
                self.heap[insertIndex-1] < self.heap[(insertIndex/2)-1]):
            # print "Comparing self.heap[insertIndex-1] < self.heap[(insertIndex/2)-1])"
            # print "Heap " + str(self.heap)
            # print "insertIndex " + str(insertIndex)
            # print "Val " + str(self.heap[insertIndex-1] < self.heap[(insertIndex/2)-1])
            # print "Val " + str(self.heap[insertIndex-1]), str(self.heap[(insertIndex/2)-1])

            # Swap the child and parent
            self.heap[(insertIndex/2)-1], self.heap[insertIndex-1] = self.heap[insertIndex-1], \
                self.heap[(insertIndex/2)-1]

            insertIndex = (insertIndex/2)
                
    def pop_min(self):
            
        smallest = None 

        # Pull off the min, but don't delete, don't want it to update entire array
        if self.heap:
            smallest = self.heap[0]

            # Swap last item and bubble down 
            heapLen = len(self.heap)
            self.heap[0], self.heap[heapLen-1] = self.heap[heapLen-1], self.heap[0]
            self.heap.pop()
            heapLen -= 1

            # Bubble down 
            bubbleIndex = 0
            # Let's use smallestChildIndex as 1-based to be used in child computations
            smallestChildIndex = 3 if heapLen > 2 and self.heap[1] > self.heap[2] else 2 
            # print "BEFORE: ", str(smallestChildIndex), str(bubbleIndex)
            # print "BEFORE2: ", str(self.heap)
            while (smallestChildIndex >= 0 and 
                    (smallestChildIndex - 1) < heapLen and
                    self.heap[bubbleIndex] > self.heap[smallestChildIndex-1]): 
                # print "Heap " + str(self.heap)
                # print "BubbleIndex " + str(bubbleIndex)
                # print "smallestChildIndex " + str(smallestChildIndex)
                # print "val " + str(self.heap[bubbleIndex]), str(self.heap[smallestChildIndex-1])
                self.heap[bubbleIndex], self.heap[smallestChildIndex-1] = self.heap[smallestChildIndex-1], \
                    self.heap[bubbleIndex]

                bubbleIndex = (smallestChildIndex-1)
                childOne = childTwo = (smallestChildIndex * 2) # Zero based, 2i + 1
                # childOne = (smallestChildIndex * 2) - 1 # Zero based, 2i
                childOne -= 1
                if childTwo < (heapLen-1):
                    smallestChildIndex = childOne + 1 if self.heap[childOne] < self.heap[childTwo] else childTwo + 1
                elif childOne < (heapLen-1):
                    smallestChildIndex = childOne + 1 

                # print "New Bubble " + str(bubbleIndex)
                # print "New Smallest " + str(smallestChildIndex)

        # Throw away last item since it's being returned to user
        return smallest

