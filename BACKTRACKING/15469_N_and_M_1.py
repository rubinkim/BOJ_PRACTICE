#-*- coding: utf-8 -*-

"""
시간 제한	메모리 제한	   제출	    정답	맞힌 사람	정답 비율
 1 초	   512 MB	    102276	  65176	   41867	  62.787%
 
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

입력 : 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
      수열은 사전 순으로 증가하는 순서로 출력해야 한다.
      
3 2
4 2
4 3
4 4
"""
"""
n, m = map(int, input().split())
visited = [False] * (n+1)
ans = []

def n_and_m(depth, n, m):
    if depth == m:
        print(" ".join(map(str, ans)))
        
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            print(f"before => depth+1 : {depth+1},  i : {i},  visited : {visited},  ans : {ans}")
            
            n_and_m(depth+1, n, m)
            visited[i] = False
            ans.pop()
            print(f"after  => depth+1 : {depth+1},  i : {i},  visited : {visited},  ans : {ans}")
        
n_and_m(0, n, m)
"""
n, m = map(int, input().split())
ans = []
visited = [False] * (n+1)

def n_and_m(depth, n, m):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            n_and_m(depth+1, n, m)
            ans.pop()
            
n_and_m(0, n, m)
        