y, x = map(int, [input(f"Число {i+1}: ") for i in range(2)])

print("Белая" if (x + y) % 2 else "Черная")