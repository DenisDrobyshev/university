import random
day = 365

def birthday(iter, count):

    paradoxed = 0
    ok = 0

    for _ in range(iter):
        birthdays = [random.randint(1, day) for _ in range(count)]
        uniq = set(birthdays)
        if len(birthdays) != len(uniq):
            paradoxed += 1
        else:
            ok += 1


    return  f"""Всего итераций: {iter}
Парадокс произошел в: {paradoxed/iter * 100}%"""

print(birthday(100000, 23))