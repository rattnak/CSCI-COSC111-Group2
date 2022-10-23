def reverse_list(original_list): 
    if len(original_list) <= 1:
        return original_list
    else:
        last_value = original_list[len(original_list) - 1]
        new_list = []
        new_list.insert(0, last_value)
        original_list.pop()
        for value in original_list:
            new_list.append(value)    
        return new_list    

list1 = ([2, 3, 4, 1])
list2 = ([1,2,3,4])
list3 = ([1])
list4 = ([])

if __name__ == '__main__':

    a = reverse_list([2, 3, 4, 1])
    b = reverse_list([1,2,3,4])
    c = reverse_list([1])
    d = reverse_list([])
    
    print(f'for{list1}, the return value is {a}.')
    print(f'for{list2}, the return value is {b}.')
    print(f'for{list3}, the return value is {c}.')
    print(f'for{list4}, the return value is {d}.')