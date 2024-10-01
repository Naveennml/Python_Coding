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

"""
Recursion has 2 things
- Base case  
- recursive case
"""


def fibonacci(number):
    if number == 0: # Base Case
        return number
    elif number == 1:
        return number # Base Case
    else:
        return fibonacci(number-1) + fibonacci(number-2) # Recursive Case
    
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


###13. Write a program in Python to find prime factors of a given integer.


"""
Consider 12
Factors of 12 are 1, 2, 3, 4, 6, 12 because all of these numbers can divide 12 without leaving any remainder.

A prime number is a number that has only two factors: 1 and itself.
Examples of prime numbers are 2, 3, 5, 7, 11, etc.

Prime factors are factors of a number that are prime numbers.

First, list the factors of 12: 
1, 2, 3, 4, 6, 12
Now, from these factors, only 2 and 3 are prime numbers

Therefore, the prime factors of 12 are 2 and 3.

12/(2) = 6  , 6/(2) = 3, 3/(3) = 1

[ 2*2*3 ] i.e [ 2, 2, 3] 
"""

def factors(number):
    num = 2
    factors = []
    while num * num <= number:
        if number % num:
            num += 1
        else:
            number //= num
            factors.append(num)
    if num > 1:
        factors.append(number)
    return factors 

number = 12
f=factors(number)
print(f)


###14.Write a program in Python to add two integer without using arithmetic operator?

"""
Binary of 8 = 8/2(0), 4/2(0), 2/1(0), (1) ... 1000
Decimal of 1000 is 
32 16 8 4 2 1
      1 0 0 0    ....... 8

carry = a & b

    0101
  & 0011
  --------
    0001  (This is the carry)

a = a ^ b

    0101
  ^ 0011
  --------
    0110  (This is the sum without carry)


b = carry << 1

    0001  (carry)
  << 1
  --------
    0010  (This is the new value of b)

"""


def sum(a, b):
    while b!= 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

a=5
b=3
s=sum(a,b)
print(s)


###15. Write a program in Python to find given number is perfect or not?

"""
What is Perfect Number?

consider 8 & 6

6/1 = 6, 6/2 = 3, 3/3 = 1  .. sum of divider 1+2+3 = 6 its a perfect number
8/1 = 8, 8/2 = 4, 4/4 = 1 ..  sum of divider 1+2+4 = 7 its not a perfect number

"""

def perfect(num):
    sum = 0
    for i in range(1, (num//2)+1):
        if num % i == 0:
            sum = sum+i
   
    if sum == num:
        return "perfect"
    else:
        return "not perfect"

num = 6
print(perfect(num))


###16. Python Program to find the Average of numbers with explanations

numbers = [4, 8, 15, 16, 23]
sum = 0
size = len(numbers)
for i in range(size):
    sum += numbers[i]
print("Avg", sum/len(numbers))

###17. Python Program to calculate factorial using iterative method.

"""
factorial of 5 is 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

def factorial(number):
    final = 1
    for i in range(1, number+1):
        print(i)
        final = final * i
    return final

number = 5
final = factorial(number)
print(final)


###18. Python Program to calculate factorial using recursion.

def fact(n):
   if n == 0:
       return 1
   else:
       return n * fact(n-1)

n=5
res=fact(n)
print(res)


###19.Python Program to check a given number is even or odd.

n=5

if n % 2:
    print("odd")
else:
    print("even")

