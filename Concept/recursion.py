# assending order in recursion
def ass(n):
    # n = int(input("Enter A Number : "))
    if n == 0:
        return
    else:
        ass(n-1)
        print(n)
# ass(5)

# descending order in recursion 
def dec(n):
    if n == 0:
        return    
    else:
        print(n)
        dec(n-1)
# dec(5)

# printing things specific times
def prin(n):
    if n == 0:
        return
    else:
        prin(n-1)
        print("Printed Hardik",n,"times")
# prin(5)

# printing only even number
def even(n):
    if n == 0:
        return
    if n % 2 == 0:
        print(n)
    even(n-1)
# even(20)

# factorial of a number 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(5))

# sum of the number 
def nat(n):
    if n == 0:
        return 0
    else:
        return n + nat(n-1)
# print(nat(36))

# count number 
def cont(n):
    if n == 0:
        return 0
    else:
        return 1 + cont(n // 10)
# print(cont(9876))

def power(n,p):
    if p == 0 :
        return 1
    else:
        return n * power(n,p-1)
print(power(2,5))