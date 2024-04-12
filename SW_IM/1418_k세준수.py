#-*- coding: utf-8 -*-
"""
10
3
(7)

10
4
(7)
"""
n = int(input())       # 주어지는 자연수 (1 <= n <= 1e5)
k = int(input())       # k-세준수계산을 위한 k

dp = [False] * (n+1)
primes = []
for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        dp[num] = True
        primes.append(num)
print(primes)

cnt = 0
final_lst = []
for num in range(2, n+1):
    max_lst = []
    for i in range(2, num+1):        
        if dp[i] and i <= k and num % i == 0:
            #cnt += 1
            #print(f"{num} : {i}")
            max_lst.append(i)
    print(f"{num}, {max_lst}")
    if max_lst != []:
        final_lst.append(max(max_lst))          
            
            
print(len(final_lst))