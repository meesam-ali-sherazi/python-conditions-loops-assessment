# Smart Pharmacy Inventory & Sales Management System
# Topic: for loop, range(), conditions, counters and accumulators

print("==============================================")
print("    SMART PHARMACY INVENTORY & SALES SYSTEM")
print("==============================================")

# Step 1: Validate number of medicines

while True:
    try:
        total_medicines = int(input("How many different medicines? "))

        if total_medicines > 0:
            break
        else:
            print("Invalid input! Enter at least 1 medicine.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Step 2: Initialize accumulator and counter

total_revenue = 0
restocking_count = 0

# Step 3: Process medicines using for loop

for medicine_number in range(1, total_medicines + 1):

    print(f"\n========== MEDICINE {medicine_number} ==========")

    # Collect medicine name

    while True:
        medicine_name = input("Enter medicine name: ").strip()

        if medicine_name != "":
            break
        else:
            print("Medicine name cannot be empty!")

    # Collect available stock

    while True:
        try:
            available_stock = int(input("Enter available stock: "))

            if available_stock >= 0:
                break
            else:
                print("Stock cannot be negative!")

        except ValueError:
            print("Please enter a valid whole number.")

    # Collect price per unit

    while True:
        try:
            price = float(input("Enter price per unit (Rs.): "))

            if price >= 0:
                break
            else:
                print("Price cannot be negative!")

        except ValueError:
            print("Please enter a valid price.")

    # Collect quantity sold and check stock availability

    while True:
        try:
            quantity_sold = int(input("Enter quantity sold: "))

            if quantity_sold < 0:
                print("Quantity sold cannot be negative!")

            elif quantity_sold > available_stock:
                print("Insufficient stock! Available stock is:",
                      available_stock)

            else:
                break

        except ValueError:
            print("Please enter a valid whole number.")

    # Calculate sales amount and remaining stock

    sales_amount = quantity_sold * price
    remaining_stock = available_stock - quantity_sold

    # Display medicine details

    print("\n----- MEDICINE SALES DETAILS -----")
    print("Medicine Name:", medicine_name)
    print("Available Stock:", available_stock)
    print("Quantity Sold:", quantity_sold)
    print("Sales Amount: Rs.", sales_amount)
    print("Remaining Stock:", remaining_stock)

    # Update total pharmacy revenue

    total_revenue += sales_amount

    # Check low stock and count medicines for restocking

    if remaining_stock < 10:
        print("WARNING: Low Stock! Restocking Required.")
        restocking_count += 1

    else:
        print("Stock Status: Sufficient Stock")

# Step 4: Generate final pharmacy report

print("\n==============================================")
print("       FINAL PHARMACY SALES REPORT")
print("==============================================")

print("Total Medicines Processed:", total_medicines)
print("Total Pharmacy Revenue: Rs.", total_revenue)
print("Medicines Requiring Restocking:", restocking_count)

print("\nThank you for using Smart Pharmacy System!")
print("==============================================")