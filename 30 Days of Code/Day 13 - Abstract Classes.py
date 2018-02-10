class MyBook(Book) :
    def __init__(self, title, author, price) :
        self.title = title
        self.price = price
        self.author = author

    def display(self) :
        print("Title: ", self.title, sep = '')
        print("Author: ", self.author, sep = '')
        print("Price: ", self.price, sep = '')
