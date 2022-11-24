ls = input().split(' ')
stroka = ''

for word in ls:
    print(stroka.count(word))
    stroka += word