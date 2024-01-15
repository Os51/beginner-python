# Ground Shipping
def groundShipping(weight):
  if weight <= 2:
    price_per_pound = 1.50 * weight
    cost = flat_charge + price_per_pound
  elif weight >2 and weight <= 6:
    price_per_pound = 3.00 * weight
    cost = flat_charge + price_per_pound
  elif weight > 6 and weight <= 10:
    price_per_pound = 4.00 * weight
    cost = flat_charge + price_per_pound
  else:
    price_per_pound = 4.75 * weight
    cost = flat_charge + price_per_pound
  print(cost)

# Drone Shipping
def droneShipping(weight):
  if weight <=2:
    cost = 4.50 * weight
  elif weight > 2 and weight <= 6:
    cost = 9.00 * weight
  elif weight > 6 and weight <= 10:
    cost = 12.00 * weight
  else: 
    cost = 14.25 * weight
  print(cost)

weight = float(input("Enter the weight of your package: "))
shipping_method = int(input("Enter your shipping method.\n1.Ground Shipping\n2. Ground Shipping Premium\n3. Drone Shipping\n"))

if shipping_method == 1:
  flat_rate = 20.00
  groundShipping(weight)
elif shipping_method == 2:
  flat_charge = 125.00
  print("Ground Shipping Premium $" + str(flat_charge))
  groundShipping(weight)
elif shipping_method == 3:
  droneShipping(weight)
