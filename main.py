from budget import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "initial deposit")
clothing.deposit(1000, "initial deposit")
entertainment.deposit(1000, "initial deposit")

food.withdraw(10.15, "groceries")
clothing.withdraw(15.89, "clothes")
entertainment.withdraw(5.60, "movie")

print(food)
print(clothing)
print(entertainment)

food.transfer(50, clothing)

print(food)
print(clothing)
print(entertainment)

print(create_spend_chart([food, clothing, entertainment]))
