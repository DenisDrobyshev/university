dictionary = {}

for i in range(0, int(input())):
    for words in input().split(' '):
        dictionary[words] = dictionary.get(words, 0) + 1

for i in sorted(dictionary, key=dictionary.get, reverse=True):
    print(i, dictionary[i])
