# pr = "Division Calculator"
# nw = pr.center(50,"=")
# print(nw)


# try:
#     a = float(input("\nEnter The Value Of A : "))
#     b = float(input("Enter The Value Of B : "))
#     div = (a/b)
#     print(f"\nResult = {div:.3f}")

# except ZeroDivisionError:
#     print("Cannot Divide By Zero !")

# except ValueError:
#     print("Invalid Value Provided !!")

# problem 2 
# try:
#     inp = int(input("Enter A Number : "))

# except ValueError:
#     print("Please Enter A Valid Integer!!")

# else:
#     print(f"You Entered {inp}")


# problem 3
# try:
#     fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
#     inp = int(input("Enter Index : "))
#     print(fruits[inp])

# except IndexError:
#     print("Sorry You Entered Wrong Index")

# except ValueError:
#     print("Wrong Value Format")

# using finally keyword 
# def divide():
#     try:
#         return "Success"

#     finally:
#         print("Cleaning up...")

# print(divide())
try:
    fruits = ["Apple", "Banana", "Mango", "Orange"]
    k = int(input("Enter A Index To Redirect : "))
    print(fruits[k])

except IndexError:
    print("Invalid Error")

except ValueError:
    print("Please enter a number")

finally:
    print("Program Finished")