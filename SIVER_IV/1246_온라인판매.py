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
bids.sort(reverse=True)
print(f"bids : {bids}")

max_bid, min_bid = max(bids), min(bids)
lst = []
for pr in range(max_bid, min_bid-1, -1):
    revenue = 0
    for i in range(len(bids)):
        if bids[i] >= pr:
            revenue += pr
    lst.append((revenue, pr))
    
new_lst = sorted(lst, key=lambda x : x[0], reverse=True)
    
print(new_lst)