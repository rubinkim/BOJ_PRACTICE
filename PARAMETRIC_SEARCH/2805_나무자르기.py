#-*- coding: utf-8 -*-

"""
시간 제한	메모리제한	  제출	  정답	   맞힌 사람	  정답 비율
1 초	    256 MB	    184127	53932	  33492	        26.002%

상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 
상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.
목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 
절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 
설정할 수 있는 높이는 양의 정수 또는 0이다.
상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 
프로그램을 작성하시오.

4 7
20 15 10 17         15

5 20
4 42 40 26 46       36

20 20   
4 9 7 2 1 8 3 7 4 3 8 9 2 1 7 2 9 1 5 5 

10 110
10 19 20 46 2 16 4 21 30 28

10 101
10 19 20 46 2 16 4 21 30 28
"""
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start, end = 0, max(array)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)









num_trees, target = map(int, input().split())
trees = list(map(int, input().split()))

def get_the_maximum_tree_while(array, target):
    start = 0
    end = max(array)
    cutting_height = 0
    
    while (start <= end):
        mid = (start + end) // 2
        
        total = 0
        for x in array:
            if x > mid:
                total += (x - mid)
        
        if total < target:
            end = mid - 1
        else:
            cutting_height = mid
            start = mid + 1
            
    return cutting_height

print(get_the_maximum_tree_while(trees, target))
"""

import sys
sys.setrecursionlimit(10_000)

num_trees, target = map(int, input().split())
trees = list(map(int, input().split()))
cutting_height = 0

def get_the_maximum_tree_recursion(cnt, array, target, start, end):
    global cutting_height
     
    mid = (start + end) // 2
    total = 0    
      
    for x in array:
        if x > mid:
            total += (x - mid)
    print(f"cnt : {cnt},  total : {total}, cutting_height : {cutting_height}")  
    
    if total == target:
        return cutting_height
            
    elif total < target:
        cnt += 1
        end = mid - 1
        get_the_maximum_tree_recursion(cnt, array, target, start, mid-1)
    else:
        cnt += 1
        cutting_height = mid
        get_the_maximum_tree_recursion(cnt, array, target, mid+1, end)
        

ans = get_the_maximum_tree_recursion(0, trees, target, 0, max(trees))  
print(ans)      
             
             