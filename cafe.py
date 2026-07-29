# Cafe Management System
# This program lets a customer order food items and prints a final bill

food_items = ["Coffee", "Tea", "Sandwich", "Burger", "Pizza", "French Fries", "Cold Drink"]
food_prices = [80, 40, 120, 150, 250, 100, 60] 
# Function to show the menu to the customer
def show_menu():
    print("\n----- CAFE MENU -----")
    for i in range(len(food_items)):
        print(str(i + 1) + ". " + food_items[i] + " - Rs." + str(food_prices[i]))
    print("----------------------")

show_menu()
# Lists to keep track of what the customer orders
ordered_items = []
ordered_qty = []
ordered_price = []

# Variable to keep the running total
total_bill = 0
# Let the customer keep ordering until they say stop
keep_ordering = True

while keep_ordering:
    choice = input("Enter the item number you want to order: ")
    choice = int(choice)

    if choice >= 1 and choice <= len(food_items):
        item_name = food_items[choice - 1]
        item_price = food_prices[choice - 1]

        qty = input("Enter quantity: ")
        qty = int(qty)

        cost = item_price * qty
        total_bill = total_bill + cost

        ordered_items.append(item_name)
        ordered_qty.append(qty)
        ordered_price.append(item_price)

        print(item_name + " added to your order!")
    else:
        print("Invalid choice! Please select a valid item number from the menu.")

    more = input("Do you want to order more items? (yes/no): ")
    if more.lower() != "yes":
        keep_ordering = False
# Print the final bill
print("\n===== FINAL BILL =====")
print("Item\t\tQty\tPrice\tTotal")

for i in range(len(ordered_items)):
    item = ordered_items[i]
    qty = ordered_qty[i]
    price = ordered_price[i]
    line_total = price * qty
    print(item + "\t\t" + str(qty) + "\t" + str(price) + "\t" + str(line_total))

print("-----------------------")
print("Grand Total: Rs." + str(total_bill))
print("=======================")
# Testing auto-merge workflow from dev-raj1 - attempt 2
# your dev-raj2 change here .