#!/opt/anaconda3/bin/python3


### 1. Write a program to reverse an integer in Python.

# number = int(input("Please enter the number:\n"))
number = 123
print("Before reverse number: %s" % (number))

reverse_num = 0

while number != 0:
    reverse_num = reverse_num * 10 + number % 10
    number = number // 10

print("After reverse number: %s" % (reverse_num))

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
    sum = sum + (num ** 3)
    i_num = i_num // 10

if orig_num == sum:
    print("Number %s is Amstrong number" % orig_num)
else:
    print("Not Amstrong number")

###3. Write a program in Python to check given number is prime or not. What is prime number?

"""
What is prime number?

A prime number is a number which can be divided by only 1 and number itself.

2, 3, 5, 7, 13,…
"""

is_prime = 1
number = 5
for i in range(2, number // 2):
    if number % i == 0:
        is_prime = 0
        break
if is_prime:
    print("%s Prime Numebr" %(number))
else:
    print("%s Not prime" %(number))

###4.Write a program in Python to print the Fibonacci series using iterative method.

"""
What is Fibonacci Series?
A Fibonacci series is a series in which next number is a sum of previous two numbers.
For example : 0, 1, 1, 2, 3, 5, 8 ……
0
1
0+1 =1
1+1=2
2+1=3
2+3=5
"""

number=10
first=0
second=1

print("Printing fibonacci series using iterative method")
for i in range(number):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result)


###5. Write a program in Python to print the Fibonacci series using recursive method.


def fibonacci(number):
    if number == 0:
        return number
    elif number == 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
print("Printing fibonacci series using recursive method")
number=10
for i in range(number):
    print(fibonacci(i))

###6. Write a program in Python to check whether a number is palindrome or not using iterative method.

"""

What is Palindrome Number?

121 and reverse also 121 its palindrome

"""
number = 121
reverse = 0
temp_num = number

while number!= 0:
    last_num = number % 10
    reverse = reverse * 10 + last_num
    number = number // 10

if temp_num == reverse:
    print("%s Palindrome" % (temp_num))
else:
    print("%s Not Palindrome" % (temp_num))


###7. Write a program in Python to check whether a number is palindrome or not using recursive method.

def reverse(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse(n//10)))

def is_palindrome(number):
    print(reverse(number))
    if number == reverse(number):
        return True
    else:
        return False

number=121

if is_palindrome(number):
    print("%s is Palindrome" %(number))
else:
    print("%s is Not Palindrome" %(number))


###8. Write a program in Python to find greatest among three integers.


n1=3
n2=9
n3=7

if n1 > n2 and n1 > n3:
    print("%s is Greater" % n1)
elif n2 > n1 and n2 > n3:
    print("%s is Greater" % n2)
else:
    print("%s is Greater" % n3)
   

###9. Write a program in Python to check if a number is binary? 

"""
Binary number means with 1 or 0 numbers 
Example: 10001
"""

def check_binary(num):
    while num > 0:
        dig = num % 10
        if dig not in [0, 1]:
            return False
        num = num // 10
    return True

number = 10001
if check_binary(number):
    print("Binaray Number")
else:
    print("Not Binary Number")


###10. Write a program in Python to find sum of digits of a number using recursion?

def sum_dig(num):
   if num < 10:
       return num
   else:
       return num % 10 + sum_dig(num//10)
      

num = 12345
print(sum_dig(num))


###11. Write a program in Python to swap two numbers without using third variable?

a=3
b=5

a=a-b
b=a+b
a=b-a

print(a,b)

###12. Write a program in Python to swap two numbers using third variable?

a=3
b=5
tmp = a
a = b
b = tmp
print(a, b)
