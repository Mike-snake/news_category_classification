from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['politics', 'Economic', 'social', 'Culture', 'world', 'IT']
df_titles = pd.DataFrame()

url = 'https://news.naver.com/section/100'
resp = requests.get(url)
print(resp)
print(list(resp))





