import time 
print("hello")
# time.sleep(3)
print("Welcome")

print("Current Year : ",time.strftime("%Y"))
print("Current Month (Month No/Month Name) : ",time.strftime("%m,%B"))
print("Day Name : ",time.strftime("%A"))
print("Current Time : ",time.strftime("%T"))

hour = int(time.strftime("%H"))

if(hour>=5 and hour<=11):
    print("Good Morning Sir")

elif(hour>=12 and hour<=17):
    print("Good Afternoon Sir")

elif(hour>=18 and hour<=21):
    print("Good Evening Sir")

else:
    print("Soo Jaa ")