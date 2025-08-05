class Rectangle:
	def __init__(self,width,height):
		self.width=width
		self.height=height
	def square(self):
		return self.width * self.height
	def perimeter(self):
		return 2*self.width + 2*self.height
		
rectangle_1 = Rectangle(2,3)
print(rectangle_1.square())
print(rectangle_1.perimeter())





class Math:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def addition(self):
		return(self.a + self.b)
	def multiplication(self):
	 	return self.a*self.b
	def division(self):
	 	return self.a/self.b
	def subtraction(self):
	 	return self.a-self.b
		
		
calc=Math(2,3)
print(calc.a)
print(calc.b)
print(f'Сумма = {calc.addition()}') #Здесь печатает результат
print(f'Умножение = {calc.multiplication()}') #Здесь Runtime error
print(f'Деление = {calc.division()}')
print(f'Разность = {calc.subtraction()}')
		
		

