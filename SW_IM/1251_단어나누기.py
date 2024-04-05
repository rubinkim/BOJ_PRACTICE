#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
arrested        (aerrdets)
"""
import sys
input = sys.stdin.readline
word = list(input().rstrip('\n'))
print(word)

res = []

for i in range(1, len(word)):
    for j in range(len(word)):
        first_part = word[:i]
        second_part = word[i:j]
        third_part = word[j:]
        
        first_part.reverse()
        second_part.reverse()
        third_part.reverse()

        res.append("".join(first_part + second_part + third_part))
        
print(min(res))
