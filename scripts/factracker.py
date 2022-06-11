import requests
import bs4
import lxml
import pandas as pd

def html(url):
    try:
        soup = bs4.BeautifulSoup(requests.get(url).text,'lxml')
        return soup
    except Exception as e:
        print(e)
        print("Not loading")

link = 'https://www.factrakers.org/search-results?q=Covid&type=blogs&page='
page = 1
article_ls = []

while True:
    current_url = link+str(page)
    soup = html(current_url)
    
    #identify articles in each page
    articles = soup.find_all('div', class_='ssmoxN')
    #get article features
    for article in articles:

        headline = article.find('a').get('title')

        url2 = article.find('a').get('href')

        soup2 = html(url2)
        date = soup2.find('span', {'class': 'post-metadata__date time-ago'}).text.strip()
        
        #compile article features into dictionary
        article_ls.append({'headline': headline, 'url': url2, 'date': date, 'source': 'factrakers'})

    #identify maximum page
    if soup.find('a', {'data-hook': 'next'}).get('aria-disabled') == 'false':
        page += 1     
    else:
        print('maximum page reached:', page)
        break
#convert to dataframe
df = pd.DataFrame(article_ls)
#export data frame
df.to_csv('Factraker_results.csv')
