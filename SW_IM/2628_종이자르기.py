#-*- coding: utf-8 -*-

"""
10 8
3
0 3
1 4
0 2

30
"""

h, v = map(int, input().split())          # h : h_axis(가로축)의 길이(j의 최대값),  v : v_axis(세로축)의 길이(i의 최대값)
n = int(input())                          # n : 잘라야 하는 점선의 개수
h_axis, v_axis = [0, h], [0, v]           # v_axis : i들을 저장하는 리스트(세로축), h_axis : j들을 저장하는 리스트(가로축)
for _ in range(n):
    axis, x = map(int, input().split())
    if axis == 0:
        v_axis.append(x)
    else:
        h_axis.append(x)

h_axis.sort()
v_axis.sort()

print(h_axis)
print(v_axis)

mx_area = 0
for i in range(1, len(v_axis)):
    for j in range(1, len(h_axis)):
        mx_area = max(mx_area, (v_axis[i] - v_axis[i-1]) * (h_axis[j] - h_axis[j-1]))
print(mx_area)