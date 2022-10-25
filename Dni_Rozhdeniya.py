import random

def birthday(people_counter, iteration):
    days = [day for day in range(0, 29)]
    months = [month for month in range(0, 13)]

    count = 0
    count_not = 0

    for iterations in range(0, iteration+1):
        l1 = []
        l2 = []

        for i in range(0, people_counter+1):
            l1.append(random.choice(days))
            l2.append(random.choice(months))

        for i in range(0, people_counter):
            if l1.count(l1[i]) == 1 or l2.count(l2[i]) == 1:
                count_not += 1
                pass
            for j in range(0, people_counter):
                if j == i:
                    pass

                if l1[j] == l1[i] and l2[j] == l2[i]:
                    count += 1

    return f"количество совпадений: {count} \n" \
           f"количество промахов: {count_not} \n" \
           f"вероятность совпадения: {(count * 100) / (count_not + count)}"

print(birthday(24, 10000))