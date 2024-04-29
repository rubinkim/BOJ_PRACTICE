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
    name, price = input().split()
    price = int(price)
    name_lst.append(name)
    price_lst.append(price)

#print(name_lst)
#print(price_lst)

price_dict = {}
for p in set(price_lst):
    price_dict[p] = price_lst.count(p)
#print(price_dict)

for k, v in price_dict.items():
    for i in range(len(price_lst)):
        if int(k) == price_lst[i]:
            final_lst.append((v, price_lst[i], name_lst[i]))
#print(final_lst)

final_lst = sorted(final_lst, key=lambda x : [x[0], x[1]])
#print(final_lst)
print(final_lst[0][2], final_lst[0][1])