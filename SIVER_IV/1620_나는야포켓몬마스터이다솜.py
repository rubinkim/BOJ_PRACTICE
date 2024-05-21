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
    lo, hi = 0, len(lst)
    mid = (lo + hi) // 2
    
    x = input()
    if x in list(map(str, range(1, n+1))):
        while lo <= hi:
            if int(x) == lst[mid-1][0]:
                print(f"answer is {lst[mid-1][1]}")
                break
            elif int(x) > lst[mid-1][0]:
                lo = mid + 1
            elif int(x) < lst[mid-1][0]:
                hi = mid - 1
            mid = (lo + hi) // 2
                
    else:
        while lo <= hi:
            if x == lst_by_name[mid-1][1]:
                print(lst_by_name[mid-1][0])
                break
            elif x > lst_by_name[mid-1][1]:
                lo = mid + 1
            elif x < lst_by_name[mid-1][1]:
                hi = mid - 1
            mid = (lo + hi) // 2
    
                
    
    
