#-*- coding: utf-8 -*-
"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(input().rstrip())
for row in graph:
    print(row)