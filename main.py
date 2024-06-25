books =[]

for i in range(3):
  book = dict()
  book["Title"] = input("Enter book title: ")
  book["Author"] = input("Enter author name: ")
  books.append(book)

for book in books:
  print(book)