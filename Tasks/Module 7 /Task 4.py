words_list = []
number_of_lines = int(input())
for i in range(0, number_of_lines):
    s = input().split(' ')
    for j in s:
        words_list.append(j)
words_list = sorted(words_list)

max: int = 0
answer = ''
for word in words_list:
    if words_list.count(word) > max:
        answer = word
        max = words_list.count(word)
print(answer)