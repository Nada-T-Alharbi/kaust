#Change the Object : 
#mutability : a value that can change them . cnat replace a str

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)


#Strings are Immutable

greeting = "Hello, world!"
greeting[0] = 'J'            # ERROR!
print(greeting)
# the correct 
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

#delete the item in list by using del


alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)#['a', 'f']


# point :checks whether two variables points to the same object : is
a = [81,82,83]
b = [81,82,83]

print(a is b)#false

print(a == b)#true , here combire the value not the point(refrence)

print(id(a))
print(id(b))#will print a diffrent value

#cloning : copy from list
a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

#lists are mutable, tuples and strings not


#method on list

# append : add item it the last of the list 
#inset : add item in spicific place (list.insert(index , the item))
#count : count how many times the element apper
#index : where the postion on the item
#reverse : reverce the list
#sot : order the lsit from big to small 
#remove : remove the value not the index like del 
#pop : remove the last value
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)

print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)


#append with concatnation 
origlist = [45,32,88]
origlist = origlist + ["cat"]

# Non-mutating Methods on Strings
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()

ss = "    Hello, World    "

els = ss.count("l")#count how many times l appear
print(els)

print("***"+ss.strip()+"***")#strip remove the whiat space srom beginig and end 

news = ss.replace("o", "***")
print(news)

s = "python rocks"
print(s[1]*s.index("n"))#repet the string which s is the many times

#format :makes substitutions into places in a string enclosed in braces
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)#:.2f that is mean i need two degit after coma
print(calculation)

#f-String : 
name = "Rodney Dangerfield"
score = -1
print("Hello {}. Your score is {}.".format(name, score))
print(f"Hello {name}. Your score is {score}.")
first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {first_name} {last_name}. Your score is {max(score, 60)}.")
