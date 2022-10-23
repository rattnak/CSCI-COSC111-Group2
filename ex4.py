def split(list, chunk_size):

  for i in range(0, len(list), chunk_size):
    yield list[i:i + chunk_size] 

chunk_size = 3
my_list = [5, 4, 7, 3, 4, 5, 4]
print(list(split(my_list, chunk_size)))
