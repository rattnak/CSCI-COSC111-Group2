def remove(list, S:int):
    if S not in list:
        return list
    else:
        cut = list.index(S)
        result = list[:cut + 1]
        return result
if __name__ == '__main__':
    final_result1 = remove([1, 2, 3, 4, 5], 3)
    final_result2 = remove([1, 1, 2, 2, 3, 3], 2)
    print(final_result1)
    print(final_result2)
