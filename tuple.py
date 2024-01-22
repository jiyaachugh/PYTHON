#TUPLE CREATED
colours = ("red","blue","white","black")

#SINGLE ITEM TUBLE
# CONSIDERING A SINGLE ITEM IN TUPLE WITHOUT COMMA,IT'S A STRING
# fruits = ("orange") # STRING
fruits = tuple(("orange"))
name = ("jiya",) # TUPLE


#CHECKING TYPE
print(type(colours))
print(type(fruits))
print(type(name))

#CHECKING LENGHT OF TUPLE
print(len(fruits))
print(len(name))
print(len(colours))

# ACESSING ITEMS IN A TUPLE (positive index)
print(colours[0]) # SQUARE BRACKETS WILL BE USED

# negative indexing
print(colours[-4])

#range indexing (SAME AS LIST)
print(colours[1:3]) # last index excluded
print(colours[-3:-1])

# PRESENCE OF AN ITEM
if "red" in colours:
    print("red is in colours")

# TRANSVERSE THE TUPLE
for i in colours:
    print(i)
    
# CONCATENATE 2 TUBLES
more_colours = ("pink","grey","green")
# colours = colours + more_colours
# print(colours)

#UNPACKING A TUPLE
colour1,colour2,colour3,colour4 = colours
print(colour1,colour2,colour3,colour4 )