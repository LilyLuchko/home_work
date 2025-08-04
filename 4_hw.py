class Rectangle:
	def __init__(self,width,height):
		self.width=width
		self.height=height
	def square(self):
		return self.width * self.height
	def perimeter(self):
		return 2*width + 2*height
		
rectangle_1 = Rectangle(2,3) #Runtime error
print(rectangle_1.square())
print(rectangle_1.perimeter())

class Math:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def addition(self):
		return(self.a + self.b)
	def multiplication(a,b):
		return a*b
	def division(a,b):
		return a/b
	def subtraction(a,b):
		return a-b
		
		
test=Math(2,3)
print(test.a)
print(test.b)
print(f'Сумма = {test.addition()}') #Здесь печатает результат
test_2=Math(4,5)
print(f'Умножение = {test_2.multiplication()}') #Здесь Runtime error
# print(f'Деление = {test.division()}')
# print(f'Разность = {test.subtraction()}')
# print(f'Сумма = {test.addition()}')
