#-*- coding: utf-8 -*-

"""
 시간 제한	    메모리 제한	    제출	 정답	  맞힌 사람	      정답 비율
  2초	       256 MB	    112859	 33642	   20494	      28.281%

답안 : 3  6  10 
2 4
CAAB
ADCB

3 6
HFDFFB
AJHGDH
DGAGEH

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
"""

r, c = map(int, input().split())
graph = [[0] * c for _ in range(r)]
for i in range(r):
    for j, x in enumerate(input()):
        graph[i][j] = x

for row in graph:
    print(row)