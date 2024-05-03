#-*- coding: utf-8 -*-
"""
4
1 7 14 10
2
(4)

5
4 8 13 24 30
10
(5)

5
10 20 30 40 50
30
(0)

8
3 7 12 18 25 100 33 1000
59
(1065)
"""

l = int(input())
s = list(map(int, input().split()))
s.sort()
n = int(input())

#print(f"l : {l}, s : {s}, n : {n}")

cnt = 0
for i in range(l-1):
    if s[i] < n < s[i+1]:
        for j in range(s[i]+1, n):
            cnt += s[i+1]-n-1

        break
            

    if s[i] == n:
        cnt = 0
        break
print(cnt)