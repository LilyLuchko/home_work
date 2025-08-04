class Rectangle:
	def __init__(self,width,height):
		self.width=width
		self.height=height
	def square(self):
		return self.width * self.height
	def perimeter(self):
		return 2*width + 2*height
		
rectangle_1 = Rectangle(2,3)
print(rectangle_1.square())
print(rectangle_1.perimeter())
