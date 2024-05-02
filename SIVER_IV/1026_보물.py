#-*- coding: utf-8 -*-
"""
5
1 1 1 6 0
2 7 8 3 1

(18)

3
1 1 3
10 30 20

(80)

9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1

(528)
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

#print(f"a : {a}")
#print(f"b : {b}")

ans = 0
for i in range(len(a)):
    ans += a[i] * b[i]
    
print(ans)