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

if __name__ == '__main__':

    a = index_power([1,2,3,4], 2)
    b = index_power([1,5,100], 0 )
    c = index_power([0,1,3], 5)
    print(a)
    print(b)
    print(c)
