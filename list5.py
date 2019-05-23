numbers=[50,40,23,70,56,12,5,10,7]
max=max(numbers[0],numbers[1])
secondmax=min(numbers[0],numbers[1])
i=0
while i<len(numbers):
	if numbers[i]>max:
		secondmax=max
		max=numbers[i]
	else:
		if numbers[i]>secondmax:
			secondmax=numbers[i]
	print str(numbers)
	i=i+1			 			 