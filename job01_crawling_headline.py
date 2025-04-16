from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['politics', 'Economic', 'social', 'Culture', 'world', 'IT']
df_titles = pd.DataFrame()

url = 'https://news.naver.com/section/100'
resp = requests.get(url)
#print(resp)

soup = BeautifulSoup(resp.text, 'html.parser')
#print(list(soup))

title_tags = soup.select('.sa_text_strong')  #컴머는 클래스 의미
titles = []

for tag in title_tags:
    titles.append(tag.text)                  #문자열만 출력

print(titles)




