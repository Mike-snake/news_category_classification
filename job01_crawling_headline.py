from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['politics', 'Economic', 'social', 'Culture', 'world', 'IT']
df_titles = pd.DataFrame()

for i in range(6):

    url = 'https://news.naver.com/section/10{}'.format(i)

    resp = requests.get(url)
    #print(resp)

    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(list(soup))

    title_tags = soup.select('.sa_text_strong')  #컴머는 클래스 의미

    titles = []
    for tag in title_tags:
        titles.append(tag.text)                  #문자열만 출력

    print(titles)

    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles],
                          axis='rows', ignore_index=True)

#print(df_section_titles.head())
#df_section_titles.info() #정보 보여짐
df_titles.info()
print(df_titles['category'].value_counts())

df_titles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)