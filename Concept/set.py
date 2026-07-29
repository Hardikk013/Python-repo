# set_name = {1,1,2,2,3,3,4,4,5,5}
# print(set_name)

# for creating empty set
# new_set = set()
# print(type(new_set))

# union in sets
s1 = {1,3,2}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)

# update method in sets to insert multiple value
v1 = {"lists","tuples","sets","arrays",1}
v2 = {1,2,3,4}
v1.update(v2)
print(v1)

# intersection only gives same value 
ci1 = {"Surat","navsari","kamrej"}
ci2 = {"Surat","jamnagar","navsari"}
ci3 = ci1.intersection(ci2)
print(ci3)

# symetric difference prints different values
ci4 = ci1.symmetric_difference(ci2)
print(ci4)

# to add a single value and for multiple value use update 
city = {"Surat","Kamrej"}
city.add("Navsari")
print(city)

# remove method is used to remove a particular value 
city1 = {"Surat","Kamrej","Jamnagar"}
city1.add("Navsari")
city1.remove("Jamnagar")
print(city1)

# pop removes random value from a set
newli = {"Khaman","litti","dal"}
newli.pop()
print(newli)

# to check if the item is in the list or not 
dg ={"BCA","BBA","BSC-IT","BTECH"}
if "BCA" in dg:
    print("Record Found")
else:
    print("Not Available")