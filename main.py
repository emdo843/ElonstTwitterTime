import aiohttp
from aiohttp import client
from aiohttp import ClientSession
import asyncio
import sys
import io
import os
import copy
import pytz
from dotenv import load_dotenv

#loads and saves bearer token as a str from .env
load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')
ID = '44196397'

#collects all liked tweets since a given time
def get_likes():
    url = f'https://api.twitter.com/2/users/{ID}/liked_tweets'


#generates headers
def create_headers():
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

#fetches a response for a given url
async def connect_to_endpoint(url):
    async with client.mysession.get(url, headers=create_headers()) as resp:
        resp.raise_for_status()
        if resp.status != 200:
            raise Exception(f"Request returned an error: {resp.status}" )
        if resp.status == 400:
            raise Exception(f"Request returned an error - Bad Request")
        return await resp.json()



if __name__ == '__main__':
    pass