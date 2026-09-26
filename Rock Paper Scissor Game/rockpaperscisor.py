import random
import time

usr_points = 0
comp_points = 0

start_message = " Welcome To The Game "
print(start_message.title().center(50, "="))

#Functions
def usr_choice_confi ():
    if usr_choice == 1:
       return "Rock"
    elif usr_choice == 2:
        return "Paper"
    else:
        return "Scissor"

def cmp_choice_confi():
    if computer_choice == 1:
        return "Rock"
    elif computer_choice == 2:
        return "Paper"
    else:
        return "Scissor"

def point_calculation():
    global usr_points, comp_points

    if usr_choice == computer_choice:
        print("\n" + "-" * 40)
        print("              It's An Draw")
        print("-" * 40 + "\n")
    elif (usr_choice == 1 and computer_choice == 3) or (usr_choice == 2 and computer_choice == 1) or (usr_choice == 3 and computer_choice == 2):
        print("\n" + "-" * 40)
        print("                You Won")
        print("-" * 40 + "\n")
        usr_points += 1
    else:
        print("\n" + "-" * 40)
        print("            Computer Wins !")
        print("-" * 40 + "\n")
        comp_points +=1

def show_result():
    if  usr_points>comp_points:
        print("🏆 Congratulations! You won")
    elif comp_points > usr_points:
        print("😢 The computer won the tournament!")
    else:
        print("👔 Overall tournament tie!")

for round_no in range(1,4):
    print("\n" + "=" * 50)
    print(f"                    ROUND {round_no}")
    print("=" * 50)

    try:
        usr_choice = int(input(
            "\nSelect An Action\n"
            "-----------------\n"
            "1. Rock\n"
            "2. Paper\n"
            "3. Scissor\n"
            "-----------------\n"
            "Enter Your Choice : "
        ))
    except ValueError:
        print("\nPlease Enter A Valid Number !")
        print("Skipping This Round.......\n")
        continue

    print("\n" + "-" * 40)
    print("You Choosed     : " + str(usr_choice_confi()))

    computer_choice = random.choice([1, 2, 3])

    print("Computer Is Choosing...........")
    time.sleep(4)

    print("\nComputer Choosed : " + str(cmp_choice_confi()))

    print("\n" + "-" * 40)
    print("        " + str(usr_choice_confi()) + "  Vs  " + str(cmp_choice_confi()))
    print("-" * 40)

    point_calculation()

print("\n" + "=" * 50)
msg = "FINAL SCORE"
print(msg.center(50))
print("=" * 50)

print(f"\nYour Score       : {usr_points}")
print(f"Computer's Score : {comp_points}")

print("\n" + "-" * 50)
show_result()
print("-" * 50)