# db_creation.py

import sqlite3

conn = sqlite3.connect("library.db")

cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE books
                  (title TEXT, author TEXT, release_date TEXT,
                   publisher TEXT, book_type TEXT)
               """)


# insert a record into the books table in the library database
cursor.execute("""INSERT INTO books
                  VALUES ('Python 101', 'Mike Driscoll', '9/01/2020',
                          'Mouse Vs Python', 'epub')"""
               )

# save data
conn.commit()

# insert multiple records using the more secure "?" method
books = [('Python Interviews', 'Mike Driscoll',
          '2/1/2018', 'Packt Publishing', 'softcover'),
         ('Automate the Boring Stuff with Python',
          'Al Sweigart', '', 'No Starch Press', 'PDF'),
         ('The Well-Grounded Python Developer',
          'Doug Farrell', '2020', 'Manning', 'Kindle')]
cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?)", books)
conn.commit()