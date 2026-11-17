# 1. if - only

# A store says if you buy more than $100 worth of
# products, you get a 10% discount

purchase_amount = float(input("Amount? "))
if purchase_amount > 100:
    print("-- Eligible for 10% discount --")
    purchase_amount *= 0.9

print(f"Please pay ${purchase_amount:.2f}")