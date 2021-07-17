"""
9.	A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.
"""
price = float(input("price of the meal= "))
percent_tip = float(input("percent tip %= "))
sum_total = price + (price/100) * percent_tip
print("The total bill with the tip included is`", sum_total)
