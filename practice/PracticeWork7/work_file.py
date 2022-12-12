import csv


def get_books(name: str) -> list:
    lst = []
    with open('books.csv', 'r') as file:
        read = csv.reader(file, delimiter='|')
        for i in read:
            if name.lower() in i[1].lower():
                lst.append(i)
    return lst


def get_totals(books: list) -> list:
    lst = []
    for book in books:
        quantity_price = float(book[3]) * float(book[4])
        if quantity_price < 500:
            quantity_price += 100
        lst.append((book[0], str(quantity_price)))
    return lst


print(get_books('java'))
print(get_totals(get_books('java')))
