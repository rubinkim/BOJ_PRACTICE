#-*- coding: utf-8 -*-
"""
3
1212345
1212356
0033445
"""
n = int(input())
student_nums = []
for _ in range(n):
    student_nums.append(input())
print(student_nums)

num_len = len(student_nums[0])
print(num_len)


for i in range(num_len-1, -1, -1):
    for j in range(len(student_nums)):
        print(student_nums[j][i:], end=" ")
    print()