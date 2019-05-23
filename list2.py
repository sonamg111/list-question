list1=[1,4,6,3,7]
list2=[5,2,4,1,8]
new_list=[]
i=0
while i<len(list2):
	if (list1[i] not in list2):
		new_list.append(list1[i])
	i=i+1
print new_list

