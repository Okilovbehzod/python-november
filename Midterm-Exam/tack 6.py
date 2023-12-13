
class Book:
    def __init__(self, title, author,year):        #Mo avval function vorid mekunem
        self.title = title                        #Nomi kitob 
        self.author = author                      #Navisandai kitob
        self.year=year                            #Soli barorish

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