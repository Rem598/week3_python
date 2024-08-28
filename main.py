def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100 )
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    #calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
#print the finakl result
    print(f"The final price after applying discount is : {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values.")    
    