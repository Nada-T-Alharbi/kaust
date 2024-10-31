#boolean 
# == equal
#this != not equal
# the < . <= . >= . >

#Logical operators 
# or T-T=T . T-F=T
#and T-T=T . T-F=F


# in is the char in the string ?
#not in if the char not in the string
#in work in list
print('p' in 'apple')
print('x' not in 'apple')
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])

#auto test with assert #its Stop program execution when a False condition is found.
lst = ['a', 'b', 'c']

first_type = type(lst[0])
for item in lst:
    assert type(item) == first_type

#conditional execustion :
x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")


x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")#else if
else:
    print("x and y must be equal")

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
if x>90 in percent_rain :
    resps = ["Bring an umbrella"] 
elif x>80 in percent_rain:
    resps.add("Good for the flowers?")
elif x>50 in percent_rain:
    resps.add("Watch out for clouds!")
else:
    resps.add("Nice day!")
#Accumulator with Conditionals
phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print(tot)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0 
for word in words:
    if len(word) > 3:
        num_words += 1


words = ["water", "chair", "pen", "basket", "hi", "car", "smile"]
past_tense = []

for word in words:
    if word.endswith("e"):
        past_tense.append(word + "d")
    else:
        past_tense.append(word + "ed")
#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
values = rainfall_mi.split(',')
num_rainy_months = 0
for value in values:
    if float(value) > 3.0:
        num_rainy_months += 1


#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count =  0
words = sentence.split()
# Write your code here.
for i in words:
    if i[0] == i[-1]:
        same_letter_count+=1


#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0

for i in items:
    if 'w' in i :
        acc_num +=1

#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0 
word = sentence.split()

for i in word:
    if 'e' in i or 'a' in i:
        num_a_or_e +=1
        

#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0 

for i in s:
    if i in vowels:
        num_vowels +=1



