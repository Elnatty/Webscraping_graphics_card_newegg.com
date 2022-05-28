import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

'''
--->> BeautifulSoup parses the html, and Urllib grabs the web page...
--->> site to beautify html code... https://beautifier.io/
'''

# url link.
# apparently there are 100 pages available.
page_number = str(input('input web page number: '))
# page_number = str(range(1, 100))
my_url = 'https://www.newegg.com/p/pl?d=graphics+cards&page='+page_number
# open up connection, grabbing the page and store raw html content into a variable.
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parsing with beautiful soup
page_soup = soup(page_html, 'html.parser')

# using the findAll method
containers = page_soup.findAll('div', {'class':'item-container'})
# index item/container that houses what we need
# container2 = containers[2]
# our loop, structured from line 15.

# saving content to a file
cur = os.path.join('C:/Users', 'test')
ch = os.chdir(cur)
filename = 'web_scrap.txt'
mf = open(filename, 'a')        # change to 'w' at 1st for write

for container in containers:
    # try:
        # 1: graphics card brand
        graphics_name = container.find('div', {'class':'item-info'}).find('a', {'class':'item-title'}).text


        # 2: graphics card make
        # gra_title = container.find('div', {'class': 'item-branding'})
        # if gra_title:
        #     graphics_make = gra_title.a.img['title']
        # else:
        #     graphics_make = 'null...'
        # print('Card Make: ', graphics_make)

        # 3: graphics card price
        gra_price = container.find('div', {'class': 'item-action'})
        if gra_price:
            graphics_price = gra_price.ul.find('li', {'class': 'price-current'}).text
        else:
            graphics_price = 'null price...'

        # print('Card Name: ', graphics_name)
        # print(graphics_price)
        # print('')
    # except TypeError as e:
        # print('no info...')

        # saving info to a file.
        mf.writelines(f'Card Names: {graphics_name}\nCard Prices: {graphics_price}\n\n')
mf.close()