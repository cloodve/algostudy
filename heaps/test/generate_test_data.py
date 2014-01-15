import sys
import random


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: <NumberOfRandomElements> <range>"

    print ",".join([str(int(round(random.random() * int(sys.argv[2])))) for x in range(int(sys.argv[1]))])

