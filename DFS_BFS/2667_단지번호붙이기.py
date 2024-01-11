#-*- coding: utf-8 -*-

"""
  ?‹œê°? ? œ?•œ	   ë©”ëª¨ë¦? ? œ?•œ	  ? œì¶?	   ? •?‹µ	    ë§íŒ ?‚¬?Œ	    ? •?‹µ ë¹„ìœ¨
   1ì´?	       128 MB	  173059	76869	  48816	         42.315%
  
<ê·¸ë¦¼ 1>ê³? ê°™ì´ ? •?‚¬ê°í˜• ëª¨ì–‘?˜ ì§??„ê°? ?ˆ?‹¤. 1??? ì§‘ì´ ?ˆ?Š” ê³³ì„, 0??? ì§‘ì´ ?—†?Š” ê³³ì„ ?‚˜????‚¸?‹¤. ì² ìˆ˜?Š” ?´ ì§??„ë¥? ê°?ì§?ê³? ?—°ê²°ëœ ì§‘ì˜ ëª¨ì„?¸ ?‹¨ì§?ë¥? ? •?˜?•˜ê³?, ?‹¨ì§??— ë²ˆí˜¸ë¥? ë¶™ì´? ¤ ?•œ?‹¤. 
?—¬ê¸°ì„œ ?—°ê²°ë˜?—ˆ?‹¤?Š” ê²ƒì?? ?–´?–¤ ì§‘ì´ ì¢Œìš°, ?˜¹??? ?•„?˜?œ„ë¡? ?‹¤ë¥? ì§‘ì´ ?ˆ?Š” ê²½ìš°ë¥? ë§í•œ?‹¤. ???ê°ì„ ?ƒ?— ì§‘ì´ ?ˆ?Š” ê²½ìš°?Š” ?—°ê²°ëœ ê²ƒì´ ?•„?‹ˆ?‹¤. <ê·¸ë¦¼ 2>?Š” <ê·¸ë¦¼ 1>?„ ?‹¨ì§?ë³„ë¡œ ë²ˆí˜¸ë¥? ë¶™ì¸ ê²ƒì´?‹¤. 
ì§??„ë¥? ?…? ¥?•˜?—¬ ?‹¨ì§??ˆ˜ë¥? ì¶œë ¥?•˜ê³?, ê°? ?‹¨ì§??— ?†?•˜?Š” ì§‘ì˜ ?ˆ˜ë¥? ?˜¤ë¦„ì°¨?ˆœ?œ¼ë¡? ? •? ¬?•˜?—¬ ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?‘?„±?•˜?‹œ?˜¤.
?…? ¥ : ì²? ë²ˆì§¸ ì¤„ì—?Š” ì§??„?˜ ?¬ê¸? N(? •?‚¬ê°í˜•?´ë¯?ë¡? ê°?ë¡œì?? ?„¸ë¡œì˜ ?¬ê¸°ëŠ” ê°™ìœ¼ë©? 5?‰¤N?‰¤25)?´ ?…? ¥?˜ê³?, ê·? ?‹¤?Œ Nì¤„ì—?Š” ê°ê° Nê°œì˜ ?ë£?(0?˜¹??? 1)ê°? ?…? ¥?œ?‹¤.
ì¶œë ¥ : ì²? ë²ˆì§¸ ì¤„ì—?Š” ì´? ?‹¨ì§??ˆ˜ë¥? ì¶œë ¥?•˜?‹œ?˜¤. ê·¸ë¦¬ê³? ê°? ?‹¨ì§??‚´ ì§‘ì˜ ?ˆ˜ë¥? ?˜¤ë¦„ì°¨?ˆœ?œ¼ë¡? ? •? ¬?•˜?—¬ ?•œ ì¤„ì— ?•˜?‚˜?”© ì¶œë ¥?•˜?‹œ?˜¤.

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
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
def bfs(graph, start_x, start_y):
    global n
    q = deque()
    q.append((start_x, start_y))
    graph[start_x][start_y] = 0
    count = 1
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

count_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count_list.append(bfs(graph, i, j))
            
print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])
"""
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
    
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
path = []
num_dict = {}

# dfs ë°©ì‹
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
            x, y = q.pop()                     # x, y = q.popleft()ë¡? ?•˜ë©? bfs?´?‹¤.
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

num_list = list(num_dict.values())
num_list.sort()
for x in num_list:
    print(x)
"""
