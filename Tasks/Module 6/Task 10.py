string = input("Строка: ")

print(string[:string.find("h")], string[string.rfind("h") + 1:], sep="")