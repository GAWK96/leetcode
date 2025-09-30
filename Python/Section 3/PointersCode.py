dict1 = {
    'value': 11
}
dict2 = dict1 
print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict point to:", id(dict1))
print("dict2 point to:", id(dict2))
##Same alocation in memory
dict2['value'] = 22 

print("\nAfter value is upated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict points to:", id(dict1))
print("dict2 point to:", id(dict2)) 
##Both location od dict1 and dict2 changed and are the same
##integers are imutable and can't change,
# different than dictionaries 