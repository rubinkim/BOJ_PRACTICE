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

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""

import sys
input = sys.stdin.readline
N = int(input())
T = [0] * N
P = [0] * N
#pay_lst = []
#last_pay = 0

for i in range(N):
    t, p = tuple(map(int, input().split()))
    T[i] = t
    P[i] = p

print(T)
print(P)
    
def dfs(n, pay):     # n : T or P 배열의 인덱스
    global pay_lst, last_pay
    if n == N-1:
        pay_lst.append(pay)
        return
    if n > N-1:
        pay_lst.append(pay - last_pay)
        return

    last_pay = P[n]
    #print(f"n : {n},  last_pay : {last_pay}")
    dfs(n+T[n], pay+P[n])     
    dfs(n+T[n], pay)  

"""       
dfs(0, 0)
print(pay_lst) 
print(max(pay_lst))
"""

total_pay_lst = []
for i in range(N):
    pay_lst = []
    last_pay = 0
    dfs(i, 0)
    total_pay_lst.append(max(pay_lst))
    
print(total_pay_lst)



    