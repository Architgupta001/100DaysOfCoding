
total_price = 0

while(True):
    user_input = input("Enter the price of the product in dollar: ")
    if(user_input=='q'or user_input=='Q'):break;
    else:
        total_price = total_price + int(user_input)

print("Customer's total bill:",total_price,"$")