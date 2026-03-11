order_items = ["Laptop", "Mouse", "Keyboard", "Monitor", "USB Cable"]
prices = [45000, 500, 1500, 12000, 300]

total = 0
invoice= []

for index, items in enumerate(order_items,start=1):
    price = prices[index-1]
    print(f"Line {index}: {items} - Rs. {price}")

    total += price
    invoice.append(f"{index}.{items}")

print("\nTotal Amount:", total)

print("\nInvoice Lines List:")
print(invoice)