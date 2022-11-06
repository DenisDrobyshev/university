stroka = input()
x = stroka.find(' ')
print(stroka[x+1:] + stroka[x] + stroka[:x])