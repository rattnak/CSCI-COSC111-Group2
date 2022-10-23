def index_power(list,exponent):
    list1 = []
    
    if len(list) >= exponent:
        list1 = list[exponent] ** exponent
        return list1
    elif exponent == 0:
        return 1
    else:
        return -1
list1 = ([1, 2, 3, 4], 2)
list2 = ([1, 3, 10, 100], 3)
list3 = ([0,1,2], 5)
list4 = ([1, 2], 3)

if __name__ == '__main__':

    a = index_power([1, 2, 3, 4], 2)
    b = index_power([1, 3, 10, 100], 3)
    c = index_power([0, 1], 0)
    d = index_power([1, 2], 3)
    
    print(f'for{list1}, the return value is {a}.')
    print(f'for{list2}, the return value is {b}.')
    print(f'for{list3}, the return value is {c}.')
    print(f'for{list4}, the return value is {d}.')
