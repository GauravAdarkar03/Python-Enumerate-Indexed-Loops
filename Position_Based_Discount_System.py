products = ["Smartphone", "Headphones", "Charger", "Case", "Screen Guard", "Power Bank"]
base_prices = [25000, 2000, 800, 500, 300, 1500]

final_prices = []

for index, product in enumerate (products):
    original_price = base_prices[index]

    if index % 2 == 0:
        discount = 0.10
    else:
        discount = 0.05

    discounted_price = original_price * (1-discount)
    savings = original_price-discounted_price

    print(f"Position {index}: {product} - Original: Rs.{original_price}, Discounted: Rs.{discounted_price}, You save: Rs.{savings}") 

    final_prices.append(discounted_price)

print("\nFinal prices")