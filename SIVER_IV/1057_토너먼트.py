#-*- coding: utf-8 -*-
"""
16 1 2
(1)

16 8 9
(4)

1000 20 31
(4)

65536 1000 35000
(16)

60000 101 891
(10)
"""

n, kim, lim = map(int, input().split())
cnt = 1

while True:
    if (kim-1) // 2 == (lim-1) // 2:
        print(cnt)
        break
    if n % 2 == 1:
        n /= 2
        kim = (kim-1) // 2 + 1
        lim = (lim-1) // 2 + 1