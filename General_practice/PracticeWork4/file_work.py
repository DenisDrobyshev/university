def read_file():
    with open('read_file.txt', mode='r') as file1:
        lists = [i.lower() + '\n' for i in file1.read().split()]
        return lists

def write_file(i, l):
    with open('outread_file.txt', mode='w') as file2:
        file2.write(f'Количество уникальных слов: ')
        file2.write(str(i) + '\n')
        file2.writelines(l)


inputs = sorted(set(read_file()))
lens = len(inputs)
write_file(lens, inputs)