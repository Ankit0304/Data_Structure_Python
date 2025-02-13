class Book :
    def __init__(self,bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price
    
    def show(self):
        print(f'bookid: {self.bookid}, title: {self.title}, price: {self.price}')
    
bookid=input("Enter bookid: ")
title=input("Enter title: ")
price=float(input("Enter price: "))
b1 = Book(bookid, title, price)
b2=Book(101,"Harry Potter", 500)
b1.show()
b2.show()

   