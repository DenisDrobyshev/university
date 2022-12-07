list = []
list_files = []
for i in range(0, int(input())):
    answer = input()
    list.append(answer)
    list_files.append(answer.split(' ')[0])

for i in range(0, int(input())):
    operations, filename = input().split()
    operations = operations.upper()
    if operations == 'EXECUTE' or operations == 'WRITE' or operations == 'READ':
        operations = operations[0]
        flag = 0
        for data in list:
            if data.count(filename) and data.count(operations):
                flag = 1
        if flag == 1:
            print('OK')
        else:
            print('Denied')
