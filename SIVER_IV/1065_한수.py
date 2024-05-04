#-*- coding: utf-8 -*-
"""
110
(99)

1
(1)

210
(105)

1000
(144)

500
(119)
"""
n = int(input())
cnt = 0
for x in range(0, n+1):
    if 1 <= x <= 99:
        cnt += 1
    elif x >= 100:
        x = str(x)
        if (int(x[0]) - int(x[1])) == (int(x[1]) - (int(x[2]))):
            cnt += 1       
        
print(cnt)