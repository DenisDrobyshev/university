import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

gener = int(input('Количество паролей для генерации: '))
len_pass = int(input('Длина пароля: '))
digit = input('Включать ли цифры? (y/n) ').strip()
ABC = input('Включать ли прописные буквы? (y/n) ').strip()
abc = input('Включать ли строчные буквы? (y/n) ').strip()
simvol = input('Включать ли символы? (y/n) ').strip()
not_simv = input('Исключать ли неоднозначные символы? (y/n) ').strip()

if digit.lower() == 'y':
    chars += digits
if ABC .lower() == 'y':
    chars += uppercase_letters
if abc.lower() == 'y':
    chars += lowercase_letters
if simvol.lower() == 'y':
    chars += punctuation
if not_simv.lower() == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(len_pass, chars):
    password = ''
    for j in range(len_pass):
        password += random.choice(chars)
    return password
for _ in range(gener):
    print(f'{generate_password(len_pass, chars)}, \n')


