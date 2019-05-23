s="nitin"
lenght=len(s)
i=0
while i<lenght/2+1:
	if s[i]!=s[-i -1]:
		print"not palindrme"
		break 
	i=i+1
else:
	print"palindrme"		