
def chunking_by(items: list, chunk_size: int):
    for i in range(len(items)):
        if i % chunk_size == 0:
            yield items[i: i + chunk_size]

list1 = ([5, 4, 7, 3, 4, 5, 4], 3)
list2 = ([3, 4, 5], 1)

if __name__ == '__main__':

    a = list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
    b = list(chunking_by([3, 4, 5], 1))
    
    print(f'for{list1}, the return value is {a}.')
    print(f'for{list2}, the return value is {b}.')


