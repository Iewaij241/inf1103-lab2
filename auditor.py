# Smart Inventory Auditor

# 1. Initialize inventory to zero
inventory = 0

# Keep track of failed/rejected entries
failed_entries = 0

# 2. Continuous loop until user types "quit"
while True:
    user_input = input("Enter stock quantity (or 'quit' to finish): ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break

    # 4. Handle invalid input
    if not user_input.isdigit():
        print("Error: Invalid input. Please enter a positive integer.")
        failed_entries += 1
        continue

    # Convert the input to an integer
    stock = int(user_input)

    # 5. Reject negative numbers
    # Note: isdigit() already prevents inputs such as "-10"
    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    # 6. Manage state - add stock to running total
    inventory += stock

    print("Stock accepted.")
    print("Current inventory:", inventory)

    # 7. Trigger overstock alert
    if inventory > 500:
        print("ALERT: Inventory exceeds 500 units!")
        break

# 8. Reporting
print("\n--- Inventory Report ---")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)