my_list = [1, 2, 3, 4, 5]
def replace_first(my_list):
    return my_list[-1:]+ my_list[0:(len(my_list)-1)] 

if __name__ == '__main__':
    print(list(replace_first(my_list)))
