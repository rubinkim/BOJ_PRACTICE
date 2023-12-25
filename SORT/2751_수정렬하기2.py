#-*- coding: utf-8 -*-

"""
시간 제한	메모리제한	  제출	  정답	   맞힌 사람	  정답 비율
2 초	    256 MB	   293962	 88351	   61657	    31.050%

N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

5
5
4
3
2
1
"""

import sys
input = sys.stdin.readline
n = int(input())

array = []
for _ in range(n):
    x = int(input())
    array.append(x)
array.sort()

for x in array:
    print(x)
    

    
