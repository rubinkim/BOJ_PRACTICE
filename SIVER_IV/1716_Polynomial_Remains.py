"""
5 2
6 3 3 2 0 1
5 2
0 0 3 2 0 1
4 1
1 4 1 1 1
6 3
2 3 -3 4 1 0 1
1 0
5 1
0 0
7
3 5
1 2 3 4
-1 -1

(3 2
-3 -1
-2
-1 2 -3
0
0
1 2 3 4)
"""
n, k = map(int, input().split())
print(f"n : {n},  k : {k}")

coeff_lst = list(map(int, input().split()))
print(f"coeff_lst : {coeff_lst}")
my_lst = []
a_x = 0

def func(n, k, x):    
    global a_x
    for i in range(n):
        a_x += coeff_lst[i] * x ** i
    
    b_x = a_x % (x ** k + 1)

# 이제 b_x를 b_x = b_0 * x ** 0 + b_1 * x ** 1 + b_2 * x ** 2 + ... + b_n-1 * x ** n-1 로 표현하기만 하면 된다.
   

        
           





