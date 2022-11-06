index = int(input("Позиция числа: ")) - 1

fib = [0, 1]
while index != 0:
    fib[0], fib[1] = fib[1], fib[1] + fib[0]
    index -= 1

print(fib[1])