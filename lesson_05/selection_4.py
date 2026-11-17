# 4. nested if - else conditions
#    used for multiple tests for multiple conditions

# if earn < 100_000 and live in hdb flat get 250
# if earn >= 100_000 and live in hdb flat get 150
# if earn < 100_000 and live in private housing get 100
# if earn >= 100_000 and live in private housing get 50

# Method 1: implemented with if-elif-... flat structure
income = int(input("Enter annual income: "))
housing_type = input("Enter housing type (hdb or pte): ")

payout = 0
if income < 100_000 and housing_type == "hdb":
    payout = 250
elif income >= 100_000 and housing_type == "hdb":
    payout = 150
elif income < 100_000 and housing_type == "pte":
    payout = 100
elif income >= 100_000 and housing_type == "pte":
    payout = 50
print(f"You get ${payout} from the government")

# Method 2: nested if
if housing_type == "hdb":
    if income < 100_000:
        payout = 250
    else:   # elif income >= 100_000
        payout = 150
elif housing_type == "pte":
    if income < 100_000:
        payout = 100
    else:
        payout = 50
print(f"You get ${payout} from the government (nested if)")










