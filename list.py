fruits = [ "apple", "mango", "banana", "cherry"]

print(fruits) # pront list

print(type(fruits)) # tyoe of list

print(len(fruits)) # length of list

#checking whether the item is in list or not
if "banana" in fruits:
    print ("banana is present in the list")
    
#checking whether the item is in list or not
if "kiwi" not in fruits:
    print ("kiwi is not present in the list")
    
    
# indexing in list
print(fruits[1])
print(fruits[-3])

print(fruits[1:3])