import requests
from bs4 import BeautifulSoup
import settings


# url = settings.BASE_URL.format('python')
# response = requests.get(url)python

def pars_content(content):
    soup = BeautifulSoup(content, 'html.parser')

    boxes = soup.find_all('article', class_='box')
    print(boxes)
    print(len(boxes))

if __name__ == '__main__':
    for name in settings.PAGES_NAMES:
        url = settings.BASE_URL.format(name)
        response = requests.get(url)
        pars_content(response.content)

# print(response.content[:1000])
# print(response)
# print(dir(response))
