def max_number(a,b):
	if a>b:
		print(a)
	else:
		print(b)
	
max_number(2,3)	
max_number(7,8)

def difference(a,b):
	if a-b==135:
		print ('yes')
		
	else:
		print ('No')
difference(137,2)		
difference(2,137)
difference(137.066,2.066)
def seasons(a):
	if a==1 or a==2 or a==12:
		print('It\'s winter')
	elif a in range(3,6):
		print('It\'s spring')
	elif a in range(6,9):
		print('It\'s summer')
	else:
		print('autumn')
		
seasons(11)
