#-*- coding: utf-8 -*-
"""
9999
(2)

122
(2)

12635
(1)

888888
(6)

126549666
(3)
"""

from collections import Counter
lst = list(map(int, input()))     # 126549666
#print(lst)

num_dict = Counter(lst)
#print(num_dict)

if num_dict[6] and num_dict[9]:
    if (num_dict[6] + num_dict[9]) % 2 == 0:
        num_dict[6] += num_dict[9]
        num_dict[6] = num_dict[6] // 2
        del num_dict[9]
    elif (num_dict[6] + num_dict[9]) % 2 == 1:
        num_dict[6] += num_dict[9]
        num_dict[6] = num_dict[6] // 2 + 1
        del num_dict[9]

elif not num_dict[6] and num_dict[9]:
    if num_dict[9] % 2 == 0:
        num_dict[9] = num_dict[9] // 2
    elif num_dict[9] % 2 == 1:
        num_dict[9] = num_dict[9] // 2 + 1
        
elif num_dict[6] and not num_dict[9]:
    if num_dict[9] % 2 == 0:
        num_dict[9] = num_dict[9] // 2
    elif num_dict[9] % 2 == 1:
        num_dict[9] = num_dict[9] // 2 + 1
            
#print(num_dict)
print(max(num_dict.values()))