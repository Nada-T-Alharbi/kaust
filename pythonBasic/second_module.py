s = "Hello world"
#    1234567891011#the len is 11
#A list is a sequential collection of Python data values, where each value is identified by an index 
# , called its elements,the items can be of different types.
b=["hello", 2.0, 5, [10, 20]]

# A tuple,like a list
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

#The key difference between lists and tuples is that a tuple is immutable
# ,meaning that its contents can’t be changed after the tuple is created.
t = (5,)#To create a tuple with a single element include the final comma
print(type(t))

x = (5)
print(type(x))

#The Index Operator
school = "Luther College"
m = school[2]# the index start from 0 
print(m)
lastchar = school[-1]#its just start from -1
print(lastchar)

#The Slice Operato
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])
fruit = "banana"
print(fruit[:3])#from bigin to 3
print(fruit[3:])#from 3 to the end

#tuple slices 
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)


fruit = ["apple","orange","banana","cherry"]
print([1,2] + [3,4])
print(fruit+[6,7,8,9])

print([0] * 4)

#count : case - sencitive return how many repated
a = "I have had an apple on my desk before!"
print(a.count("e"))
#indix :return the indeix of the element
music = "Pull out your music and dancing can begin"
print(music.index("m"))

#split , 
song = "The rain in Spain..."
wds = song.split()#search for the space between the wlmwnt and split it to list
wds = song.split('ai')#split and remove the ai from list
print(wds)
#join jpin the split back
wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

#loop
# genres is a list defined elsewhere

for genre in genres:
    print(genre)



w = range(10)

tot = 0
print("***** Before the For Loop ******")
for num in w:
    print("***** A New Loop Iteration ******")
    print("Value of num:", num)
    tot += num
    print("Value of tot:", tot)
print("***** End of For Loop *****")
print("Final total:", tot)
