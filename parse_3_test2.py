# print('hello')
from lxml.html import parse
# page = parse('http://www.minpairs.talktalk.net/minimal.html').getroot()
# hrefs = page.cssselect("a")
# x = 0;
# print(hrefs)
# for row in hrefs:
# 	print(row.get("href"))

# tree = parse.fromstring('http://www.minpairs.talktalk.net/minimal.html')
tree = parse('http://www.minpairs.talktalk.net/minimal.html').getroot()
# tree.xpath('//td') # все h2 теги
tree.xpath('//td[@align]') # h2 теги с атрибутом align
# tree.xpath('//h2[@align="center"]') # h2 теги с атрибутом align равным "center"

# print( tree.text_content() )

# div_node = tree.xpath('//div')[0] # div тег
# div_node.xpath('.//h2') # все h2 теги, которые являются дочерними div ноде

# /html/body/center[1]/table/tbody/tr[2]/td[3]/a
for row in tree:
	print (row.get("href"))
	# print( row )
	# for x in row:
		# print(x)

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
