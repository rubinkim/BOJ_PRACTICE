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
s = list(input())
half = len(s) // 2
if len(s) % 2 == 0:
    if sum(s[0:half]) == sum(s[half:len(s)]):
        print(len(s))
    else:
        while True:
            decrement = 2
            half = (len(s) - decrement) // 2
            ans = 0
            for i in range(0, decrement):
                if sum(s[i:i+half]) == sum(s[i+half:i+2*half]):
                    ans = 2 * half
                    print(ans)
                    break
            else:
                decrement += 2
            if decrement >= len(s):
                ans = 0
                print(ans)
                break


            