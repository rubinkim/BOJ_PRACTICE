#-*- coding: utf-8 -*-
"""
4
0 1 2 3
(1)

1
0
(-1)

6
0 3 1 3 2 3
(3)

2
1 1
(0)
"""
n = int(input())
nums = list(map(int, input().split()))
#print(f"nums : {nums}")

nums_dict = {}
for i in range(n+1):
    if i not in nums:
        nums_dict[i] = 0
    elif i in nums:
        nums_dict[i] = nums.count(i)
            
#print(f"nums_dict : {nums_dict}")

ans = 0
for k, v in nums_dict.items():
    if k == v:
        ans = k
    if k == 0 and v == 1:
        ans = -1
print(ans)