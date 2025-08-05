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






class Button:
	type_button='Кнопка'
class Button_sidebar(Button):
	def __init__(self,text,loc=None):
		self.text=text
		self.loc=loc
	def print_name_of_button(self):
		print(f'Кнопка называется {self.text}')
	def press_the_button(self):
		print(f'Клик по кнопке {self.text}')
text_box=Button_sidebar('Text Box')
text_box.print_name_of_button()
text_box.press_the_button()
check_box=Button_sidebar('Check Box')
check_box.print_name_of_button()
check_box.press_the_button()
radio_button=Button_sidebar('Radio Box')
radio_button.print_name_of_button()
radio_button.press_the_button()
web_tables=Button_sidebar('Web Tables')
web_tables.print_name_of_button()
web_tables.press_the_button()
web_tables=Button_sidebar('Web Tables')
web_tables.print_name_of_button()
web_tables.press_the_button()
		
		

