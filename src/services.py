
import json
import random
from typing import Dict,List




def get_quotes()->List:
    with open('quotes.json') as quotes_file:
        data  = json.load(quotes_file)

    return data    

def get_random_quotes()->Dict:
    quotes = get_quotes()
    quote = random.choice(quotes)

    return quote


def form_tweet(quote:Dict[str,str])->str:
    author = quote['author'].strip(',')
    quote_text = quote['quote_text']
    genre = quote['genre']
    tweet = f'{quote_text} - {author}'
    return tweet


def is_valid(tweet:str)->bool:
    return len(tweet)<=200



def get_tweet():
    while True:
        quote = get_random_quotes()
        tweet = form_tweet(quote)
        if is_valid(tweet):
            return tweet
        
print(get_tweet())        




