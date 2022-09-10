def sub_lists(my_list):
    subs = [[]]
    for sub in my_list:
        subs += [i + [sub] for i in subs]
    return subs

print(sub_lists([1,2,3,4]))

from itertools import combinations
l=[1,2,3,4]
sa=[]
for i in range(1,len(l)+1):
    sa+=[*combinations(l,i)]

print(sa)