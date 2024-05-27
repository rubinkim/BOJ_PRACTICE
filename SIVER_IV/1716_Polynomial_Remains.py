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

def func_x(n, k, x):
    a_x = 0
    for i in range(len(coeff_lst)):
        a_x += coeff_lst[i] * x ** i    

    remaining_lst = []
    for c in range(len(coeff_lst)):
        remaining = a_x / (x**k + 1)
        remaining_lst.append(remaining)
    return remaining_lst
        



