# ACCOUNT AND A WAREHOUSE PROJECT
# In this exercise, you are tasked to write a Python program that simulates operations on a company's account and a warehouse. 
# The program should handle various commands for performing operations like:
# adding/subtracting balance, recording sales and purchases, displaying account balance, showing warehouse status, and reviewing recorded operations.
v_option = None
v_balance = 0
v_sale = 0
v_purchase = []
v_account = 0
v_list = None
v_quantity = 0
v_warehouse = []
v_review = []

def goto(linenum):
    global line
    line = linenum
    
# 'balance': The program will prompt for an amount to add or subtract from the account.
def f_balance(): 
    global v_balance
    global v_review
    try:
        v_action = int(input("Press '1' to Add or press '2' to Subtract: "))
        if v_action != 1 and v_action != 2:
            print("Sorry {} is not a valid option.\n".format(v_action))
        else:
            v_value = float(input("Insert the amount to your balance: "))
            if v_action == 1:
                v_balance += v_value
                print("Your new balance is: {}".format(v_balance))
                v_review.append("Balance changed, added: {}".format(v_value))
            elif v_action == 2:
                if v_value <= v_balance:
                    v_balance -= v_value
                    print("Your new balance is: {}".format(v_balance))
                    v_review.append("Balance changed, subtracted: {}".format(v_value))
                else:
                    print("Sorry, you do not have balance enough to do this withdraw.\nYour actual balance is {}.".format(v_balance))
        
            
    except ValueError:
        print("Sorry {} is not a valid value.\n".format(v_value))


# 'sale': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly.        
def f_sale():
    global v_sale
    global v_balance
    global v_quantity
    global v_warehouse
    global v_review
    try:
        v_name = str(input("Insert the name of product to sell: "))
        for sale in v_warehouse:
            if sale["v_name"] == v_name:
                print("The price of {} is {}\nWe have {} in our warehouse.\n".format(v_name, sale["v_price"], sale["v_quantity"]))
                try:
                    v_sale = int(input("Insert the quantity of {} to sell: ".format(v_name)))
                    if sale["v_quantity"] >= v_sale:
                        sale["v_quantity"] -= v_sale
                        v_balance += sale["v_price"] * v_sale
                        print("Your new balance is: {}\nYour new quantity of {} is {}\n".format(v_balance, v_name, sale["v_quantity"]))
                        v_review.append("Sale made, sold: {} of {} by a total of: {}".format(v_sale, v_name, sale["v_price"] * v_sale))
                    
                    else:
                        print("Sorry, you do not have enough {} to sell.\n".format(v_name)) 
                
                except ValueError:
                    print("Sorry, you did not input a valid value.\n") 
                
            else:
                print("Sorry, we do not have {} in our warehouse.\n".format(v_name))

    except ValueError:
        print("Sorry, you did not input a valid value.\n")        

    
# 'purchase': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly. 
#             Ensure that the account balance is not negative after a purchase operation.    
def f_purchase():
    global v_purchase
    global v_balance
    global v_warehouse
    global v_review
    try:
        v_name = str(input("Insert the name of product: "))
        v_price = float(input("Insert the unit price of {}: ".format(v_name)))
        v_quantity = int(input("Insert the quantity of {}: ".format(v_name)))
        
        total_price = v_price * v_quantity
        if total_price > v_balance:
            print("Sorry, you do not have balance enough to do this purchase.\nYour actual balance is {}.".format(v_balance))
        else:       
            for purchase in v_purchase:
                if purchase["v_name"] == v_name:
                    purchase["v_price"] = v_price
                    purchase["v_quantity"] += v_quantity
                    v_review.append("Purchase made, added: {} of {} by a total of: {}".format(v_quantity, v_name, total_price))
                    break     
            else:
                v_purchase.append({"v_name": v_name, "v_price": v_price, "v_quantity": v_quantity})
                v_review.append("Purchase made, added: {} of {} by a total of: {}".format(v_quantity, v_name, total_price))
            v_balance -= total_price
            print("Your new balance is: {}".format(v_balance))
            
        print(*v_purchase, sep = "\n")
        v_warehouse = v_purchase
        print(id(v_name))
    except ValueError:
        print("Sorry, you did not input a valid value.\n")

# 'account': Display the current account balance.
def f_account():
    global v_account
    if v_account == []:
        print("The account is empty.\n")
    else:
        print("Your actual balance is: {}".format(v_balance))

# 'list': Display the total inventory in the warehouse along with product prices and quantities.
def f_list():
    global v_list
    global v_warehouse
    if v_warehouse == []:
        print("The warehouse is empty.\n")
    else:
        print(*v_warehouse, sep = "\n")  

# 'warehouse': Prompt for a product name and display its status in the warehouse.
def f_warehouse():
    global v_warehouse
    if v_warehouse == []:
        print("The warehouse is empty.\n")
    try:
        v_name = str(input("Insert the name of product to check in Warehouse: "))
        for warehouse in v_warehouse:
            if warehouse["v_name"] == v_name:
                print("The {} is Available in Warehouse.\nHave {} itens in Warehouse.\nAnd its price is {}\n".format(v_name, warehouse["v_quantity"], warehouse["v_price"]))            
            elif warehouse["v_name"] not in v_name:
                print("Sorry, we do not have {} in our warehouse.\n".format(v_name))

    except ValueError:
        print("Sorry, you did not input a valid value.\n")  

# 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. 
#           If ‘from’ and ‘to’ are empty, display all recorder operations. 
#           Handle cases where 'from' and 'to' values are out of range.
def f_review():
    global v_review
    if v_review == []:
        print("The review is empty.\n")
    else:
        print(*v_review, sep = "\n")


while v_option != 0:
    v_option = int(input("\n\nSelect one of the following options:\n1 - balance\n2 - sale\n3 - purchase\n4 - account\n5 - list\n6 - warehouse\n7 - review\n0 - end\n\n"))

    try:
        if v_option == 0:
            print("\nThank you for using our system.\n\n")
            exit()
            
        elif v_option == 1: # option to balance
            print("You choose the v_option {} to check the Balance.".format(v_option))
            f_balance()
            
        elif v_option == 2: # option to sale
            print("You choose the option {} to check the sale.".format(v_option))
            f_sale()
            
        elif v_option == 3: # option to purchase
            print("You choose the option {} to check the purchase.".format(v_option))
            f_purchase() 
                 
        elif v_option == 4: # option to account
            print("You choose the option {} to check the account.".format(v_option))
            f_account()
            
        elif v_option == 5: # option to list
            print("You choose the option {} to check the list.".format(v_option))
            f_list()
            
        elif v_option == 6: # option to warehouse
            print("You choose the option {} to check the warehouse.".format(v_option))
            f_warehouse()
            
        elif v_option == 7: # option to review
            print("You choose the ption {} to check the review.".format(v_option))
            f_review() 
                
    except ValueError:
        print("Sorry, but you have input a wrong option, please let's try again with an valid option number.\n")
        
