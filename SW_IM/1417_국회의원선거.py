#-*- coding: utf-8 -*-
"""
3
5
7
7

(2)
"""
n = int(input())
votes = []
for i in range(n):
    votes.append(int(input()))
    
max_vote = 0

while True:
    max_vote = max(max_vote, votes[1:])

    
