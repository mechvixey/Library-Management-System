class Library():
    def __init__(self,file):
        self.booksFile = open(file,"a+")
        
    def __del__(self):
        self.booksFile.close()

    def listBooks(self):
        #books.txt convert to a list 
        self.booksFile.seek(0)
        books = self.booksFile.readlines()
        print("**********************\n        Library")
        for i in books:
            print(i,end="")
    def addBooks(self):
        #get infos about book and write to books.txt

        title=input("Book Title: ")
        author=input("Book Author: ")
        firstRelease=input("First Release: ")        
        pages=input("Pages: ")
        
        book = title+","+author+","+firstRelease+","+pages+"\n"
        
        self.booksFile.write(book)
    def removeBooks(self):
        
        title = input("Title of the book that you want to delete: ")
        self.booksFile.seek(0)  # go to top of books.txt
        books = self.booksFile.readlines()#get books
        listedBooks = []
        for i in books:
            if not i.startswith(title):
                listedBooks.append(i)
        self.booksFile.seek(0)
        self.booksFile.truncate()  # clean the first book
        self.booksFile.writelines(listedBooks) #write the list which the book that user want to remove  is deleted 
lib = Library("books.txt")
while True:
    #Ask the operation until user wants to quit
    print('''
**************************
***MENU***
1)List Books
2)Add Books
3)Remove Books  
Press any key to exit          
''')
    choice = input("What is your choice: ")
    if choice=="1":
        lib.listBooks()
    elif choice=="2":
        lib.addBooks()
    elif choice=="3":
        lib.removeBooks()
    else:
        break
