heading = "GST CALCULATOR MENU"
f = heading.center(40, "=")
print(f)

menu = int(input("1. Food (5%)\n2. Clothes (12%)\n3. Electronics (18%)\n4. Luxury Items (28%)\n5. Exit\n\nEnter Choice In number : "))

def gst_cal(pri, gst):
    return (pri * gst) / 100

if menu == 5:
    print("Exiting...........")

else:
    pri = float(input("Enter the product price : "))

    match menu:
        case 1:
            category = "Food"
            gst = 5
            final = gst_cal(pri, gst)

        case 2:
            category = "Clothes"
            gst = 12
            final = gst_cal(pri, gst)

        case 3:
            category = "Electronics"
            gst = 18
            final = gst_cal(pri, gst)

        case 4:
            category = "Luxury Item"
            gst = 28
            final = gst_cal(pri, gst)

        case _:
            print("Invalid Choice Try Again !!!")
            exit()   

    gc = "FINAL GST CALCULATOR"
    h = gc.center(40, "=")
    print(h)

    print("Category     :", category)
    print("Price        : ₹", pri)
    print("GST Rate     :", gst, "%")
    print("GST Amount   : ₹", final)

    print("-" * 40)

    print("Total Price  : ₹", pri + final,"\n\n")