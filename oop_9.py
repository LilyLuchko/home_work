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
