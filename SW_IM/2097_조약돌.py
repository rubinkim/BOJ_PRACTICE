#-*- coding: utf-8 -*-
"""
5
(6)

14
(12)
"""
n = int(input())    # ���൹���� ����
max_side_plus_one = 0
for i in range(int((n-1)**0.5)+1):
    if i ** 2 <= n:
        max_side_plus_one = max(max_side_plus_one, i)
print(max_side_plus_one)