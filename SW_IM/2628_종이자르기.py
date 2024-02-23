#-*- coding: utf-8 -*-

"""
10 8
3
0 3
1 4
0 2

30
"""

h, v = map(int, input().split())       # h : 가로,  v : 세로
n = int(input())                       # n : 잘라야 하는 점선의 개수
horizontals, verticals = [0, v], [0, h]        # horizontals : 가로로 자르는 i들을 저장하는 리스트, verticals : 세로로 자르는 j들을 저장하는 리스트
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0:
        horizontals.append(y)
    else:
        verticals.append(y)

horizontals.sort()
verticals.sort()

print(horizontals)
print(verticals)

mx_area = 0
for i in range(1, len(horizontals)):
    for j in range(1, len(verticals)):
        mx_area = max(mx_area, (horizontals[i] - horizontals[i-1]) * (verticals[j] - verticals[j-1]))
print(mx_area)