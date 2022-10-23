def chunking_by(items: list, chunk_size: int):
    return [items[i: i + chunk_size] for i in range(len(items)) if i % chunk_size == 0]

if __name__ == '__main__':
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))
