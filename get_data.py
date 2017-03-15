from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
adress = 'http://www.minpairs.talktalk.net'

# adress + '/minimal.html'


class CL_links():
	mass = []
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg

	def add(self, attr):
		CL_links.mass.append(attr)

	def start(self,full_adress):
		driver.get(full_adress)
		html_doc = driver.page_source
		soup = BeautifulSoup(html_doc, 'lxml')
		self.find_links(soup)

	def find_links(self,soup_find):
		for tbody in soup_find.find_all('tbody'):
			for tr in tbody.find_all('tr'):
				for td in tr.find_all('td'):
						mylink = td.find('a')
						if mylink !=None:
							self.add(adress + '/' + mylink['href'])


co_links = CL_links()
co_links.start(adress + '/minimal.html')

# mass = set(mass)

# mass =  sorted(mass, key=lambda student: student[0] , reverse=True)
print CL_links.mass		
# print len(mass)

driver.quit()