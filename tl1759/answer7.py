raw_list = [1,2,3,4,5,6,7,8,9]
list1 = raw_list[:4]
list2 = [1,1,1,2,2,2,3,3,3,4,4,4]
list1.extend(list2)
list1.sort()
print list1
