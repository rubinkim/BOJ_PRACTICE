#-*- coding: utf-8 -*-
"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수 중에서 M개를 고른 수열
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

4 2
9 7 9 1
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
