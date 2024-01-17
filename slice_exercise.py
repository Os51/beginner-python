# Your code below:
toppings = ["Pepperoni", "Pineapple", "Cheese", "Sausage", "Anchovies", "Mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [[2, "Pepperoni"], [5, "Hawaiian"], [1, "Tres Queso"], [6, "Sausage"], [2, "Olives"], [8, "American"], [1, "Mushrooms"]]
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
pizza_and_prices.pop()
pizza_and_prices.insert(4,[2.5, "Peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
