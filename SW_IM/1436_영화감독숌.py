#-*- coding: utf-8 -*-
"""
187
(66666)

500
(166699)
"""
import time
import sys

start = time.time()
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(100000001):
    if '666' in str(i):
        cnt += 1
    if cnt == n:
        print(i)
        break
end = time.time()

print(f"time elapse : {end - start}")