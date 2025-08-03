class Button:
	
	def __init__(self,text,link):
		self.text=text
		self.link=link
home=Button('Домой','/home')
catalog_msk=Button('Каталог','/msk/catalog')
print(home.text)
print('Button '+home.text+' has link '+home.link)
print('\n')
print(catalog_msk.text)
class Input:
	def __init__(self,Loc,text):
		self.Loc=Loc
search=Input('Moscow')
print(search.Loc)



class Page:
	def __init__(self,url):
		self.url = url
	def get(self):
		print(self.url)
home = Page('https://blabla.ru')
home.get()

class Soda:
	def __init__(self,add=None):
		self.add=add
	def show_my_drink(self):
		if self.add:
			print(f'Газировка и {self.add}')
		else:
			print('Обычная газировка')
			
			
			
gaz=Soda('apple')
gaz_2=Soda()
gaz.show_my_drink()
gaz_2.show_my_drink()
