#!/opt/anaconda3/bin/python3


### 1. Write a program to reverse an integer in Python.

#number = int(input("Please enter the number:\n"))
number = 123
print("Before reverse number: %s" % (number))

reverse_num = 0

while number != 0:
    reverse_num = reverse_num * 10 + number % 10
    number = number // 10

print("After reverse number: %s" %(reverse_num))


""" This code takes an input from the user and stores it in the variable n. Then, it prints the original number n.
After that, it initializes a variable reverse to 0 and uses a while loop to continuously add the last digit of n to reverse while also
updating n to be the integer division of n by 10, until n becomes zero. Finally, it prints the reversed number. """



### 2. Write a program in Python to check whether an integer is Armstrong number or not.

"""
What is Amstrong number?

Example: 153  == (1*1*1) + (5*5*5) + (3*3*3) its Amstrong number
"""

i_num = 153
orig_num = 153

sum = 0
while i_num != 0:
    num = i_num % 10
    sum = sum +  (num**3)
    i_num = i_num // 10

if orig_num == sum:
    print("Number %s is Amstrong number" % orig_num)
else:
   print("Not Amstrong number")    



