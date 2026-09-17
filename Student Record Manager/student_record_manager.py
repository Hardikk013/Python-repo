#this is being created with the help of file io in python

title = "Student Record Manager"
print(title.title().center(50,"="))

choice = ""
while choice != "3":
    choice = input("1.Add student\n2.View Student\n3.Search Student By ID\n5.Exit\nEnter Your Choice : ")


    match choice :
        case "1" | "Add" | "add":
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

        case "3" | "search" | "Search":
            search_id = input("Enter A Student ID : ")

            with open("student_record.txt" , "r") as file:
                for n,line in enumerate(file,start=1):

                    student_sorted = line.strip().split("|")

                    if search_id in line:
                        print("Record Found".center(30,"*"))
                        print("\nFound At Line No : " + str(n))
                        print("Student Id         : " + student_sorted[0])
                        print("Student Name       : " + student_sorted[1])
                        print("Student Age        : " + student_sorted[2])
                        print("Student Course     : " + student_sorted[3])
                        print("Student Marks      : " + student_sorted[4])
                        break
                else:
                        print("Record Not Found")
                                        

        case "5" | "exit" | "Exit":
            print("Exiting......")
            break

        case _:
            print("Invalid Choice !!")
