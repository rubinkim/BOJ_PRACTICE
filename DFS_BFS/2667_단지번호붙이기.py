#-*- coding: utf-8 -*-

"""
 ?���? ?��?��	  메모�? ?��?��	?���?	   ?��?��	   맞힌 ?��?��	   ?��?�� 비율
   1 �?	       128 MB	  173059	76869	  48816	         42.315%
  
<그림 1>�? 같이 ?��?��각형 모양?�� �??���? ?��?��. 1??? 집이 ?��?�� 곳을, 0??? 집이 ?��?�� 곳을 ?��????��?��. 철수?�� ?�� �??���? �?�?�? ?��결된 집의 모임?�� ?���?�? ?��?��?���?, ?���??�� 번호�? 붙이?�� ?��?��. 
?��기서 ?��결되?��?��?�� 것�?? ?��?�� 집이 좌우, ?��??? ?��?��?���? ?���? 집이 ?��?�� 경우�? 말한?��. ???각선?��?�� 집이 ?��?�� 경우?�� ?��결된 것이 ?��?��?��. <그림 2>?�� <그림 1>?�� ?���?별로 번호�? 붙인 것이?��. 
�??���? ?��?��?��?�� ?���??���? 출력?���?, �? ?���??�� ?��?��?�� 집의 ?���? ?��름차?��?���? ?��?��?��?�� 출력?��?�� ?��로그?��?�� ?��?��?��?��?��.

?��?�� : �? 번째 줄에?�� �??��?�� ?���? N(?��?��각형?���?�? �?로�?? ?��로의 ?��기는 같으�? 5?��N?��25)?�� ?��?��?���?, �? ?��?�� N줄에?�� 각각 N개의 ?���?(0?��??? 1)�? ?��?��?��?��.
출력 : �? 번째 줄에?�� �? ?���??���? 출력?��?��?��. 그리�? �? ?���??�� 집의 ?���? ?��름차?��?���? ?��?��?��?�� ?�� 줄에 ?��?��?�� 출력?��?��?��.

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
                   
"""

"""       
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
    
graph = [[0] * n for _ in range(n)]
for i in range(n):
    row = input()    
    for j in range(len(row)):
        if row[j] == '1':
            graph[i][j] = 1

path = []
num_dict = {}

def connected_component_mutant(graph, start_x, start_y, num):
    global path, num_dict
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    if graph[start_x][start_y] == 0:
        return False
    if graph[start_x][start_y] == 1 and (start_x, start_y) in path:
        return False
    
    if graph[start_x][start_y] == 1 and (start_x, start_y) not in path:
        q.append((start_x, start_y))
        path.append((start_x, start_y))
        graph[start_x][start_y] = num
        if num not in num_dict.keys():
            num_dict[num] = 1
        
        while q:
            x, y = q.pop()
            cnt = 0
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1 and (nx, ny) in path:
                    continue
                if graph[nx][ny] == 1 and (nx, ny) not in path:
                    q.append((nx, ny))
                    path.append((nx, ny))
                    graph[nx][ny] = num
                    cnt += 1
                    num_dict[num] += 1
        
        return True
    return False

cnt = 1
for i in range(n):
    for j in range(n):
        if connected_component_mutant(graph, i, j, cnt) == True:
            cnt += 1  

print(cnt - 1)
for x in list(num_dict.values()):
    print(x)
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
