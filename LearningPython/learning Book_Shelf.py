# -*- coding: utf-8 -*-

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def get_info(self):
        return f"{self.title} by {self.author}"        
        
class Bookshelf:
    def __init__(self):
        self.books=[]
        
    def add_book(self,book):
        self.books.append(book) #append book instance into bookshelf
    
    def remove_book_by_title(self,title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} is removed")
                return
        print("could not find the book")
                
    def find_by_author(self,author):
        found = False
        for book in self.books:
            if author == book.author:
                found = True
                print(f"{book.title} by {book.author}")
        if not found:
            print("cound not find the author's book")
    
    def list_books(self):
        for book in self.books:
            print(book.get_info())
            
        
book1 = Book("Sea", "Hemingway")
book2 = Book("1984", "George Orwell")
book3 = Book("Old Man", "Hemingway")

shelf = Bookshelf()
shelf.add_book(book1)
shelf.add_book(book2)
shelf.add_book(book3)

shelf.list_books()
print("----- 削除 -----")
shelf.remove_book_by_title("1984")
shelf.list_books()
print("----- 検索（Hemingway） -----")
shelf.find_by_author("Hemingway")
print("----- 検索（Tolkien） -----")
shelf.find_by_author("Tolkien")