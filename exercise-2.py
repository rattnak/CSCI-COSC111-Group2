from tokenize import Exponent


def index_power(list,exponent):
    list1 = []
    if exponent == 0:
        return 1
    elif len(list) > exponent:
        for i in list:
            expo = i ** exponent
            list1.append(expo)
        return list1
    
    else:
        return -1

list= [1, 2, 3]
Exponent = 3
a = index_power(list, Exponent)
print(a)