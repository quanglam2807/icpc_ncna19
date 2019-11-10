# Quang Lam

n = int(input())

main_str_dict = {}

for i in range(n):
    main_str_dict[input()] = True

map_str_dict = {}

for str in main_str_dict:
    str_dict = main_str_dict.copy()
    str_dict[str] = False
    for j1 in range(len(str)):
        for j2 in range(j1 + 1, len(str), 1):
            l1 = str[j1]
            l2 = str[j2]
            new_str = str.replace(l1, '0').replace(l2, l1).replace('0', l2)
            if new_str in str_dict:
                if str_dict[new_str]:
                    str_dict[new_str] = False

    map_str_dict[str] = str_dict

count_dict = {}

def getCount(lst):
    idx = ''.join(lst)
    if idx in count_dict:
        return count_dict[idx]
    count = 0
    for str in lst:
        k = 1 + getCount([str2 for str2 in lst if map_str_dict[str][str2]])
        if k > count:
            count = k

    count_dict[idx] = count
    return count

print(getCount([str for str in main_str_dict]))