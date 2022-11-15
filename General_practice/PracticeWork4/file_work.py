import string
def read_file():
    with open('read_file.txt', 'r') as rf:
        ''' 
         translate() в Python возвращает новую строку, в 
         которой каждый символ в строке заменяется с использованием данной таблицы перевода. 

         maketrans(intab, outtab) -> создаем таблицу перевода, 
         intab — Это строка, имеющая переводимые символы. 
         outtab — Это строка, имеющая перевод intab символов. 
         Т.е intab - это симвов, outtab - перевод 
         '''
        string = str.maketrans('''!()-[]{};?@#$%:'"\,./^&amp;*_''', '                             ')
        read_f = rf.read().lower().translate(string).split()
        return [i + '\n' for i in read_f]

def write_file(count, inp):
    with open('outread_file.txt', 'w') as wf:
        wf.write(f'Количество уникальных слов: {str(count)}\n===============================\n')
        wf.writelines(inp)

inputs = sorted(set(read_file()))
counts = len(inputs)
write_file(counts, inputs)