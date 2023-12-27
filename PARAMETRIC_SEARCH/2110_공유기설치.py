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
#print(f"n : {n},  c : {c}")
#print(f"houses : {houses}")
          
house_dist = []
for i in range(1, len(houses)):
    house_dist.append(houses[i] - houses[i-1])
#print(f"house_dist : {house_dist}")

while len(house_dist) >= c-1:
    min_idx = house_dist.index(min(house_dist))
    #print(f"min_idx : {min_idx}")
    if min_idx == 0:
        min_idx_val = house_dist[0] + house_dist[1]
        house_dist = [min_idx_val] + house_dist[2:]

    elif min_idx == len(house_dist) - 1:
        min_idx_val = house_dist[-2] + house_dist[-1]
        house_dist = house_dist[:-2] + [min_idx_val]
        
    else:
        if house_dist[min_idx-1] < house_dist[min_idx+1]:
            min_idx_val = house_dist[min_idx-1] +house_dist[min_idx]
            house_dist = house_dist[:min_idx-1] + [min_idx_val] + house_dist[min_idx+1:]
        else:
            min_idx_val = house_dist[min_idx] + house_dist[min_idx+1]
            house_dist = house_dist[:min_idx] + [min_idx_val] + house_dist[min_idx+2:]    
        
    c += 1
    #print(f"c : {c},  house_dist : {house_dist}" )

max_nearest_dist = min(house_dist)
print(max_nearest_dist)