#-*- coding: utf-8 -*-
"""
N���� �ڿ����� �ڿ��� M�� �־����� ��, �Ʒ� ������ �����ϴ� ���̰� M�� ������ ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�. N���� �ڿ����� ��� �ٸ� ���̴�.
N���� �ڿ��� �߿��� M���� �� ����
������ ���� ������ �����ϴ� ������ ����ؾ� �Ѵ�.

4 2
9 8 7 1
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(N):
        dfs(n+1, lst+[nums[j]])
        
dfs(0, [])
for lst in ans:
    print(*lst)