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

7 2
1 1
1 1
1 1
1 1
1 1
1 1
1 1
"""

N, K = map(int, input().split())
my_dict = {}

for sex in range(0, 2):
    for year in range(1, 7):
        my_dict[(sex, year)] = 0
        
print(my_dict)

for _ in range(N):
    sex, year = map(int, input().split())
    my_dict[(sex, year)] += 1
    
print(my_dict)


