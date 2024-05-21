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
    x = x.lower()
    lst.append(x)
    
lst.sort()

new_lst = []
for i in range(n):
    new_lst.append((i+1, lst[i]))
    
#print(new_lst)

for _ in range(m):
    lo, hi = 0, len(new_lst)-1
    mid = (lo + hi) // 2
    ans = 0
    
    x = input()
    if x in list(map(str, range(1, n+1))):
        
    
    
