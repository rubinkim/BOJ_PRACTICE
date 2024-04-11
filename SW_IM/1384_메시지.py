#-*- coding: utf-8 -*-
"""
5
Ann P N P P
Bob P P P P
Clive P P P P
Debby P N P P
Eunice P P P P
6
Zheng P P P P P
Yeng P P P P P
Xiao P P P P P
Will P P P P P
Veronica P P P P P
Utah P P P P P
0


Group 1
Debby was nasty about Ann
Bob was nasty about Debby

Group 2
Nobody was nasty
"""

n = int(input())
name_dict = {}
for i in range(n):
    row = list(input().split())
    name_dict[(i, row[0])] = row[1:]
    
cnt = 0
for idx, (k, v) in enumerate(name_dict.items()):
    for i in range(len(v)):
        if v[i] == 'N':
            cnt += 1
            num_backward = len(v) - 1 - i
            if idx - num_backward < 0:
                from_person = list(name_dict.keys())[len(name_dict.keys()) + idx - num_backward][1]    
                to_person = k[1]
                print(f"{from_person} was nasty about {to_person}.")
            else:
                from_person = list(name_dict.keys())[k[1] - num_backward]
                to_person = k[1]
                


