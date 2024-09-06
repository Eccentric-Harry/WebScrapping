import asyncio
from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint

MINIMUM_TWEETS = 20;
QUERY = '(Floods OR #naturaldisaster OR earthquake OR tsunami OR firefighters OR landslide OR #floods  OR "Natural Disaster") lang:en'

async def get_tweets(client, tweets):
    if tweets is None:
        print(f'{datetime.now()} - Getting tweets...')
        tweets = await client.search_tweet(QUERY, product='Top')
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds ...')
        await asyncio.sleep(wait_time)
        tweets = await tweets.next()

    return tweets

async def main():
    #* login credentials
    config = ConfigParser()
    config.read('config.ini')
    username = config['X']['username']
    email = config['X']['email']
    password = config['X']['password']

    #* create a csv file
    with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tweet_count', 'Username', 'Text', 'Created At', 'Retweets', 'Likes', 'Image'])

    #* authenticate to X.com
    client = Client(language='en-US')
    client.load_cookies('cookies.json')  

    tweet_count = 0
    tweets = None

    while tweet_count < MINIMUM_TWEETS:
        try:
            tweets = await get_tweets(client, tweets)
        except TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
            wait_time = rate_limit_reset - datetime.now()
            await asyncio.sleep(wait_time.total_seconds())
            continue

        if not tweets:
            print(f'{datetime.now()} - No more tweets found')
            break

        for tweet in tweets:
            tweet_count += 1
            tweet_data = [tweet_count, tweet.user.name, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count]

            with open('tweets.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(tweet_data)

        print(f'{datetime.now()} - Got {tweet_count} tweets')

    print(f'{datetime.now()} - Done! Got {tweet_count} tweets found')

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())