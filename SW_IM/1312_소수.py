#-*- coding: utf-8 -*-
"""
25 7 5

(2)

import math
a, b, n = map(int, input().split())
#print(f"a : {a}, b : {b}, n : {n}")

#print(f"a/b : {a * 10**n / b}")
ln_ans = math.log(a) + n * math.log(10) - math.log(b)
#print(f"ln_ans : {ln_ans}")
ans = math.exp(ln_ans)
ans = str(ans)[:n+1][-1]
#print(f"ans : {ans}")
print(ans)
"""
import math
a, b, n = map(int, input().split())
ln_ans = math.log(a) + n * math.log(10) - math.log(b)
ln_ans_above = math.floor(ln_ans)
print(f"ln_ans : {ln_ans},   ln_ans_above : {ln_ans_above}")
ans = 1

