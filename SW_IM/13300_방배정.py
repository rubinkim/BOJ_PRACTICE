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


N, K = map(int, input().split())
my_dict = {}

for i in range(N):
    S, Y = map(int, input().split())
    if Y not in my_dict:
        if S == 0:
            my_dict[Y] = [1, 0]
        else:
            my_dict[Y] = [0, 1]
    else:
        if S == 0:
            my_dict[Y][0] += 1
        else:
            my_dict[Y][1] += 1
            
print(my_dict)

cnt = 0
for f, m in my_dict.values():
    if f  % 2 == 0:
        cnt += f // 2
    else:
        cnt += f // 2 + 1
    
    if m % 2 == 0:
        cnt += m // 2
    else:
        cnt += m // 2 + 1

print(cnt)

cnt = 0
if 1 not in my_dict:
    print(0)
else:
    if my_dict[1][1] % 2 == 0:
        cnt += my_dict[1][1] // 2
    else:
        cnt += my_dict[1][1] // 2 + 1

print(cnt)
"""


