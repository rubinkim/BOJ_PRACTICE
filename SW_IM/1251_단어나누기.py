#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
"""
word = input()
min_ord = 1e5

for ch in word:
    min_ord = min(min_ord, ord(ch))
min_idx = word.index(chr(min_ord))
print(min_ord)
print(min_idx)

first_part = word[: min_idx+1]
print(first_part[::-1])
word = word[min_idx+1 :]
print(word)

min_ord = 1e5
for ch in word:
    min_ord = min()
