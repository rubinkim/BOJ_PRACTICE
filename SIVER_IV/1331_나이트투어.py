#-*- coding: utf-8 -*-
"""
A1
B3
A5
C6
E5
F3
D2
F1
E3
F5
D4
B5
A3
B1
C3
A2
C1
E2
F4
E6
C5
A6
B4
D5
F6
E4
D6
C4
B6
A4
B2
D1
F2
D3
E1
C2

(Valid)


A1
C2
E3
F5
D4
B3
A1
C2
E3
F5
D4
B3
A1
C2
E3
F5
D4
B3
A1
C2
E3
F5
D4
B3
A1
C2
E3
F5
D4
B3
A1
C2
E3
F5
D4
B3

(Invalid)


D4
F5
D6
B5
A3
B1
D2
F1
E3
D1
F2
E4
F6
D5
B6
A4
B2
C4
A5
C6
E5
F3
E1
C2
A1
B3
C5
E6
F4
E2
C3
A2
C1
D3
B4
A6

(Invalid)


D4
F5
D6
B5
A3
B1
D2
F1
E3
D1
F2
E4
F6
D5
B6
A4
B2
C4
A5
C6
E5
F3
E1
C2
A1
B3
C5
A6
B4
A2
C3
E2
C1
D3
F4
E6

(Valid)
"""
chk = [[False] * 6 for _ in range(6)]
moves = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]
x, y = input()
x = ord(x) - ord('A')
y = int(y) - 1
print(f"y : {y},  x : {x}")

for _ in range(1):
    new_x, new_y = input()
    new_x = ord(new_x) - ord('A')
    new_y = int(new_y) - 1
    print(f"new_y : {new_y},  new_x : {new_x}")
    
    for i in range(len(moves)):
        ny = y + moves[i][0]
        nx = x + moves[i][1]
        if ny == new_y and nx == new_x and not chk[new_y][new_x] and 0 <= new_y <= 5 and 0 <= new_x <= 5:
            y = new_y
    


