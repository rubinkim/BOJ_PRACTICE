#-*- coding: utf-8 -*-
"""
8
0 1 0 1 0 0 0 1
2
1 3
2 3

(1 0 0 0 1 1 0 1)
"""

N = int(input())                        # ����ġ ����
lst = list(map(int, input().split()))   # ����ġ ����Ʈ
K = int(input())                        # �л���
k_lst = []
for _ in range(K):
    gender, switch_num = map(int, input().split())
    k_lst.append((gender, switch_num))
      