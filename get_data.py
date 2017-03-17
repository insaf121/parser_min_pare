from selenium import webdriver
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import re
<<<<<<< HEAD
from multiprocessing import Pool  #parallel
from multiprocessing.dummy import Pool as ThreadPool
=======


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
		self.mass.append(attr)

	@classmethod	
	def get_adress(self,full_adress):
		driver.get(full_adress)
		html_doc = driver.page_source
		return BeautifulSoup(html_doc, 'lxml')
		# self.find_links(soup)

	def set(self):

		# print len( list(dict.fromkeys(self.mass)) )
		self.mass = list(dict.fromkeys(self.mass))
		# set(self.mass)

	def find_links(self,soup_find):
		for tbody in soup_find.find_all('tbody'):
			for tr in tbody.find_all('tr'):
				for td in tr.find_all('td'):
						mylink = td.find('a')
						if mylink !=None:
							self.add(adress + '/' + mylink['href'])

	

# class cl_data():
# 	# """docstring for """
# 	# data_links = []
# 	data_pars  = []
# 	def __init__(self, arg):
# 		# super( self).__init__()
# 		self.data_links = arg

# 	def get_pars(self):
# 			# print len(self.data_links)
# 			for x in self.data_links:
# 				print x 
# 				# Co_parse_text = Cl_parse_text(CL_links.get_adress(x),'pre')
# 				# self.data_pars = self.data_pars + Co_parse_text.get_data()
# 				# print Co_parse_text.struct
# 				# print zx
# 				# break



# class Cl_parse_text(object):
# 	"""docstring for ClassName"""
# 	regex = r"([\w'\-]{1,})"
# 	# list_arr = []
# 	mass = []
# 	int_i = 0
# 	struct = []
# 	def __init__(self, arg,predicat):
# 		# super(ClassName, self).__init__()
# 		self.arg = arg.findAll(predicat)
# 		# self.arg = self.arg.findAll('pre')

	
# 	def add_match(self,i_find):
# 		self.int_i += 1 
# 		self.struct.append( str(i_find.group()))
# 		if self.int_i % 2 == 0:
# 			self.mass.append(self.struct)
# 			self.struct = []

# 	def get_data(self):
# 		for iss in self.arg:
# 			matches = re.finditer(self.regex, iss.text)
# 			for is_find in matches:
# 				self.add_match(is_find)
# 				# break
# 		return self.mass

class cl_data():
	# """docstring for """
	# data_links = []
	data_pars  = []
	def __init__(self, arg):
		# super( self).__init__()
		self.data_links = arg

	def get_pars(self):
			# print len(self.data_links)
			for x in self.data_links:
				print x 
				# Co_parse_text = Cl_parse_text(CL_links.get_adress(x),'pre')
				# self.data_pars = self.data_pars + Co_parse_text.get_data()
				# print Co_parse_text.struct
				# print zx
				# break


class Cl_parse_text(object):
	"""docstring for ClassName"""
	regex = r"([\w'\-]{1,})"
	# list_arr = []
	mass = []

	int_i = 0
	struct = []

	def __init__(self, arg,predicat):
		# super(ClassName, self).__init__()
		self.arg = arg.findAll(predicat)
		# self.arg = self.arg.findAll('pre')

	

	# def add_match(self,i_find):
	# 	self.int_i += 1 
	# 	self.struct.append( str(i_find.group()))
	# 	if self.int_i % 2 == 0:
	# 		self.mass.append(self.struct)
	# 		self.struct = []

	def add_match(self,i_find):
		self.int_i += 1 
		self.struct.append( str(i_find.group()))
		if self.int_i % 2 == 0:
			self.mass.append(self.struct)
			self.struct = []


	def get_data(self):
		for iss in self.arg:
			matches = re.finditer(self.regex, iss.text)
			for is_find in matches:
				# print str(i_find.group())
				self.mass.append( str(i_find.group()))
				# print self.mass
				# add_match(is_find)
				# break
		return self.mass		

				self.add_match(is_find)
				# break
		return self.mass		


	# data = {'text':(  3,  33, stripnulls),
			# 'transcript':(  33,  63, stripnulls)}
	
	# def function(self):
		# pass
		

co_links = CL_links()
<<<<<<< HEAD

# def get_funct(i_class):
co_links.find_links(soup_find = co_links.get_adress(adress + '/minimal.html') )
co_links.set()


def function_1(data_links):
	data_find = []
	for x in data_links:
		Co_parse_text = Cl_parse_text(CL_links.get_adress(x),'pre')
		data_find.append( Co_parse_text.get_data() )
		# print Co_parse_text 
	# pass
	return data_find


# Make the Pool of workers
pool = ThreadPool(4) 

get_ret = pool.map(function_1, co_links.mass)
# #close the pool and wait for the work to finish 
pool.close() 
pool.join() 

print get_ret
# print len( co_links.mass )

# mergedlist = list(set(listone + listtwo))

# data = [{ 'a':'A'}]
# for x in xrange(1,10):
# 	# iter(data).next()['f'] = x
# 	data.append({'f':1})
# # for 1 in 1000:

# print data	


# co_data = cl_data(arg = co_links.mass)
# co_data.get_pars()

# def make_all(url):
# 	print x 
# 	# driver.quit()
# 	return x
    # html = get_html(url)
    # data = get_page_data(html)
    # write_csv(data)

# co_data.get_pars()
# pool = Pool(2)


# pool.map(make_all, co_data.data_links)  
    # driver.quit()
       # p.map(co_data.get_pars())






# if __name__ == '__main__':
    # main()
# print co_data.data_pars


=======
co_links.find_links(soup_find = co_links.get_adress(adress + '/minimal.html') )
co_links.set()

# print len( co_links.mass )

# mergedlist = list(set(listone + listtwo))

# data = [{ 'a':'A'}]
# for x in xrange(1,10):
# 	# iter(data).next()['f'] = x
# 	data.append({'f':1})
# # for 1 in 1000:

# print data	


co_data = cl_data(arg = co_links.mass)
co_data.get_pars()


print co_data.data_pars


>>>>>>> a3327700003f6c7e88d49ecccf04a88f684335dd
# ab = {}
# ab['Guido'] = 'guido@python.org','sdfsdf'
# ab['Guido'] = '34','34'
# print help(ab)
# mass = set(mass)

# mass =  sorted(mass, key=lambda student: student[0] , reverse=True)
# print CL_links.mass		
# print len(mass)

# pool.close()
# pool.join()
driver.quit()