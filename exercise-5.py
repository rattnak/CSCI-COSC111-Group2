str1 = ''
str2 = 'world'
str3 = 'hello world'
def backward_string_by_word(w):
    rev = ""
    rev += w[::-1]
    return rev
if __name__ == '__main__':
    print(f"If you reverse '{str1}', the reversed string is '{backward_string_by_word(str1)}'.")
    print(f"If you reverse '{str2}', the reversed string is '{backward_string_by_word(str2)}'.")
    print(f"If you reverse '{str3}', the reversed string is '{backward_string_by_word(str3)}'.")
