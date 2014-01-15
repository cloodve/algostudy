from regular_heap import Heap
from select_sort_comparison import SelectSort



def run_select_sort_test(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        strNumbers = line.split(',') 
        intNumbers = []
        for number in strNumbers:
            intNumbers.append(int(number)) 
        

    s = SelectSort()
    for number in intNumbers:
        s.insert(number)

    while len(s.data):
        s.pop_min()



def run_heap_test(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        strNumbers = line.split(',') 
        intNumbers = []
        for number in strNumbers:
            intNumbers.append(int(number)) 

    h = Heap()
    for number in intNumbers:
        h.insert(number)

    
    while len(h.heap):
        h.pop_min() 

        
