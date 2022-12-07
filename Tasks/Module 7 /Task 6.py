g = {}
for i in range(0, int(input())):
    cities = input().split()
    for city in cities[1:]:
        g[city] = cities[0]

cities_list = []
for i in range(0, int(input())):
    cities_list.append(g.get(input()))

for i in cities_list:
    print(i)
