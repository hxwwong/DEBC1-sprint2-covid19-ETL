import requests
import bs4
import lxml
import pandas as pd

link = 'https://www.rappler.com/topic/covid-19-fact-checks/page/'
page = 1

def html(url):
    try:
        soup = bs4.BeautifulSoup(requests.get(url).text,'lxml')
        return soup
    except Exception as e:
        print(e)
        print("Not loading")

#get maximum page
while True:
    test = link + str(page)
    if requests.get(test).status_code != 404:
        page += 1
    else:
        print("maximum page reached:", page-1)
        break

#compile articles into dictionary
article_ls = []
for i in range(1, page):
    soup = html(link + str(i))
    articles = soup.find_all('div', class_='archive-article__content')
    for article in articles:
        try:
            headline = article.find('h2').text.strip()
            
            url = article.find('a').get('href')

            date = article.find('time').text.strip()

            #Compile article features into dictionary
            article_ls.append({'headline': headline, 'url': url, 'date':date, 'source':'rappler'})
        except:
            continue

#convert to dataframe
df = pd.DataFrame(article_ls)
#convert object type date to date format
df['date'] = pd.to_datetime(df['date'].str.replace(' PHT', ''))