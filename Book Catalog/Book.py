class Book:
    def __init__(self, name, author, publisher, publishingYear, category, price, copiesSold):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publishingYear = publishingYear
        self.category = category
        self.price = price
        self.copiesSold = copiesSold

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getAuthor(self):
        return self.author

    def setAuthor(self, value):
        self.author = value

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, value):
        self.publisher = value

    def getPublishingYear(self):
        return self.publishingYear

    def setPublishingYear(self, value):
        self.publishingYear = value

    def getCategory(self):
        return self.category

    def setCategory(self, value):
        self.category = value

    def getPrice(self):
        return self.price

    def setPrice(self, value):
        self.price = value

    def getCopiesSold(self):
        return self.copiesSold

    def setCopiesSold(self, value):
        self.copiesSold = value

