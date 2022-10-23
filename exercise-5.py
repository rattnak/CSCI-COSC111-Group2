def backward_string_by_word(w):
    rev = ""
    rev += word[::-1]
    return rev
if __name__ == '__main__':
    word = input("Enter a statement you want to reverse: ")
    print(f"Your reversed word is {backward_string_by_word(word)}")
