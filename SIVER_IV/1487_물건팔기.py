#-*- coding: utf-8 -*-
"""
3
13 0
22 0
35 0
(22)

3
13 5
22 15
35 30
(13)

3
13 15
22 30
35 40
(0)

5
10 1
10 5
20 11
20 15
5 0
(10)

8
13 12
17 1
14 5
30 10
19 3
17 2
55 40
16 19
(17)
"""
n = int(input())
price_lst, cost_lst, profit_lst = [], [], []

for _ in range(n):
    price, cost = map(int, input().split())
    price_lst.append(price)
    cost_lst.append(cost)
    
for price in range(max(price_lst)+1):
    profit = 0
    for i in range(len(price_lst)):
        if price <= price_lst[i]:
            if price - cost_lst[i] >= 0:
                profit += (price - cost_lst[i])
    profit_lst.append((profit, price))
 
profit_lst.sort(key=lambda x : x[0], reverse=True)

if profit_lst[0][0] >= 0:
    print(profit_lst[0][1])
else:
    print(0)