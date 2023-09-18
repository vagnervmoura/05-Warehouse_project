# ACCOUNT AND A WAREHOUSE PROJECT
# In this exercise, you are tasked to write a Python program that simulates operations on a company's account and a warehouse. 
# The program should handle various commands for performing operations like:
# adding/subtracting balance, recording sales and purchases, displaying account balance, showing warehouse status, and reviewing recorded operations.
option = None
balance = 0

def goto(linenum):
    global line
    line = linenum

def balance_1(): # The program will prompt for an amount to add or subtract from the account.
    global balance
    try:
        action = int(input("Press '1' to Add or press '2' to Subtract: "))
        print(action == 1)
        if action == 1:
            value = float(input("1 - Insert the value to add to your balance: "))
            balance += value
            print("Your new balance is: {}".format(balance))
        elif action == 2:
            value = float(input("2 - Insert the value to subtract from your balance:"))
            if value < balance:
                balance -= value
                print("Your new balance is: {}".format(balance))
            else:
                print("Sorry, you do not have balance enough to do this withdraw.")
    except ValueError:
        print("Sorry.\n")
    

while option != 0:
    option = int(input("\n\nSelect one of the following options:\n1 - balance\n2 - sale\n3 - purchase\n4 - account\n5 - list\n6 - warehouse\n7 - review\n0 - end\n\n"))

    try:
        if option == 0:
            print("\nThank you for using our system.\n\n")
            exit()
            
        elif option == 1: # Option to balance
            print("You choose the Option {} to check the Balance.".format(option))
            balance_1()
            
            
        elif option == 2: # Option to sale
            print("You choose the Option {} to check the sale.".format(option))
            
            
        elif option == 3: # Option to purchase
            print("You choose the Option {} to check the purchase.".format(option))
             
                 
        elif option == 4: # Option to account
            print("You choose the Option {} to check the account.".format(option))
            
            
        elif option == 5: # Option to list
            print("You choose the Option {} to check the list.".format(option))
            
            
        elif option == 6: # Option to warehouse
            print("You choose the Option {} to check the warehouse.".format(option))
            
            
        elif option == 7: # Option to review
            print("You choose the Option {} to check the review.".format(option))
             
                
    except ValueError:
        print("Sorry, but you have input a wrong option, please let's try again with an valid option number.\n")
        
