#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
arrested        (aerrdets)
"""
word = input()
min_ord = 1e5

for ch in word[:-2]:
    min_ord = min(min_ord, ord(ch))
min_idx = word.index(chr(min_ord))
#print(min_ord)
#print(min_idx)

first_part = word[: min_idx+1]
#print(first_part[::-1])
word = word[min_idx+1 :]
#print(word)

min_ord = 1e5
for ch in word[:-1]:
    min_ord = min(min_ord, ord(ch))
min_idx = word.index(chr(min_ord))
second_part = word[: min_idx+1]
third_part = word[min_idx+1 :]

#print(f"first_part : {first_part},  second_part : {second_part},  third_part : {third_part}")
print(first_part[::-1] + second_part[::-1] + third_part[::-1])
