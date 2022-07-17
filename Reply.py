import tweepy
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from twarc_csv import CSVConverter
import sys
import pandas as pd
from flask import request


consumer_key = "E5WnkW6QdXoxMiAhafIFcae7v "
consumer_secret = "HkIJvaOJtQH70o5NldTEOEDjMBMmb4PQgOt5ffFtYg67WFgbhU"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMKsRAEAAAAAVFeFz0lmnSQK2QAdFqJR7xvRjfI%3DzOAQC4dT1CnQR7XEAybZTC1VX1gPmGyYvz4kuWHlKrUHXeNRmI"
Access_token = "2861228630-A5Zq9I81jo2MLq5Fo9sarry9t46m3yAcIGwpXQJ"
Access_token_secret = " pbroGrEQBZKS1qNqspxxitFeMIau17GKTq9qzvAsdbm0Z"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_secret, consumer_key)

# Setting your access token and secret
auth.set_access_token(Access_token,Access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 



search_url = "https://api.twitter.com/2/tweets/search/recent?"

query_params = {  'query': '#Alshabaab (Alshabaab OR shabaab OR Jihad OR Mujahidin OR mandera OR wajir -is:retweet) OR #Garrissa ', 
'tweet.fields':   'author_id','expansions' : 'in_reply_to_user_id', }


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))




if __name__ == "__main__":
    main()


print("Finished crawling, saving csv.")