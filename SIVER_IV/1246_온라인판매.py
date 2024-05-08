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
#print(f"bids : {bids}")

max_bid, min_bid = max(bids), min(bids)
lst = []
for pr in range(max_bid, min_bid-1, -1):
    revenue = 0
    cnt = 1
    for i in range(len(bids)):
        if bids[i] >= pr and cnt <= n:
            revenue += pr
            cnt += 1
    lst.append((pr, revenue))
    
new_lst = sorted(lst, key=lambda x : x[1], reverse=True)
    
print(new_lst[0][0], new_lst[0][1])