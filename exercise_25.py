"""25.	Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
"""
a = input("Enter four-digit number >>>")
suma = 0
for digit in a:
    suma += int(digit)
print(a[0], "+", a[1], "+", a[2], "+", a[3], "=", suma, sep="")
