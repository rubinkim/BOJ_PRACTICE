#-*- coding: utf-8 -*-

"""
4
1 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919
2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900
3 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 900
4 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900 919

1 0
2 190
3 19
4 171


P = int(input())       # 테스트 케이스의 수

tc_dict = {}
for i in range(P):
    lst = list(map(int, input().split()))
    tc_dict[lst[0]] = lst[1:]
   
for k, v in tc_dict.items():
    print(k, v)

    
for x in range(1, P+1):
    ans = 0
    for i in range(20):
        for j in range(0, i):
            if tc_dict[x][j] > tc_dict[x][i]:
                for k in range(j, i):
                    tc_dict[x][k+1] = tc_dict[x][k]
                    ans += 1
                tc_dict[x][j] = tc_dict[x][i]
            break
        
    print(x, ans)
"""    

P = int(input())
tc_dict = {}
for i in range(P):
    lst = list(map(int, input().split()))
    tc_dict[lst[0]] = lst[1:]
    
for k, v in tc_dict.items():