#-*- coding: utf-8 -*-
"""
시간 제한	메모리 제한	  제출	   정답	   맞힌 사람	정답 비율
  10 초	     128 MB	    107545	 51566	  33491	      46.555%
  
N-Queen 문제는 크기가 N*N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
출력 : 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

8     92
"""
import sys
input = sys.stdin.readline
N = int(input())
ans = 0
v1 = [0] * N
v2 = [0] * (2 * N)
v3 = [0] * (2 * N)

def dfs(n):
  global ans
  if n == N:
        ans += 1
        return
  for j in range(N):
    if v1[j] == v2[n+j] == v3[n-j] == 0:
          v1[j] = v2[n+j] = v3[n-j] = 1
          dfs(n+1)
          v1[j] = v2[n+j] = v3[n-j] = 0
          
dfs(0)
print(ans)
      


  
  