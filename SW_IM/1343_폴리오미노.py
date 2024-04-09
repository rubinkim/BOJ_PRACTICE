#-*- coding: utf-8 -*-
"""
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX

(BB.AAAAAAAABB..AAAAAAAA...AAAABB)
"""
board = list(input())
cnt = 0
poly = []

for i, ch in enumerate(board):
    if ch == 'X':
        cnt += 1
    elif ch == '.':
        poly.append(0)
        poly.append(cnt)
        cnt = 0
    if i == len(board)-1 and board[-1] == 'X':
        poly.append(cnt)
        
print(poly)

num_poly = []

def convert_to_ch(poly):
    global num_poly
    
    for num in poly:
        if num % 2 == 1:
            print(-1)
            break
        else:
            if num >= 4:
                num_poly.append('AAAA' * (num//4))
                num -= 4 * (num//4)
            if num == 2:
                num_poly.append('BB')
            if num == 0:
                num_poly.append('.')
                
convert_to_ch(poly)               
print(''.join(num_poly))

        


            
            
