menu = input("Enter The Item Name You Want To Order :\nPizza\nBurger\nPasta\n\nEnter Your Choice : ").lower()
match menu:
    case "pizza":
        print("""Item Name : Pizza
                 Price     : ₹250
                 Thank you for ordering!""")
        
    case "burger":
        print("""Item Name : Burger
                 Price     : ₹180
                 Thank you for ordering!""")
        
    case "pasta":
         print("""Item Name : Pasta
                 Price     : ₹220
                 Thank you for ordering!""")
         
    case _:
        print("Invalid Choice")