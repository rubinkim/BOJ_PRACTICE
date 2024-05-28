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
    
    my_lst = [0] * n
    b_x = a_x % (x ** k + 1)
    
    for i in range(n):
        my_lst[i] = b_x / x ** i
        
    return my_lst

print(func(n, k, 2))
        
           





