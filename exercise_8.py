"""8.Write a program that asks the user to enter three numbers (use three separate input statements).
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
"""

num1 = float(input("enter the number 1 -> "))
num2 = float(input("enter the number 2 -> "))
num3 = float(input("enter the number 3 -> "))
sum_nums = num1 + num2 + num3
average_nums = sum_nums / 3

print("sum= ", sum_nums, ",", " average= ", average_nums, sep="")