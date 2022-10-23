def remove_all_after(list,num):
    list1 = []
    for i in list:
        if i <= num:
            list1.append(i)
    return list1

list = [1,2,2,3,3,4,4,4,5,6,7,8,9]
num = 4

a = remove_all_after(list,num)
print(a)
