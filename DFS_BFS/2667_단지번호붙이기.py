#-*- coding: utf-8 -*-

"""
 ?κ°? ? ?	  λ©λͺ¨λ¦? ? ?	? μΆ?	   ? ?΅	   λ§ν ?¬?	   ? ?΅ λΉμ¨
   1 μ΄?	       128 MB	  173059	76869	  48816	         42.315%
  
<κ·Έλ¦Ό 1>κ³? κ°μ΄ ? ?¬κ°ν λͺ¨μ? μ§??κ°? ??€. 1??? μ§μ΄ ?? κ³³μ, 0??? μ§μ΄ ?? κ³³μ ?????Έ?€. μ² μ? ?΄ μ§??λ₯? κ°?μ§?κ³? ?°κ²°λ μ§μ λͺ¨μ?Έ ?¨μ§?λ₯? ? ??κ³?, ?¨μ§?? λ²νΈλ₯? λΆμ΄? € ??€. 
?¬κΈ°μ ?°κ²°λ??€? κ²μ?? ?΄?€ μ§μ΄ μ’μ°, ?Ή??? ???λ‘? ?€λ₯? μ§μ΄ ?? κ²½μ°λ₯? λ§ν?€. ???κ°μ ?? μ§μ΄ ?? κ²½μ°? ?°κ²°λ κ²μ΄ ???€. <κ·Έλ¦Ό 2>? <κ·Έλ¦Ό 1>? ?¨μ§?λ³λ‘ λ²νΈλ₯? λΆμΈ κ²μ΄?€. 
μ§??λ₯? ?? ₯??¬ ?¨μ§??λ₯? μΆλ ₯?κ³?, κ°? ?¨μ§?? ??? μ§μ ?λ₯? ?€λ¦μ°¨??Όλ‘? ? ? ¬??¬ μΆλ ₯?? ?λ‘κ·Έ?¨? ??±???€.

?? ₯ : μ²? λ²μ§Έ μ€μ? μ§??? ?¬κΈ? N(? ?¬κ°ν?΄λ―?λ‘? κ°?λ‘μ?? ?Έλ‘μ ?¬κΈ°λ κ°μΌλ©? 5?€N?€25)?΄ ?? ₯?κ³?, κ·? ?€? Nμ€μ? κ°κ° Nκ°μ ?λ£?(0?Ή??? 1)κ°? ?? ₯??€.
μΆλ ₯ : μ²? λ²μ§Έ μ€μ? μ΄? ?¨μ§??λ₯? μΆλ ₯???€. κ·Έλ¦¬κ³? κ°? ?¨μ§??΄ μ§μ ?λ₯? ?€λ¦μ°¨??Όλ‘? ? ? ¬??¬ ? μ€μ ???© μΆλ ₯???€.

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
                   
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