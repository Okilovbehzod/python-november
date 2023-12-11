
class Book:
    def __init__(self, title, author,year):
        self.title = title
        self.author = author
        self.year=year

    def get_info(self):
        
        print(f"Title: {self.title}\n Author: {self.author}\n Year: {self.year}")

n = "Avdonin"
a = "1984"
b = "Krilov"

na = "Geologist"
aa = "1954"
ba = "Andrey"

p1 = Book(n, a, b)
p1.get_info()

p2 = Book(na, aa,ba)
p2.get_info()