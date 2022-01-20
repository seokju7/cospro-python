def soluton(sentence):
    word = ''
    for c in sentence:
        if c != ' ' and c != '.':
            word += c
    size = len(word)
    for i in range(size // 2):
        if word[i] != word[size - (1 + i)]:
            return False
    return True


print(soluton(''))