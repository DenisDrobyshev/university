string = input("Строка: ")

print(string[: string.find("h") + 1],
      string[string.find("h") + 1 : string.rfind("h")][::-1],
      string[string.rfind("h") :],
      sep="",)