def un(arr):
    l = list(set(arr))
    emt_list = list()
    for i in l:
        c = 0
        c = arr.count(arr[arr.index(i)])
        emt_list.append(c)
    new_set = set(emt_list)
    if len(new_set) == len(emt_list):
        return True
    return False   
    
arr = [1,2]
print(un(arr))