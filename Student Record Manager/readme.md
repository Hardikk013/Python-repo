# Student Record Manager

A simple command-line **Student Record Manager** built with Python to practice **File I/O, loops, match-case, and basic file handling**.

## 📌 About the Project

This project allows users to add student information and view previously stored student records.

Student records are stored permanently in a text file using Python's built-in file handling functionality.

## ✨ Features

* Add a new student record
* View all stored student records
* Store records permanently in a `.txt` file
* Menu-driven command-line interface
* Supports multiple student records
* Exit the application from the menu
* Handles invalid menu choices

## 🛠️ Technologies Used

* **Python 3**
* Python File I/O
* `while` loop
* `match-case`
* `with open()`
* String manipulation

## 📂 Project Structure

```text
student-record-manager/
│
├── student_record_manager.py
├── student_record.txt
└── README.md
```

## 💾 Data Storage

Student records are stored in `student_record.txt`.

Each student is stored on a separate line using `|` as a separator.

Example:

```text
101|Hardik|20|BCA|85
102|Rahul|21|BCA|78
```

The format is:

```text
Student ID | Name | Age | Course | Marks
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project

```bash
cd student-record-manager
```

### 3. Run the program

```bash
python student_record_manager.py
```

## 🖥️ Example

```text
========================================
        Student Record Manager
========================================

1.Add student
2.View Student
3.Exit

Enter Your Choice : 1

Enter Student Information

Enter ID : 101
Enter Name : Hardik
Enter Age : 20
Enter Course : BCA
Enter Marks : 85

Data Added Successfully.......
```

Viewing the records:

```text
1.Add student
2.View Student
3.Exit

Enter Your Choice : 2

101|Hardik|20|BCA|85

Data Retrieved Successfully.......
```

## 📚 What I Learned

While building this project, I practiced:

* Opening files using `open()`
* Reading data from files
* Appending data to files
* Writing data using `write()`
* Using `with open()` for safer file handling
* Using loops to create a menu-driven application
* Using `match-case` for menu options
* Storing structured data in a text file

## 🚀 Future Improvements

Planned improvements for future versions:

* [ ] Search student by ID
* [ ] Delete a student record
* [ ] Update student information
* [ ] Validate student input
* [ ] Improve record formatting
* [ ] Add better exception handling
* [ ] Store records using JSON
* [ ] Eventually migrate to SQLite

## 👨‍💻 Author

**Hardik**

This project was created as part of my journey to improve my Python programming and problem-solving skills.
