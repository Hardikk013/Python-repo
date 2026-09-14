#this is being created with the help of file io in python

title = "Student Record Manager"
print(title.title().center(50,"="))

choice = ""
while choice != "3":
    choice = input("1.Add student\n2.View Student\n3.Exit\n\nEnter Your Choice : ")


    match choice :
        case "1" | "Add":
            print("Enter Student Information\n")

            stud_id = input("Enter ID : ")
            stud_name = input("Enter Name : ")
            stud_age = input("Enter Age : ")
            stud_course= input("Enter Course : ")
            stud_marks = input("Enter Marks : ")

            student = stud_id + "|" + stud_name + "|" + stud_age + "|" + stud_course + "|" + stud_marks 

            with open("student_record.txt" , "a") as add_data:
                add_data.write(student + "\n")

            print("Data Added Successfully.......\n")

        case "2" | "View":
            view_data = open("student_record.txt" , "r")
            read_data = view_data.read()
            print("\n" + read_data)
            view_data.close()
        
            print("Data Retrived Successfully.......\n")

        case "3" | "exit" | "Exit":
            print("Exiting......")
            break

        case _:
            print("Invalid Choice !!")