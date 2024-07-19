import datetime

# Input fields
company_name = input("Enter your company name: ")
company_address = input("Enter your company address: ")

client_name = input("Enter client's name: ")
client_address = input("Enter client's address: ")

invoice_number = input("Enter invoice number: ")
invoice_date = datetime.date.today()
due_date = input("Enter due date (YYYY-MM-DD): ")

items = []
while True:
    description = input("Enter item description (or 'done' to finish): ")
    if description.lower() == 'done':
        break
    quantity = int(input("Enter quantity: "))
    rate = float(input("Enter rate: "))
    total = quantity * rate
    items.append((description, quantity, rate, total))

# Calculations
subtotal = sum(item[3] for item in items)
tax_rate = float(input("Enter tax rate (as a percentage): "))
tax = subtotal * (tax_rate / 100)
grand_total = subtotal + tax

# Invoice generation
print("\n" + "="*50)
print(f"INVOICE")
print("="*50)
print(f"From: {company_name}")
print(f"Address: {company_address}")
print("\n")
print(f"To: {client_name}")
print(f"Address: {client_address}")
print("\n")
print(f"Invoice Number: {invoice_number}")
print(f"Invoice Date: {invoice_date}")
print(f"Due Date: {due_date}")
print("\n")
print("Itemized List:")
print(f"{'Description':<20} {'Quantity':<10} {'Rate':<10} {'Total':<10}")
for item in items:
    print(f"{item[0]:<20} {item[1]:<10} {item[2]:<10} {item[3]:<10}")
print("\n")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax ({tax_rate}%): {tax:.2f}")
print(f"Grand Total: {grand_total:.2f}")
print("="*50)
