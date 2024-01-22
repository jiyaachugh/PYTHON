#creating a set
names = {"sia", "jia", "tia", "pia"}

print(names) #unordered
print(len(names)) #length of set
print(type(names)) #types of set

#accessing items of a set
for x in names:
  print(x)
  
if "jia" in names:
   print("yes jia in names") #presence of element
   
names.add("ria") # add
names.remove("tia") # remove
names.discard("xia") # won't throw error even if the element isn't present in the set
print(names)

#add another sequence to set
names_list = ["kia","ria","mia"]
names.update(names_list) #USING UPDATE FUNCTION
print(names)

#JOINING TWO SETS
s1 = {1,2,3,4}
s2 = {1,2,5,6,7}

s3 = s1.union(s2)
print(s3)


s4 = s1.intersection(s2) # common values

s5 = s1.symmetric_difference_update(s2)

print(s4,s5)