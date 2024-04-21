#-*- coding: utf-8 -*-
"""
1234567

3
NO

import time
start = time.time()

import sys
input = sys.stdin.readline
x = int(input())
x_added = 0
i = 0
while True:
    if x < 1 and x_added >= 10:
        x = x_added
        x_added = 0
        i += 1
    if x < 1 and x_added < 10:
        i += 1
        break
        
    remainder = x % 10  
    x //= 10
    x_added += remainder
print(i)
print("YES" if x_added % 3 == 0 else "NO")

end = time.time()
print(f"time elapsed : {end - start}")
"""
x = list(input())
cnt = 0

while len(x) >= 1:
    if len(x) == 1:
        x_added = int(x[0])
        print(cnt)
        print('YES' if x_added % 3 == 0 else 'NO')
        break
    x_added = sum([int(i) for i in range(x)])
    cnt += 1
    
    if x_added < 10:
        print(cnt)
        print('YES' if x_added % 3 == 0 else 'NO')
    else:
        x = list(str(x_added))
        