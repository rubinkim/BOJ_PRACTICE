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
    if (S,Y) not in my_dict:
        my_dict[(S, Y)] = 1
    else:
        my_dict[(S, Y)] += 1
            
#print(my_dict)

cnt = 0
for val in my_dict.values():
    if val  % K == 0:
        cnt += val // K
    else:
        cnt += val // K + 1
        
print(cnt)