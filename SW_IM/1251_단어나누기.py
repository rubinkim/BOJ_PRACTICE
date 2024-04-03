#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
"""
word = input()
min_ch = 1e5

for ch in word:
    min_ch = min(min_ch, ord(ch))
min_idx = word.index(ch(min_ch))
print(min_idx)