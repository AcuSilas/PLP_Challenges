# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
#  
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 

# Print the final price after applying the discount, or if no discount was applied, print the original price.

original_price = float(input("Enter the original price of the item: "))

discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price < original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")