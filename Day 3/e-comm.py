# You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:

# 1.Add a product to the cart.

# 2.Remove a product from the cart 

# 3.Search for a product in the cart 

# 4.Display all products in the cart

# 5.Show the total number of products in the cart
 
# Cart Operations:

# 1. Add Product

# 2. Remove Product

# 3. Search Product

# 4. Display Cart

# 5. Count Products

# 6. Exit
 
# Enter choice: 1

# Enter product to add: Laptop

# Product 'Laptop' added to cart.
 
# Enter choice: 1

# Enter product to add: Phone

# Product 'Phone' added to cart.
 
# Enter choice: 4

# Cart: ['Laptop', 'Phone']
 
# Enter choice: 3

# Enter product to search: Phone

# Yes, 'Phone' is in the cart.
 
# Enter choice: 5

# Total products in cart: 2

def e_commerce():
    l=[]
    print("***OPERATIONS***\n1.Add a product to the cart.\n2.Remove a product from the cart \n3.Search for a product in the cart \n4.Display all products in the cart\n5.Show the total number of products in the cart\n6.Sort the products in the cart\n7.Clear the cart\n8.Exit")
    while True:
        choice=int(input("Enter the operation you want to perform: "))
        match choice:
            case 1:l.append(input("Enter the product you want to add: "))
            case 2:
                x=input("Enter the product you want to remove: ")
                if x in l:
                    l.remove(x)
                else:
                    print("Product not found in the cart")
            case 3:
                x=input("Enter the product you want to search: ")
                if x in l:
                    print("Product is in the cart")
                else:
                    print("Product is not in the cart")
            case 4:
                if len(l)==0:
                    print("The cart is empty")
                    continue
                print("PRODUCTS IN THE CART ARE:")
                for i in l:
                    print(i)
            case 5:print("The total number of products in the cart is:",len(l))
            case 6:
                l.sort()
                print("The cart is sorted" )
            case 7:l.clear()
            case 8:
                print("Exiting the program")
                exit()
            case _:break
e_commerce()