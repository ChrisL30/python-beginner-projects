price_per_apple = 0.5
price_per_orange = 0.5
price_per_banana = 0.25
managers_first_name = "Chris"
cashiers_first_name = "Kris"


# equal to and not equal to
print(price_per_apple == price_per_orange)
print(price_per_apple==price_per_banana)
print(price_per_apple == price_per_banana)
print(price_per_apple != price_per_banana)
print(price_per_orange != price_per_apple)
print(managers_first_name == cashiers_first_name)

# greater than / less than
print(price_per_apple > price_per_banana)
print(price_per_apple < price_per_banana)

#combination
print(price_per_apple >= price_per_orange)
print(price_per_banana >= price_per_apple)

# Combining Condition for Booleans (and, or, not)
price_per_apple = 0.50
apple_needs_fridge = False
apples_per_bag = 10
price_per_mango = 0.75
mango_needs_fridge = True
mangos_per_bag = 5

# 'and' Operator
worth_stocking_apples = (price_per_apple > 0.35) and (apples_per_bag > 8)
worth_stocking_mangos = (price_per_mango > 1.00) and (mangos_per_bag > 3)
print(worth_stocking_apples)
print(worth_stocking_mangos)



# 'or' Operator
worth_stocking_apples = (price_per_apple > 0.35) or (apple_needs_fridge == False)
worth_stocking_mangos = (price_per_mango > 1.00) or (mangos_per_bag > 3)
print(worth_stocking_apples)
print(worth_stocking_mangos)


# 'not' Operator
worth_stocking_apples = not(price_per_apple <= 0.35)
print(worth_stocking_apples)
worth_stocking_mangos = not(price_per_mango <= 0.90)
print(worth_stocking_mangos)
