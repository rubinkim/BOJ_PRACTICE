#-*- coding: utf-8 -*-
"""
0001100
(1)

11111
(0)

00000001
(1)

11001100110011000001
(4)

11101101
(2)
"""
s = list(input())
cnt_zero, cnt_one = 0, 0    # cnt_zero : number of flipping to make every element zero,  cnt_one : vice versa
i = 1
while i <= len(s)-1:
    if s[i-1] != s[i] and s[i] == '1':
        cnt_one += 1        
    elif s[i-1] != s[i] and s[i] == '0':
        cnt_zero += 1
    i += 1
if s[-1] == '1':
    cnt_zero += 1
if s[-1] == '0':
    cnt_one += 1      
    
#print(f"cnt_zero : {cnt_zero},   cnt_one : {cnt_one}")
print(min(cnt_zero, cnt_one))
        

        
        
            
    
     
    