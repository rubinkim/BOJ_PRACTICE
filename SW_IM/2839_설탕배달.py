#-*- coding: utf-8 -*-
"""

"""

N = int(input())
cnt5 = N // 5

while cnt5 >= 5:
    cnt3 = (N - cnt5 * 5) // 3
    if cnt5 * 5 + cnt3 * 3 == N:
        print(cnt5 + cnt3)