
import bs4 as _bs4
import requests as _request
import constants
import json


def create_url(tag:str)->str:
    
    return f'https://www.goodreads.com/quotes/tag/{tag}'


def get_page(url:str)->_bs4.BeautifulSoup:
    page =_request.get(url)
    soup = _bs4.BeautifulSoup(page.content,'html.parser')

    return soup

def exctract_quote_and_author(quote):
    quote_text = quote.contents[0].strip()
    author = quote.find(class_='authorOrTitle').text.strip()

    return quote_text, author

def scrap_quotes():
    collections = list() 
    for tag in constants.TAGS:
        url = create_url(tag)
        soup = get_page(url)
        raw_quote = soup.find_all(class_='quoteText')
        for quote in raw_quote:
            quote_text,author = exctract_quote_and_author(quote)
            data = {
                'author':author,
                'quote_text':quote_text,
                'genre':tag
            }
            collections.append(data)

    return collections    

# print(scrap_quotes())    


if __name__=='__main__':
    quotes = scrap_quotes()
    with open('quotes.json','w') as f:
        json.dump(quotes,f,ensure_ascii=False)


