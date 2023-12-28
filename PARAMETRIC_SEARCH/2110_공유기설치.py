"""

시간 제한	메모리 제한	   제출	   정답	   맞힌 사람	   정답 비율
 2 초	     128 MB  	 68527	 23951	 16656	         36.011%

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

5 3
1
2
8
4
9          3
"""

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
print(f"n : {n},  c : {c}")
print(f"houses : {houses}")

max_nearest_dist = 0

def calculate_max_nearest_dist(array):
    global max_nearest_dist
    start = 1                            # 공유기를 설치할 집들간의 최소거리를 1로 초기화한다.
    end = array[-1] - array[0]           # 공유기를 설치할 집들간의 최대거리를 끝집과 첫번째집간의 거리차로 초기화한다.
        
    while start <= end:
        mid = (start + end) // 2
        count = 1
        current = array[0]
        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]
        if count >= c:
            max_nearest_dist = mid
            start = mid + 1
        else:
            end = mid - 1
            
calculate_max_nearest_dist(houses)
print(max_nearest_dist)
          
