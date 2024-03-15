#-*- coding: utf-8 -*-
"""
8
0 1 0 1 0 0 0 1
2
1 3
2 3

(1 0 0 0 1 1 0 1)
"""

N = int(input())                        # 스위치 개수
lst = list(map(int, input().split()))   # 스위치 리스트
K = int(input())                        # 학생수
k_lst = []
for _ in range(K):
    gender, switch_num = map(int, input().split())
    k_lst.append((gender, switch_num))
    
print(lst)
print(k_lst)

def switch_motion(sex, switch_num):
    if sex == 1:
        for i in range(switch_num, N):
            if i % switch_num == 0:
                lst[i] = 1 - lst[i]
    else:
        lst[switch_num] = 1 - lst[switch_num]
        
        
      