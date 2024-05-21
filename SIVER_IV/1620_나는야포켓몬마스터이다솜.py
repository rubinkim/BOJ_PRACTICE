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

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lst = []

for i in range(n):
    lst.append(input().rstrip())
    
for _ in range(m):
    x = input().rstrip()
    if x in list(map(str, range(1, n+1))):
        print(lst[int(x)-1])                
    else:
        print(lst.index(x) + 1)
"""     
                
import sys
input = sys.stdin.readline    
    
n, m = map(int, input().rstrip().split())
lst = []

for i in range(n+m):
    if 0 <= i <= n-1:
        lst.append(input().rstrip())
    