fruits = [ "apple", "mango", "banana", "cherry"]

new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

fruits = fruits + new_fruits # contatinating two list

print(fruits)

# NESTED LIST
list = [10,20,30,[40,50,60]]

print(list[2])
print(list[3][1])
fruits.insert(2, ["kiwi", "orange"])
print(fruits)