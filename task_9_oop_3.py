class Soda:
	def __init__(self,dobavka):
		self.dobavka=dobavka
	def show_my_drink(self):
		if self.dobavka:
			print(f'Soda and {self.dobavka}')
		else:
			print('Just soda')
soda_pink=Soda('Pink rose')
soda=Soda('')
soda_pink.show_my_drink()
soda.show_my_drink()

