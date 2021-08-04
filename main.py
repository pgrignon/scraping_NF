import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import pprint
import sqlalchemy


url = 'https://noirfonce.eu/collections/sneakers'



def get_article_price(article):
    price = article.find(class_="grid-product__price").get_text().replace("\n","").replace("€","")
    if len(price.split("Sale price"))>1:
        return float(price.split("Sale price")[1])
    else:
        return float(price)

def get_article_name(article):
    return article.find(class_="grid-product__title grid-product__title--body").get_text()

def get_article_href(article):
    return article.find("a").get('href')

def get_articles():
    """
    Get the articles from the front page of the blog
    """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.findAll(class_="grid-product__content")
    names = []
    prices = []
    href = []
    for article in articles:
        print(get_article_price(article))
        names.append(get_article_name(article))
        prices.append(get_article_price(article))
        href.append(get_article_href(article))
    
    pprint.pprint(names)
    return pd.DataFrame({"Name":names, "Price":prices, "Ref":href})

def connect_sql_alchemy():
    database_username = 'paul'
    database_password = 'motdepasse'
    database_ip       = 'localhost'
    database_name     = 'NF'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))
    return database_connection

def write_articles_to_sql(df, con, table):
    return df.to_sql(con=con, name=table, if_exists="replace")


if __name__ == '__main__':
    articles = get_articles()
    pprint.pprint(articles)
    # con = connect_sql_alchemy()
    # print(con)
    # write_articles_to_sql(articles, con, "articles")