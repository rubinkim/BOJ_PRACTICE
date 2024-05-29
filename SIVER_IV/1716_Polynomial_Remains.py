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
n, k = 0, 0
while n != -1 and k != -1:
    n, k = map(int, input().split())
    coeff_lst = list(map(int, input().split()))
    coeff_lst = coeff_lst[::-1]
    divisor = [0] * (n+1)
    divisor[0] = 1
    divisor[k] = 1
    
    i = 0




    
        
           





