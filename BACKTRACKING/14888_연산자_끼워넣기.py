#-*- coding: utf-8 -*-

"""
6
1 2 3 4 5 6
2 1 1 1

2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

"""
"""
N = int(input())                              # 숫자의 개수
nums = list(map(int, input().split()))        # 크기가 N인 숫자배열
ops = ['+', '-', '*', '//']                    # 연산자의 종류
op_nums = list(map(int, input().split()))     # 4종류인 연산자들의 크기들의 배열 = N - 1

operators = []                                # 크기가 N-1인 연산자배열
for i in range(len(ops)):
    for _ in range(op_nums[i]):
        operators.append(ops[i])
        
from itertools import permutations

op_list = []
for i in permutations(operators, len(operators)):
    if i not in op_list:
        op_list.append(i)
        
ans_list = []

def dfs(n, i):                            # n : 현재 작업중인 숫자의 nums 리스트에서의 index,   i : 현재 작업중인 연산자배열의 op_list에서의 인덱스
    global ans_list, ans
    
    if n == N-1:
        ans_list.append(ans)
        return    
    else:
        if op_list[i][n] == '+':
            ans += nums[n+1]
        elif op_list[i][n] == '-':
            ans -= nums[n+1]
        elif op_list[i][n] == '*':
            ans *= nums[n+1]
        elif op_list[i][n] == '//':
            if ans < 0:
                ans = -((-ans) // nums[n+1])
            else:
                ans = ans // nums[n+1]     
    dfs(n+1, i)
    
for i in range(len(op_list)):
    ans = nums[0]
    dfs(0, i)

print(max(ans_list))
print(min(ans_list))
"""
"""
# DFS  : plus, minus, multiply, divide를 divide, multiply, minus, plus로 바꿔도 정답이다!!!
import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9

def dfs(n, total, plus, minus, multiply, divide):
    global maximum, minimum
    if n == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(n+1, total+num[n], plus-1, minus, multiply, divide)
    if minus:
        dfs(n+1, total-num[n], plus, minus-1, multiply, divide)
    if multiply:
        dfs(n+1, total*num[n], plus, minus, multiply-1, divide)
    if divide:
        dfs(n+1, int(total/num[n]), plus, minus, multiply, divide-1)
        
dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
"""

# Permutations
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op_num = []

for i in range(len(op)):
    for j in range(op[i]):
        op_num.append(op_list[i])

maximum = -1e9
minimum = 1e9
        
def solve():
    global maximum, minimum
    for case in permutations(op_num, N-1):
        total = num[0]
        for i in range(1, N):
            if case[i-1] == '+':
                total += num[i]
            elif case[i-1] == '-':
                total -= num[i]
            elif case[i-1] == '*':
                total *= num[i]
            elif case[i-1] == '/':
                total = int(total / num[i])
        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total
            
solve()
print(maximum)
print(minimum)
