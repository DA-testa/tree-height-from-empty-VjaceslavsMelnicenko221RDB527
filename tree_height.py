#221RDB527 Vjačeslavs Meļņičenkoo 15.grupa
# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    q = n*[-1]
    
    def h(node):
        if q[node] != -1:
            return q[node]
        if parents[node] == -1:
             q[node] = 1
        else:
             q[node] = h(parents[node])+1
        return  q[node]
   
    max_height = 0
    for root in range(n):
        max_height = max(max_height,h(root))
        
    return max_height


def main():
    
    t = input("I or F: ")
    if "I" in t:
       n = int(input())
       parents = list(map(int, input().split()))
    elif "F" in t:
        w = input()
        e ='./test/'
        r = e+w
        
        if "a" not in w:
            try:
                with open(r) as x:
                    n=int(x.readline())
                    parents=list(map(int,x.readline().split()))
            except Exception as y:
                print("Error",str(y))
                return
            
        else:
            print("Error")
            return    
    print(compute_height(n,parents))    
    

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
