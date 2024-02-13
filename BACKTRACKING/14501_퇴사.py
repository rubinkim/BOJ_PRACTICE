#-*- coding: utf-8 -*-
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
"""

import sys
input = sys.stdin.readline
N = int(input())
T = [0] * N
P = [0] * N
pay_lst = []

for i in range(N):
    t, p = tuple(map(int, input().split()))
    T[i] = t
    P[i] = p
    
    
print(f"N : {N}")
print(f"T : {T}")
print(f"P : {P}")

def dfs(n, pay):     # n : T배열의 인덱스
    global pay_lst
    if n >= N-1:
        #print(f"n : {n},  pay : {pay}")
        print()
        pay_lst.append(pay)
        return
    #if n + T[n] <= len(T):
    dfs(n+T[n], pay+P[n])  
    print(f"n : {n}, T[n] : {T[n]},  P[n] : {P[n]}")      
    dfs(n+T[n], pay)  
    

        
dfs(0, 0)
print(pay_lst) 
print(max(pay_lst))
    