#!/opt/anaconda3/bin/python3

###1. Python program to remove given character from String.

"""
Remove character from string using replace() method in python
"""

string="Nnaveen"
print(string.replace("N", ""))

###2. Python Program to count occurrence of a given characters in string.

""" Using for loop """

cha = "n"

string = "naveen"

count = 0

for s in string:
    if cha == s:
        count += 1
print(count)


""" Using while loop """

count = 0
string = "naveen"
cha = "n"
length = len(string)
index = 0
while length != 0:
    if cha == string[index]:
        count += 1
    index = index + 1
    length = length - 1
print(count)

""" Using any built-in method """

ch = "n"
for i in string:
   if ch == i:
       print(string.count(i))
       break

###3. Python Program to check if two Strings are Anagram.


"""" Using sorted function """
s1 = "python"
s2 = "onpyth"

def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(anagram(s1, s2))

""" Another method """

s1 = "python"
s2 = "onpyth"

def count(s):
    count_dict = {}
    for i in s:
        if i in count_dict:
            count_dict[i] = count_dict[i] + 1
        else:
            count_dict[i] = 1
    return count_dict

s1_count = count(s1)
s2_count = count(s2)

val = 1
for i in s1_count.keys():
    if s1_count[i] != s2_count[i]:
        val = 0
print(val)


###4. Python program to check a String is palindrome or not.

""" Using string slice """

s = "madam"
r = s[::-1]
if s == r:
    print("palindrome")
else:
    print("not - palindrome")

""" Using logic """

s = "mada"
flag = 1
length = len(s)
for i in s:
    length = length - 1
    if i != s[length]:
        flag = 0
if flag:
    print("Palindrome")
else:
    print("not palindrome")

     
###5.Python program to check given character is vowel or consonant.

c = "n"

vow = "aeiou"
flag = 0
for v in vow:
   if c == v:
       flag = 1

if flag:
    print("True")
else:
    print("False")


###6. Python program to check given character is digit or not.

""" You can use isdigit method also """

c = "9"

digits = "0123456789"

is_digit = 0
for i in digits:
    if i == c:
        is_digit = 1

if is_digit:
    print("true")
else:
    print("false")

###7.Python program to check given character is digit or not using isdigit() method.

ch = "u" 
if ch.isdigit():
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is not a Digit")


###8.Python program to replace the string space with a given character.

char = "n"
string = "naveen"
print(string.replace("n", "c"))

###9. Python program to convert lowercase char to uppercase of string

string = "NAVEEN"
print(string.lower())

###10.Python program to convert lowercase vowel to uppercase in string.

string = "naveen"
print(string.upper())

###11.Python program to delete vowels in a given string.

string = "naveen"
new_string = ""
for i in range(0, len(string)):
    if string[i] == "a" or string[i] == "i" or string[i] == "o" or string[i] == "e" or string[i] == "u" :
        continue
    else: 
        new_string = new_string+string[i]
print(new_string)

""" Using join and in """

#def delete_vowels(str):
#  vowels = "aeiouAEIOU"
#  str_without_vowels = "".join([c for c in str if c not in vowels])
#  return str_without_vowels

