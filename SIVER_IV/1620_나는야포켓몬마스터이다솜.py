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
lst_num_name = []
lst_name = []


for i in range(n):
    x = input()
    lst_num_name.append((i+1, x))
    lst_name.append(x)
    
for _ in range(m):
    x = input()
    if x in list(map(str, range(1, n+1))):
        print(lst_num_name[int(x)-1][1])        
    else:
        print(lst_name.index(x) + 1)
        
                
    
    
