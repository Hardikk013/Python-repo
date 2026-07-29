class InsufficeintBalanceError(Exception):
    pass

try:

    ac_bal = float(input("Enter Your Account Balance : "))

    wth_amt = float(input("Enter The Withdrawal Amount : "))

    remaining_bal = (ac_bal-wth_amt)

    if wth_amt>ac_bal:
        raise InsufficeintBalanceError("\nInsufficient balance! Withdrawal denied.")
    else:
        print(f"\nWithdrawal successful.\nRemaining Balance :- {remaining_bal}")

except ValueError:
    print("Please Enter Value Only In Number ")

except InsufficeintBalanceError as e:
    print(e)

finally:
    print("Transaction Completed")