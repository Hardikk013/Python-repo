# def name(nm):
#     print("Your Name Is : ",nm)
# name("Hardik")

# def lp():
#     uinp = int(input("Enter a number: "))
#     for i in range(1, uinp + 1):
#         print(i)

# lp()

def sum_of_two():
    '''Hii this is function document feature'''
    print(sum_of_two.__doc__)
    ainp = int(input("Enter The First Value : "))
    binp = int(input("Enter The Second Value : "))
    c = ainp + binp
    print("Value After Adding Both Values : ",c)

sum_of_two()

# sum_of_two()

# def sq_nm(a):
#     print("Square Of Your Number",a,"Is",a*a)

# sq_nm(10)

# def ev_od():
#     num = int(input("Enter Your Number Even/Odd : "))
#     if num % 2 == 0:
#         print(num,"Is An Even Number")
#     else:
#         print(num,"Is An Odd Number")

# ev_od()

# def mul(a):
#     print("The Multiplication Table Of",a)
#     for i in range(1,10+1):
#         print(a,"x",i,"=",i*a)
# mul(5)        