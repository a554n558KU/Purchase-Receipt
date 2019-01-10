lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32
inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = .088 

# Our First Customer
customer_one_total = 0
customer_one_itemization = ""

#Adding love_seat price to customer_one_total
customer_one_total += lovely_loveseat_price

#Adding purchased items to customer_one_itemization
customer_one_itemization += stylish_settee_description

#Add luxurious lamp to customer_total
customer_one_total += luxurious_lamp_price

#Update Itemization
customer_one_itemization += luxurious_lamp_description

# Getting ready for checking out
customer_one_tax = customer_one_total * sales_tax
#Add sales tax to customer total cost
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

#Second Customer:
customer_two_total = 0
customer_two_itemization = ""

customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description

# Customer two purchased luxurious lamp
customer_two_total += luxurious_lamp_price
# Update customer two itemization list
customer_two_itemization += luxurious_lamp_description

# Sales tax
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)