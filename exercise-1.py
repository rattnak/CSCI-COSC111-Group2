original_list = [2, 3, 4, 1]
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

print(reverse_list([2,3,4,1]))
