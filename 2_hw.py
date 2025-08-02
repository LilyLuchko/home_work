def task_1():
	a:int = 6
	b:float = 7.2
	c:bool = False
	d:list = [3,4]
	e:str='string'
	return a,type(a),b,type(b),c,type(c),d,type(d),e,type(e)
	
call=task_1()
print(call)


def task_2():
	a = [1, 2, 3, 5, 8, 13, 21]
	return a[0:3],type(a)
	#срез строки,натуральные числа
call_2=task_2()
print(call_2)

def task_3(a):
	return a**2,type(task_3),type(a)
	
deg = task_3(4.4)
print(deg)
