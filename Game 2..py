import random

vin1 = 0
vin2 = 0

for i in range(0, 10000):
    door = [0, 1, 0]
    doors = random.choice(door)
    door.remove(doors)
    door.remove(0)
    if doors == 1:
        vin1 += 1
    elif door[0] == 1:
        vin2 += 1

print(f'Процент выигрыша при своем изначальном выборе {vin1 // 100}%')
print(f'Процент выигрыша при своем измененном выборе {vin2 // 100}%')








# import random
#
# result_change = []
# result_static = []
#
# times = 0
# while times <= 10000:
#     door = [0, 0, 1]
#     if random.choice(door) == 0:
#         door.remove(0)
#         if random.choice(door) == 1:
#             result_change.append(1)
#         else:
#             result_static.append(0)
#         times += 1
#     elif random.choice(door) == 1:
#         door.remove(0)
#         if random.choice(door) == 1:
#             result_change.append(0)
#         else:
#             result_static.append(1)
#         times += 1
#
# sumi_static = len(result_static)
# sumi_change = len(result_change)
#
# print(result_static.count(1) / sumi_static)
# print(result_change.count(1) / sumi_change)







