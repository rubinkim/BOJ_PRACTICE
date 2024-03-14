#-*- coding: utf-8 -*-
"""
16 2
1 1
0 1
1 1
0 2
1 2
0 2
0 3
1 3
1 4
1 3
1 3
0 6
1 5
0 5
1 5
1 6

(12)



3 3
0 3
1 5
0 6

(3)
"""

N, K = map(int, input().split())
my_dict = {}

for i in range(N):
    S, Y = map(int, input().split())
    if Y not in my_dict:
        if S == 0:
            my_dict[Y][0] = 1
        else:
            my_dict[Y][1] = 1
    else:
        if S == 0:
            my_dict[Y][0] += 1
        else:
            my_dict[Y][1] += 1