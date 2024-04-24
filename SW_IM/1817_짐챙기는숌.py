#-*- coding: utf-8 -*-
"""
6 10
5 5 5 5 5 5
(3)

5 100
51 51 51 51 51
(5)

6 8
1 1 1 7 7 7
(4)

11 12
12 1 11 2 10 3 4 5 6 6 1
(6)

0 7
(0)
"""
n, m = map(int, input().split())
lst = list(map(int, input().split()))

book_weight = 0
cnt = 1             # no. of boxes to put books in

while len(lst) >= 0:          
    last_bw = lst.pop()
    book_weight += last_bw
    if book_weight > m:
        cnt += 1
        book_weight = last_bw
if n == 0:
    cnt = 0       
        
print(cnt)