from random import randint
acc = {}
def create_account():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    pin = int(input("Set a pin: "))
    amount = int(input("Enter amount: "))
    acc_num = randint(9**9,10**10)
    acc.update({acc_num:[f_name,l_name,amount,pin]})
    print(f"""
          Account No: {acc_num}
          Firat Name: {f_name}
          Last Name: {l_name}
          Amount: {amount}
          """)
    choice()
    
def deposite_amount():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    acc_num = int(input("Enter Account number: "))
    if acc_num in acc and acc[acc_num][0] == f_name and acc[acc_num][1] == l_name:
        new_amount = int(input("Enter amount: "))
        acc[acc_num][2] += new_amount
        print(f"""
          Account No: {acc_num}
          Firat Name: {f_name}
          Last Name: {l_name}
          Amount: {acc[acc_num][2]}
          """)
        choice()
    else:
        print("Account not found")
        choice()

def withdraw_amount():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    acc_num = int(input("Enter Account number: "))
    pin = int(input("Enter the pin: "))
    if acc[acc_num][0] == f_name and acc[acc_num][1] == l_name and acc[acc_num][3] == pin:
        new_amount = int(input("Enter amount: "))
        if acc[acc_num][2] < new_amount:
            print("Insufficiant Balance")
        else:
            acc[acc_num][2] -= new_amount
        print(f"""
            Account No: {acc_num}
            Firat Name: {f_name}
            Last Name: {l_name}
            Amount: {acc[acc_num][2]}
            """)
        choice()
    elif acc[acc_num][3] != pin:
        print("Incorrect pin")
        choice()
    else:
        print("Account not found")
        choice()
        
def delete_account():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    acc_num = int(input("Enter Account number: "))
    if acc_num in acc and acc[acc_num][0] == f_name and acc[acc_num][1] == l_name:
        acc.pop(acc_num)
        print("Account deleted successfully")
        choice()
    else:
        print("Account not found")
        choice()

def choice():
    print("===========Options to select===========")
    user = int(input('1.Create Account 2.Deposit Amount 3.Withdraw Amount 4.Delete Account: '))
    if user == 1:
        create_account()
    elif user == 2:
        deposite_amount()
    elif user == 3:
        withdraw_amount()
    elif user == 4:
        delete_account()
    else:
        print("Sorry")


print("========Welcome to National Bank========")
print("What would you like to do")
choice()

