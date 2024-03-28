"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

(5)


5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

(10)


5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

(11)


5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1

(32)

"""
from itertools import combinations

N, M = map(int, input().split())     # N : one-side length of the city,  M : maximum number of chicken houses
houses, chickens = [], []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))
            
print(f"houses : {houses}")
print(f"chickens : {chickens}")

ans = 2 * N * len(houses)      # 도시의 치킨거리의 최솟값을 구하는 문제이므로 default로 매우 큰값을 할당하였다.

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for combi in combinations(chickens, M):
    tot = 0     # 이번 combi에서의 도시의 치킨거리의 최솟값
    for house in houses:
        tot += min(get_dist(house, chicken) for chicken in combi)
    print(f"combi : {combi},  tot : {tot}")