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
try:
    n, k = 0, 0
    while n != -1 and k != -1:
        n, k = map(int, input().split())
        coeff_lst = list(map(int, input().split()))
        if k == 0:
            print(0)
            continue
        if n < k:
            print(*coeff_lst)
        if n >= k:
            coeff_lst = coeff_lst[::-1]
            divisor = [0] * (n+1)
            divisor[0] = 1
            divisor[k] = 1     

            i = 0
            while True:
                if coeff_lst[i] != 0:
                    divisor = [coeff_lst[i] * x for x in divisor]
                    coeff_lst = [coeff_lst[j] - divisor[j] for j in range(n+1)]
                    for m in range(n+1):
                        if coeff_lst[m] != 0:
                            nonzero_idx = m
                            break
                    divisor = [0] * (n+1)
                    divisor[nonzero_idx] = 1            
                    divisor[nonzero_idx + k] = 1
                else:
                    i += 1
                if nonzero_idx + k == n:
                    divisor = [coeff_lst[nonzero_idx] * x for x in divisor]
                    coeff_lst = [coeff_lst[j] - divisor[j] for j in range(n+1)]
                    coeff_lst = coeff_lst[::-1]
                    ans = []
                    for x in coeff_lst:
                        if x != 0:
                            ans.append(x)
                    print(*ans)
                    break
except EOFError:
    exit(0)


    
        
           





