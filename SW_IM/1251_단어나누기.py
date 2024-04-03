#-*- coding: utf-8 -*-
"""
mobitel         (bometil)

arrested        (ratserde)
"""
word = input()
min_ch = 1e5

for ch in word:
    min_ch = min(min_ch, ord(ch))
min_idx = word.index(ch(min_ch))