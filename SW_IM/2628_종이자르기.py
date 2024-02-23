#-*- coding: utf-8 -*-

"""
10 8
3
0 3
1 4
0 2

30
"""

h, v = map(int, input().split())          # h : 가로축의 길이(j의 최대값),  v : 세로축의 길이(i의 최대값)
n = int(input())                          # n : 잘라야 하는 점선의 개수
h_axis, v_axis = [0, h], [0, v]           # v_axis : i들을 저장하는 리스트(세로축), h_axis : j들을 저장하는 리스트(가로축)
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0:
        h_axis.append(y)
    else:
        v_axis.append(y)

horizontals.sort()
verticals.sort()

print(horizontals)
print(verticals)

mx_area = 0
for i in range(1, len(horizontals)):
    for j in range(1, len(verticals)):
        mx_area = max(mx_area, (horizontals[i] - horizontals[i-1]) * (verticals[j] - verticals[j-1]))
print(mx_area)