html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

data_foo = '<div data-foo="value">foo!</div>'

from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup)
# print(dir(soup))
# print(soup.title)
# print(soup.title.get_text())
# print(soup.find_all())
# print(soup.find())
# print(soup.find_all('a'))

# a_tags = soup.find_all('a')
# a_tags = soup.find_all('a', id='link1')

# a_tags = soup.find_all('a', class_='sister')
# for tag in a_tags:
#     # print(tag)
#     # print(tag.get_text())
#     print(tag.attrs['href'])

# soup = BeautifulSoup(data_foo, 'html.parser')
# a_tags = soup.find_all('a', class_='sister')
# a_tags = soup.find_all('div', {'data-foo': 'value'})
# # print(a_tags)
# for tag in a_tags:
#     print(tag.attrs['data-foo'])
soup = BeautifulSoup(html_doc, 'html.parser')
tag = soup.select('.sister')
print(tag)