#-*- coding: utf-8 -*-
"""
5
(6)

14
(12)
"""
n = int(input())    # 조약돌들의 갯수
max_side_plus_one = 0
for i in range(int((n-1)**0.5)+1):
    if i ** 2 <= n:
        max_side_plus_one = max(max_side_plus_one, i)
print(max_side_plus_one)

one_side_length = max_side_plus_one - 1

ans = 0
if max_side_plus_one ** 2 < n <= max_side_plus_one ** 2 + max_side_plus_one:
    ans = 2 * (one_side_length + one_side_length + 1)
elif max_side_plus_one ** 2 + max_side_plus_one < n <= (max_side_plus_one + 1) ** 2:
    ans = 4 * (one_side_length + 1)

print(ans)