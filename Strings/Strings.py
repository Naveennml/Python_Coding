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


###12.Python program to count Occurrence Of Vowels & Consonants in a String.

vowel = "aeiou"
string = "naveen"

v_c = 0
c_c = 0

for i in string:
    if i in vowel:
        v_c += 1
    else:
        c_c += 1
print(f"Vowels: {v_c}, Consonanats: {c_c}")

###13. Python program to print the highest frequency character in a String.

string = "Hello every one"
dict = {}
for i in string:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
grater = {count : 0, val : ''}
for k in dict.keys():
   if dict[k] > grater[count]:
       grater[count] = dict[k]
       grater[val] = k
print(f"char {grater[val]}, val {grater[count]}")


###14. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.

string = "naveen"
for i in string:
    if i in "aeiou":
        string_new = string.replace(i, "-")
        break
print(string_new)


###15. Python program to count alphabets, digits and special characters.

alphabet = 0
digits = 0
specil_charcter = 0

string = "Hi Naveen @1123 how are you ?"
for i in string:
    if i == " ":
        next
    elif i.isdigit():
        digits += 1
    elif i.isalpha():
        alphabet += 1
    else:
        specil_charcter += 1

print(f"alph : {alphabet}, dig : {digits}, speci : {specil_charcter}")


###16. Python program to separate characters in a given string.

string = 'naveen'
out = [ i for i in string ]
print(out)

###17. Python program to remove blank space from string.

string = "Hi Naveen @how are you ?"
print(string.replace(" ", ""))

###18. Python program to concatenate two strings using join() method.

string1 = "Naveen"
string2 = "Chaithra"

print("".join([string1, string2]))

###19. Python program to concatenate two strings without using join() method.

string1 = "Naveen"
string2 = "Chaithra"

print(string1+string2)

###20. Python program to remove repeated character from string.

string = "naveen"
for i in  string:
    if string.count(i) > 1:
        string = string.replace(i, "")
print(string)


""" other way """

def remove_duplicates(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string
input_string = "example string"
output_string = remove_duplicates(input_string)
print(output_string)


###21. Python program to calculate sum of integers in string

string = "qwel123rty456"
sum = 0
for i in string:
    if i.isdigit():
        di = int(i)
        sum = sum + di
print(sum)

###22. Python program to print all non repeating character in string.

string = "naveen"

new_sting = ""

for i in string:
    if string.count(i) == 1:
        new_sting = new_sting + i
print(new_sting)

### 23. Python program to copy one string to another string.

st1 = "Naveen"
st2 =  st1
print(st2)

### 24. Python Program to sort characters of string in ascending order.

st = "naveen"
print("".join(sorted(st)))

### 25. Python Program to sort character of string in descending order.

st = "naveen"
print("".join(sorted(st, reverse=True)))

