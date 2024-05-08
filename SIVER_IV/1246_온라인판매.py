#-*- coding: utf-8 -*-
"""
5 4
2
8
10
7

(7 21)
"""
n, m = map(int, input().split())
bids = []
for _ in range(m):
    bids.append(int(input()))
bids.sort()
print(f"bids : {bids}")

while bids:
    max_price, min_price = max(bids), min(bids)
    lst = []
    for pr in range(max_price, min_price-1):
        