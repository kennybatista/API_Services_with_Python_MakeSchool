from lxml import html

import requests

page = requests.get("https://www.makeschool.com/students")
tree = html.fromstring(page.content)

# this will create a list of buyers
names = tree.xpath('//p[@class="head"]/text()')
bio = tree.xpath('//p[@class="mt2"]/text()')

print 'Names: ', names
# print 'Bio: ', bio
