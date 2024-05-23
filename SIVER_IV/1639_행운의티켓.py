#-*- coding: utf-8 -*-
"""
74233285
(4)

123231
(6)

986561517416921217551395112859219257312
(36)

1
(0)

112
(2)
"""
s = list(map(int, input()))

half = len(s) // 2
if len(s) % 2 == 0:
    if sum(s[0:half]) == sum(s[half:len(s)]):
        print(len(s))
    else:
        decrement = 2
        flag = False
        while True:
            if len(s) - decrement <= 1:
                ans = 0
                print(ans)
                break
            half = (len(s) - decrement) // 2
            ans = 0
            for i in range(0, decrement+1):
                if sum(s[i:i+half]) == sum(s[i+half:i+2*half]):
                    ans = 2 * half
                    print(ans)
                    flag = True
                    break
            if flag == True:
                break   
            else:
                decrement += 2
                
else:
    if sum(s[0:half]) == sum(s[half:len(s)-1]):        
        print(len(s)-1)        
    elif sum(s[1:half+1]) == sum(s[half+1:len(s)]):
        print(len(s)-1)
    else:
        for j in range(2):
            decrement = 2
            flag = False
            while True:
                if len(s) - 1 - decrement <= 1:
                    ans = 0
                    print(ans)
                    break
                half = (len(s)-1-decrement) // 2
                ans = 0
                for i in range(0, decrement+1):
                    if sum(s[i+j:i+j+half]) == sum(s[i+j+half:i+j+2*half]):
                        ans = 2 * half
                        print(ans)
                        flag = True
                        break
                if flag == True:
                    break  
                else:
                    decrement += 2
            if flag == True:
                break
            



            