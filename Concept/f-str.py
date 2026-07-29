# sen = "Hii {} Welcome To The Best University {} In The World"
# name = "Hardik"
# uni = "Uka Tarsadia University"

# print(sen.format(name,uni))

for i in range(9):
    print(f"This is iteration {i+1}")
else:
    print("Loop Is Over")

for i in range(6):
    print("this is {} iteration".format(i+1))
else:
    print("See you")


# n1 = "Hii this is {nm} language and you are now {level}"
# nm = "Python"
# level = "Intermediate"

# print(f"Hii this is {nm} language and you are now {level}")

# name = "Hardik"
# age = 19
# city = "Navsari"

# print(f"My name is {name}\nI am {age} years old\nI live in {city}")

# n1 = 4
# n2 = 2
# print(f"{n1} + {n2} = {n1 + n2}")

# area of rectangle
# length = float(input("Enter The Length Of Rectangle : "))
# width = float(input("Enter The Width Of Rectangle : "))
# print(f"Length Of Rectangle = {length}\nWidth Of Rectangle = {width}\nArea Of Rectangle = {length*width}")

# student results
# name = "Hardik"
# marks = 87
# print(f"{name} scored {marks} marks.")

#  shopping bill
# item = "Amul Gold"
# price = 35
# quantity = 3
# print(f"Item : {item}\nPrice : {price}\nQuantity : {quantity}\nTotal : ₹{price*quantity}")

# temp cel to fer
# celsius = float(input("Enter Temperature In Celsius : "))
# print(f"{celsius}°C = {celsius * (9/5) + 32}°F")

# format decimal 
# pi = 3.141592653
# print(f"Pi ({pi}) = {pi:.2f}")

# bmi calcu using f strings 
# weight = float(input("Enter Your Weight : "))
# height = float(input("Enter Your Height(IN Centimeters only): "))
# print(f"BMI = ({weight / (height * height ) * 10000:.2f})")

# table 
# tbl = int(input("Enter A Value For Printing Table : "))
# for i in range(1,11):
#     print(f"{tbl} x {i} = {tbl*i}")

# num = int(input("Enter A Number : "))
# if (num % 2 == 0):
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number")

# a = float(input("Enter The First Number : "))
# b = float(input("Enter The Second Number : "))
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")

# report card
# nm = input("Enter Your Name : ")
# pm = float(input("Enter Your Physics Marks : "))
# cm = float(input("Enter Your Chemistry Marks : "))
# mm = float(input("Enter Your Maths Marks : "))
# print(f"Student Name : {nm}\nPhysics : {pm}\nChemistry : {cm}\nMaths : {mm}\nTotal : {(pm+cm+mm)}\nAverage : {(pm+cm+mm) / 3}")