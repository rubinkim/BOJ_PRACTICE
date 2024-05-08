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
bids.sort(inverse=True)
print(f"bids : {bids}")

while bids:
    max_price, min_price = max(bids), min(bids)
    lst = []
    pr = max_price
    revenue = 0
    for i in range(len(bids)):
        if bids[i] >= pr:
            revenue += pr
    lst.append((pr, revenue))
    pr -= 1
    revenue = 0
    

max_bid, min_bid = max(bids), min(bids)
lst = []
for pr in range(max_bid, min_bid-1):
    revenue = 0
    