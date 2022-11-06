stroka = input()
if stroka.count('f') == 1:
    print(stroka.find('f'))
elif stroka.count('f') >= 2:
    print(stroka.find('f'), stroka.rfind('f'))