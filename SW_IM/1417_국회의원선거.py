#-*- coding: utf-8 -*-
"""
3
5
7
7

(2)

4
10
10
10
10

(1)
"""
n = int(input())
votes = []
for i in range(n):
    votes.append(int(input()))
    
max_vote = 0
cnt = 0

while True:
    max_vote = max(max_vote, max(votes))
    max_vote_idx = votes.index(max_vote)
    
    if max_vote_idx == 0 and votes.count(max_vote) == 1:
        print(cnt)
        break
    elif max_vote_idx == 0 and votes.counts(max_vote) > 1:
        cnt += 1
        votes[0] += 1
        nxt_max_vote_idx = max(votes[1:])
        votes[nxt_max_vote_idx] -= 1
    elif max_vote_idx > 0:
        cnt += 1
        votes[0] += 1
        votes[max_vote_idx] -= 1

    
