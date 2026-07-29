new = (1,2,3)
print(type(new))
print(new)

ntpl = (1,2,3,4,5,6)
temp = list(ntpl)
temp.append(7)
temp.pop(3)
temp[2]= "Okay"
ntpl = tuple(temp)
print(ntpl)

# count() is uswd to cont occurence