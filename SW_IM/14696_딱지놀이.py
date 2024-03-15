#-*- coding: utf-8 -*-
"""
5
1 4
4 3 3 2 1
5 2 4 3 2 1
4 4 3 3 1
4 3 2 1 1
4 2 3 2 1
4 4 3 2 1
3 4 3 2
5 4 4 2 3 1
5 4 2 4 1 3

A B B A D


4
4 4 3 2 1
4 1 4 3 2
4 3 3 2 1
4 4 3 3 3
4 4 3 3 3
4 3 4 3 2
4 3 2 1 1
3 3 2 1

D B A A


N = int(input())
for i in range(N):
    card_dict = {1 : [0, 0], 2 : [0, 0], 3 : [0, 0], 4 : [0, 0]}
    A_lst = list(map(int, input().split()))[1:]
    #A_lst = A_lst[1:]
    print(f"i : {i},  A_lst : {A_lst}")
    B_lst = list(map(int, input().split()))[1:]
    #B_lst = B_lst[1:]
    print(f"i : {i},  B_lst : {B_lst} ")
    
    for x in A_lst:
        card_dict[x][0] += 1
    for x in B_lst:
        card_dict[x][1] += 1
        
    print(f"i : {i},  card_dict :  {card_dict}")
    
    if card_dict[4][0] > card_dict[4][1]:
        print('A')
        break
    elif card_dict[4][0] < card_dict[4][1]:
        print('B')
        break
    elif card_dict[4][0] == card_dict[4][1]:
        if card_dict[3][0] > card_dict[3][1]:
            print('A')
            break
        elif card_dict[3][0] < card_dict[3][1]:
            print('B')
            break
        elif card_dict[3][0] == card_dict[3][1]:
            if card_dict[2][0] > card_dict[2][1]:
                print('A')
                break
            elif card_dict[2][0] < card_dict[2][1]:
                print('B')
                break
            elif card_dict[2][0] == card_dict[2][1]:
                if card_dict[1][0] > card_dict[1][1]:
                    print('A')
                    break
                elif card_dict[1][0] < card_dict[1][1]:
                    print('B')
                    break
                elif card_dict[1][0] == card_dict[1][1]:
                    print('D')
                    break
"""

N = int(input())
for i in range(N):
    card_dict = {1 : [0, 0], 2 : [0, 0], 3 : [0, 0], 4 : [0, 0]}
    A_lst = list(map(int, input().split()))[1:]
    #A_lst = A_lst[1:]
    print(f"i : {i},  A_lst : {A_lst}")
    B_lst = list(map(int, input().split()))[1:]
    #B_lst = B_lst[1:]
    print(f"i : {i},  B_lst : {B_lst} ")
    
    for x in A_lst:
            card_dict[x][0] += 1
    for x in B_lst:
        card_dict[x][1] += 1
        
    print(f"i : {i},  card_dict :  {card_dict}")
    
    print(f"card_dict[2][0] : {card_dict[2][0]}, card_dict[2][1] : {card_dict[2][1]}")