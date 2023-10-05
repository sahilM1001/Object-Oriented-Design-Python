class Catalog:
    def __init__(self,name):
        self.books = []
        self.name = name

    def addBook(self,book):
        self.books.append(book)

    def getName(self):
        return self.name
    
    def getBooks(self):
        return self.books
    
    def getTopBooksByAuthor(self, author, limit):
        filteredArr = []
        for i in self.books:
            if i.getAuthor() == author:
                filteredArr.append(
                    {
                        "Book Title": i.getName(),
                        "Author": i.getAuthor(),
                        "Copies Sold": i.getCopiesSold(),
                        "Price": i.getPrice()
                    }
                )

        filteredArr.sort(key=lambda x: x["Price"], reverse=True)

        if len(filteredArr) > limit:
            return filteredArr[:limit]
        else:
            return filteredArr
    def getTopBooksByCategory(self, category, limit):
        filteredArr = []
        for i in self.books:
            if i.getCategory() == category:
                
                filteredArr.append(
                    {
                        "Book Title": i.getName(),
                        "Author": i.getAuthor(),
                        "Copies Sold": i.getCopiesSold(),
                        "Price": i.getPrice()
                    }
                )
        
        filteredArr.sort(key=lambda x: x["Price"], reverse=True)
        
        if len(filteredArr) > limit:
            return filteredArr[:limit]
        else:
            return filteredArr
        
    def searchBookByName(self, bookName):
        flag = False
        for i in self.books:
            if i.getName() == bookName:
                flag = True
                {
                        "Book Title": i.getName(),
                        "Author": i.getAuthor(),
                        "Copies Sold": i.getCopiesSold(),
                        "Price": i.getPrice()
                }
                return i
        if flag == False:
            print("No book with name: ", bookName, " found in the catalog.")

    def searchBookByAuthor(self, author):
        flag = False
        for i in self.books:
            if i.getAuthor() == author:
                flag = True
                return i
        if flag == False:
            print("No author with name: ", author, " found in the catalog.")