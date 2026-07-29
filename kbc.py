k = "WELCOME TO KBC"
fin = k.center(50, "*")
print(fin)

questions = [
    ["What is the capital of India?",
     "A. Mumbai",
     "B. New Delhi",
     "C. Chennai",
     "D. Kolkata",
     "B"],

     ["Which planet is known as the Red Planet?",
      "A. Earth",
      "B. Mars",
      "C. Jupiter",
      "D. Venus",
      "B"],

     ["Who is known as the Father of the Nation in India?",
      "A. Jawaharlal Nehru", 
      "B. Sardar Patel", 
      "C. Mahatma Gandhi", 
      "D. Bhagat Singh",
      "C"],

      ["How many players are there in a cricket team?",
       "A. 9", 
       "B. 10", 
       "C. 11", 
       "D. 12",
       "C"],
]

price = [700,1000,2000,5000]
amt = 0 

for i in range(len(questions)):
    print()
    print("Questions : ",i+1)
    print("Amount : ",price[i])

    print(questions[i][0])
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])

    answer = input("Enter Your Answer : ")
    answer  = answer.upper()

    if answer != questions[i][5]:
        print("Sorry Baby Yor'e out ")
        break

    if answer == questions[i][5]:
        print("Congratulations!!!!")
    else:
        print("Sorry You Are Out")

    if answer == questions[i][5]:
        amt = price[i]

print("\n\n Thanks For Playing With Us")
print("Amount Your'e Taking Home",amt)