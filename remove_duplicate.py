def remove_duplicates(s):
    k = []
    for i in s:
        if i not in k:
            k.append(i)
    return ''.join(k)
    
print(remove_duplicates('sajgsduwwjns'))
            
print(''.join(dict.fromkeys('cjclchbxnb')))
    
