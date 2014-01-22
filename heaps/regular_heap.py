"""
Implentation of a min heap.

Finding a parent:
parent(i) = i/2 if i is even, or i/2 floored if i is odd.

Finding Children:
2i and 2i+1

"""
class Heap(object):
    def __init__(self, objects=None):
        if objects:
            pass # TODO: implement heap if all the objects passed in
        else:
            self.heap = [] 

    def insert(self, number):
        """
        To insert, we append the new number to the end of the array, 
        and bubble it upwards to its final resting place. Bubbling
        is accomplished by swaping the child with its parent.

        """
        
        self.heap.append(number) 

        # Check its parents and move up
        insertIndex = len(self.heap)
        while ((insertIndex-1) > 0 and 
                self.heap[insertIndex-1] < self.heap[(insertIndex/2)-1]):

            # Swap the child and parent
            self.heap[(insertIndex/2)-1], self.heap[insertIndex-1] = self.heap[insertIndex-1], \
                self.heap[(insertIndex/2)-1]

            insertIndex = (insertIndex/2)
                
    def pop_min(self):
        """
        To pop min item, save the top node to a temp, swap it to the bottom and remove.
        Then, bubble the top item down to final resting place. 

        NOTE: Bubble down to the smaller of the two children.
        
        """
            
        smallest = None 

        # Pull off the min, but don't delete, don't want it to update entire array
        if self.heap:
            smallest = self.heap[0]

            # Swap the popped off item to the end of the tree and bubble down 
            # the item from the bottom to it's rightful position in tree.
            heapLen = len(self.heap)
            self.heap[0], self.heap[heapLen-1] = self.heap[heapLen-1], self.heap[0]
            self.heap.pop()
            heapLen -= 1

            # Bubble down 
            bubbleIndex = 0
            # Let's use smallestChildIndex as 1-based to be used in child computations
            smallestChildIndex = 3 if heapLen > 2 and self.heap[1] > self.heap[2] else 2 
            while ((smallestChildIndex - 1) < heapLen and
                   self.heap[bubbleIndex] > self.heap[smallestChildIndex-1]): 

                self.heap[bubbleIndex], self.heap[smallestChildIndex-1] = self.heap[smallestChildIndex-1], \
                    self.heap[bubbleIndex]

                bubbleIndex = (smallestChildIndex-1)
                childOne = childTwo = (smallestChildIndex * 2) # Zero based, 2i + 1
                childOne -= 1
                if childTwo < (heapLen-1): # Both must be valid indexes into heap, let's check both
                    smallestChildIndex = childOne + 1 if self.heap[childOne] < self.heap[childTwo] else childTwo + 1
                elif childOne < (heapLen-1): # Only one node left to check
                    smallestChildIndex = childOne + 1 

        # Throw away last item since it's being returned to user
        return smallest

