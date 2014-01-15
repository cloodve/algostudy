import sys




class SelectSort(object):
    def __init__(self):
        self.data = []

    def insert(self, number):
        self.data.append(number)

    def pop_min(self):
        num = sys.maxint
        for item in self.data:
            if item < num:
                num = item  

        self.data.remove(num)
