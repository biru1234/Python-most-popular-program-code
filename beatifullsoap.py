from bs4 import BeautifulSoup as bs
import requests
import re

#url = 'https://www.w3schools.com/'
url = 'https://webscraper.io/test-sites'
page = requests.get(url)
html_content = page.content
beautify_html=bs(html_content,'html.parser')
title2=beautify_html.find('title')
print(title2.text)
link =beautify_html.findAll('a')
'''for temp_link in link:
    x=temp_link.get('href')
    if 'https' in x:
        #print(x)'''
paragraph=beautify_html.findAll('p')
for x in paragraph:
    y=x.text
    print(y.strip())
