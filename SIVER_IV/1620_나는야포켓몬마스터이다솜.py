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
    lst.append(input())
    
lst.sort(key=lambda x : x[1])

new_lst = []
for i in range(len(lst)):
    new_lst.append((i+1, lst[i]))
    
print(new_lst)

