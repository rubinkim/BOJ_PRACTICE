#-*- coding: utf-8 -*-
"""
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

(Pikachu
26
Venusaur
16
14)
"""
n, m = map(int, input().split())
lst = []

for i in range(n):
    x = input()
    lst.append((i+1, x))
    
lst_by_name = sorted(lst, key=lambda x : x[1])

for _ in range(m):
    lo, hi = 0, len(new_lst)
    mid = (lo + hi) // 2
    
    x = input()
    if int(x) in list(range(1, n+1)):
        while lo <= hi:
            if int(x) == new_lst[mid-1][0]:
                print(new_lst[mid-1][1])
                break
            elif int(x) > new_lst[mid-1][0]:
                lo = mid + 1
            elif int(x) < new_lst[mid-1][0]:
                hi = mid - 1
            mid = (lo + hi) // 2
                
    else:
        while lo <= hi:
            if x == new_lst[mid-1][1]:
                print(new_lst[mid-1][0])
                break
            elif x > new_lst[mid-1][1]:
                lo = mid + 1
            elif x < new_lst[mid-1][1]:
                hi = mid - 1
            mid = (lo + hi) // 2
    
                
    
    
