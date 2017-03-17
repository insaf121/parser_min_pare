# print('hello')
# import lxml.html
from lxml.html import parse
from multiprocessing.dummy import Pool as ThreadPool
# import requests

# r = requests.get('http://www.minpairs.talktalk.net/minimal.html')
# tree = lxml.html.fromstring(r.text)
# print(r.text)

# # tree.xpath('//td') # все h2 теги
# tree.xpath('//td[@align]') # h2 теги с атрибутом align
# # tree.xpath('//h2[@align="center"]') # h2 теги с атрибутом align равным "center"

adress = 'http://www.minpairs.talktalk.net/'
page = parse(adress + 'minimal.html').getroot()

# /html/body/center[2]/table/tbody/tr[2]/td[10]/a

link = []
link_hrefs = []
min_par = []
for a in page.cssselect('table tr td a'):
	link.append(adress + a.get("href"))

# print(len(link) )	
link = list(dict.fromkeys(link)) #unic
print(len(link))
link = link[:9]


def get_pre(link):
	page2 = parse(link).getroot()
	temp = page2.cssselect("pre")
	if len( temp ) ==0 :
		temp = []
	return temp



# for row in link:
# 	# print()
# 	# /html/body/pre/text()
# 	page2 = parse(row).getroot()
# 	hrefs2 = page2.cssselect("pre")
# 	for x in xrange(1,10):
# 		pass
# 	print(hrefs2.text_content())
# 	break
	# if len(hrefs2) == 1:
	# 	print('1')
	# else:
	# 	print(len(hrefs2))
	# 	print(row)
	# 	sdfds


# Make the Pool of workers
pool = ThreadPool(8) 

link_hrefs = pool.map(get_pre, link)
# #close the pool and wait for the work to finish 
pool.close() 
pool.join() 

print( len( link_hrefs ))

for x in link_hrefs:
	for isk in x:
		min_par.append(isk.text_content())
		# print( isk.text_content )
		# break
print(min_par)		










	# for fte in hrefs2:
		# min_par.append(fte.text_content())

		# print(fte.text_content())

# print( len(min_par))	
	# break
# print(len(link) )	

		# print( a.getchildren() )
        # print(a.get("href"))

# namespace-prefix|element
# hrefs = page.cssselect("a")
# print( hrefs(html) )
# for x in td:
# 	# for inss in hrefs(x):
# 	print( x.getchildren() )
	# print( hrefs(x) )

	# break
		# print( inss )

# print( len(hrefs))
# print( lxml.html.tostring('http://www.minpairs.talktalk.net/minimal.html') )
# print( parse.tostring(page) )

# parse().getroot().cssselect()

# x = 0;
# print(hrefs)
# for row in hrefs:
# 	print(row.get("href"))

# for row in hrefs:
# 	# x += 1
# 	# print (x)d
# 	if (row.text_content()).isdigit() :
# 	# and int((row.text_content().encode('utf-8'))) >= 1200:
# 		# print (row.text_content())
# 		# print (row.get("href"))
# 		page2 = parse('http://www.minpairs.talktalk.net/'+ row.get("href")).getroot()
# 		hrefs2 = page2.cssselect("pre")
# 		for row2 in hrefs2:
# 			print (row2.text_content())
