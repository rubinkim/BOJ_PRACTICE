#-*- coding: utf-8 -*-

"""
 시간 제한	  메모리 제한	제출	정답	 맞힌 사람	   정답 비율
    1 초	   256 MB	  9363	  3287	    2393	    35.882%
  
명절이 되면, 홍익이 집에는 조카들이 놀러 온다. 떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.
조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.
그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.
M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.
단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.

입력 : 첫째 줄에 조카의 수 M (1 ≤ M ≤ 1,000,000), 과자의 수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
      둘째 줄에 과자 N개의 길이 L1, L2, ..., LN이 공백으로 구분되어 주어진다. 과자의 길이는 (1 ≤ L1, L2, ..., LN ≤ 1,000,000,000) 를 만족한다.
출력 : 첫째 줄에 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 출력한다. 단, 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0을 출력한다.

3 10
1 2 3 4 5 6 7 8 9 10           8

4 3
10 10 15                       7
"""

import sys
input = sys.stdin.readline

m, n = map(int, input().split())          
array = list(map(int, input().split()))

start, end = 1, max(array)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    for i in range(len(array)):
        if array[i] >= mid:
            cnt += array[i] // mid    
    
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)