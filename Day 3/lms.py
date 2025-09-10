# You are building a Library Management System in Python. The system should store books in a dictionary where:
# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:
# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).
def library(f):
    print("***OPERATIONS***\n1.Add a book to the library (Book ID, Title).\n2.Remove a book using Book ID.\n3.Search for a book by Book ID and display the title.\n4.Update the title of a book (e.g., correction in title).\n5.Display all books in the library.\n6.Count the total number of books in the library.\n7.Check if a book title exists in the library (reverse lookup).\n8.Exit")
    while True:
        c=int(input("Enter the operation to be performed(integer): "))
        match c:
            case 1:f[int(input("Enter the book ID: "))]=input("Enter the book Title: ")
            case 2:
                if len(f)==0:
                    print("No data")
                else:
                    ix=int(input("Enter the book id to be deleted: "))
                    if ix in f:
                        del f[ix]
                    else:
                        print("Book ID not found")
            case 3:
                x=int(input("Enter the id of the book to be searched: "))
                if x in f:
                    print(f[x])
                else:
                    print("Not Found")
            case 4:
                k=int(input("Enter the id of the book to be updated: "))
                v=input("Enter the updated title: ")
                f[k]=v
            case 5:
                if len(f)==0:
                    print("No data")
                else:
                    for i in f:
                        print(i,':',f[i])
            case 6:print("Total number of books in the library: ",len(f))
            case 7:
                flag=0
                t=input("Enter the title of the book to be checked: ")
                for i in f:
                    if f[i]==t:
                        flag=1
                        break
                if flag==1:
                    print("Book exists")
                else:
                    print("Book does not exist")
            case _:break
f=dict()
library(f)