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
def three_numbers(a,b,c):
	if a>10 and b>10 and c>10:
		print("Yes")
	else:
		print("No")
three_numbers(1,3,8)
three_numbers(11,43,78)
three_numbers(1,3,-8)
three_numbers(10.3,10.02,10.1)
