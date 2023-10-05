from Book import Book
from Catalog import Catalog

b1 = Book("The Psychology of Money", "Morgan Housel","Private", "2016", "Personal Finance", 250, 5000)
b2 = Book("The Intelligent Investor", "Benjamin","Private", "2000", "Personal Finance", 200, 2000)

b3 = Book("The Candlesticks", "Benjamin","Private", "2010", "Personal Finance", 100, 1000)

b4 = Book("Atomic Habits", "James Clear","Private", "2020", "Productivity", 250, 10000)
b5 = Book("The 5AM Club", "Robin Sharma","Private", "2016", "Productivity", 250, 7000)

c1 = Catalog("Catalog 1")
c1.addBook(b1)
c1.addBook(b2)
c1.addBook(b3)
c1.addBook(b4)
c1.addBook(b5)

print(c1.getBooks())

print(c1.getTopBooksByAuthor("James Clear",2))

print(c1.getTopBooksByCategory("Personal Finance",2))

print(c1.searchBookByAuthor("Personal Finance"))

print(c1.searchBookByName("Atomic Habits"))

print(c1.getTopBooksByCategory("Productivity",2))

