#-*- coding: utf-8 -*-
"""
5
picture
turepic
icturep
word
ordw
(2)

7
ast
ats
tas
tsa
sat
sta
ttt
(3)

5
aaaa
aaa
aa
aaaa
aaaaa
(4)
"""

n = int(input())

word_dict = {}
word = input()
word_dict[word] = [word]

for _ in range(n-1):
    word = input()
    for i in range(len(word)):
        if word[i:] + word[:i] in word_dict.keys():
            break
        