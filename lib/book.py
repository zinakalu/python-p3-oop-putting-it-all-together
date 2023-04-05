#!/usr/bin/env python3

class Book:
   
   def __init__(self, title, page_count = 0):
      self.title = title
    #   self.author = author
      self.page_count = page_count
    #   self.genre = genre

   def get_page_count(self):
      return self._page_count
   
   def set_page_count(self, page_count):
      if not isinstance(page_count,int):
         print("page_count must be an integer")
      else:
         self._page_count = page_count

   page_count = property(get_page_count, set_page_count)

   #create page_count attribute and use property() to give page_count 
   # the powers/abilities of the get or set methods depending on the context
   #self.page-count will run the result of get_page_count()
   #self.page_count = something will run the result of set_page_count()
    #   else:
    #      self._page_count = page_count
   
   def turn_page(self):
        print ("Flipping the page...wow, you read fast!")


new_book = Book("title of book", "566") 
new_book