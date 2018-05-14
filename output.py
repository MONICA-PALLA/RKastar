'''Algo tester'''

from os import *
import time
import readfiles as rf
import time
import networkx
import subprocess


def dist(a, b):
   (x1, y1) = a
   (x2, y2) = b
   return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def antAlgo():
#    start_time = time.time()
    #system('g++ TSPConstructor.cpp -o TSPConstructor')
    #system('./TSPConstructor')
    system('g++ antal.cpp -o antal')
    #system('g++ antalElitist.cpp -o antalElitist')
    #system('g++ antalRank.cpp -o antalRank')
    #x = subprocess.check_output(['./antal'])
    #t1 = time()
    
    system('./antal')
    #system('./antalElitist')
    #system('./antalRank')

    rf.cityReadSACO()
    #rf.cityReadElitist()
    #rf.cityReadRank()

    # G=nx.path_graph(5)
    # G=nx.grid_graph(dim=[3,3])  # nodes are two-tuples (x,y)
    
    # print(nx.astar_path(G,(0,0),(2,2),dist))

if __name__ =='__main__':
    antAlgo()
 #   print ("time (%s)") % (time.time() - start_time)