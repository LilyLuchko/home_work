class Page:
	def __init__(self,url):
		self.url=url
	def get(self):
		print(self.url)
print_url=Page('https://terver.com')
print_url.get()
