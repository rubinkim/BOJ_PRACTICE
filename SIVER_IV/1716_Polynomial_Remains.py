"""
5 2
6 3 3 2 0 1
5 2
0 0 3 2 0 1
4 1
1 4 1 1 1
6 3
2 3 -3 4 1 0 1
1 0
5 1
0 0
7
3 5
1 2 3 4
-1 -1

(3 2
-3 -1
-2
-1 2 -3
0
0
1 2 3 4)
"""
import numpy as np

n, k = map(int, input().split())
print(f"n : {n},  k : {k}")

dividend = list(map(int, input().split()))
dividend = dividend[::-1]
dividend = np.array(dividend)
print(f"dividend : {dividend}")

divisor = [1, 0, 1]
divisor = np.array(divisor)
print(f"divisor : {divisor}")


    
        
           





