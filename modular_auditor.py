# Smart Inventory Auditor - Modular Version


def get_valid_input():
    """Get and validate stock quantity from the user."""

    user_input = input("Enter stock quantity (or 'quit' to finish): ")

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Error: Invalid input. Please enter a positive integer.")
        return None

    stock = int(user_input)

    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        return None

    return stock


def process_delivery(current_total, new_value):
    """Add the new delivery to the current inventory total."""

    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    """Calculate 10% tax for a delivery."""

    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    """Print the final inventory report."""

    print("\n--- Inventory Report ---")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


# Main program

# 1. Initialize inventory to zero
inventory = 0

# Counter for failed/rejected entries
failed_attempts = 0

# Counter for successful deliveries
deliveries_processed = 0


# 2. Continuous loop
while True:

    # Get and validate user input
    delivery = get_valid_input()

    # Check if user wants to quit
    if delivery == "quit":
        break

    # Check if input was invalid
    if delivery is None:
        failed_attempts += 1
        continue

    # 3. Process valid delivery
    inventory = process_delivery(inventory, delivery)

    # Calculate tax for this delivery
    tax = calculate_tax(delivery)

    # Update delivery counter
    deliveries_processed += 1

    print("Delivery accepted.")
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)


# 4. Generate final report
generate_report(inventory, failed_attempts)