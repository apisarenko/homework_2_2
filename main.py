import hashlib


def md5(path):
    with open(path, encoding='utf8') as file:
        while True:
            word = file.readline()
            if not word:
                exit(0)
            hash_word = hashlib.md5()
            hash_word.update(word.encode('utf8'))
            out = hash_word.hexdigest()
            yield out


gen = md5('file.txt')

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
