import numpy as np
import random as random
import math as math
from dataclasses import dataclass

def rabbit_stairs(n) :
    ways = [0] * (n + 1)
    
    ways[1] = 1
    ways[2] = 2
    
    for stair in range(3, n + 1 ) :
        ways[stair] = ways[stair - 1] + ways[stair - 2]
        
    return ways[n]

def rabbit_stairs_2(n) :
    
    if n == 0 :
        return 1
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    
    ways = [0] * (n + 1)
    
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2
    
    for stair in range(3, n + 1) :
        ways[stair] = ways[stair - 1 ] + ways[stair - 2] + ways[stair - 3]
    
    return ways[n]

