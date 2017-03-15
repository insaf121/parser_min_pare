from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
adress = 'http://www.minpairs.talktalk.net'
driver.get(adress + '/minimal.html')

html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')
mass = []



for tbody in soup.find_all('tbody'):
	for tr in tbody.find_all('tr'):
		for td in tr.find_all('td'):
				mylink = td.find('a')
				if mylink !=None:
					# sk = (adress + '/' + mylink['href'],conversion_insaf(str(mylink.text)))
					mass.append(adress + '/' + mylink['href'])


mass = set(mass)

# mass =  sorted(mass, key=lambda student: student[0] , reverse=True)
# print mass		
# print len(mass)


# a_tags = soup.find_all('a')
# for a in a_tags:
# 	# print a['href']
# 	try:
# 		print a['href']
# 	except KeyError:
#             pass # or some other fallback action

	

# remain_siblings = first_a.findNextSibling()
# array.append(remain_siblings)
# print array
driver.quit()