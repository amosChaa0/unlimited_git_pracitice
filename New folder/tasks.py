# create a list named "numbers" containing the numbers1,3,5, 7 and 9
li=[1,3,5,7,9]
print(li[1])
li[3]=10
print(li)
li.append(12)
li.remove(5)
print(li)
sliced_list=li[2:]
print(sliced_list)
combined_list=li+sliced_list
print(combined_list)
print(8 in li)
combined_list.sort()
print(combined_list)

