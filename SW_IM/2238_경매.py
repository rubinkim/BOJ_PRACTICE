#-*- coding: utf-8 -*-
"""
10 4
Lew 10
CD 5
Fe 5
CD 7

(CD 7)
"""
u, n = map(int, input().split())
name_lst, price_lst, final_lst = [], [], []
for _ in range(n):
    name, price = map(input().split())
    name_lst.append(name)
    price_lst.append(price)

print(name_lst)
print(price_lst)