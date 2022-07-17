from typing import Text
from requests.models import Response
import tweepy
import matplotlib.pyplot as plt
import requests
import os
import json
import numpy as np
import sys
import csv
from twarc_csv import CSVConverter
import sys


#uncomment any code to test.

# Create these keys and tokens in your Twitter Developer account check #readme

consumer_key = "#"
consumer_secret = "#"
bearer_token = "#"
Access_token = "#"
Access_token_secret = "#"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_secret, consumer_key)

# Setting your access token and secret
auth.set_access_token(Access_token,Access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

def create_url():
    # Replace with user ID below
    user_id = 68382599
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at", "tweet.fields": "author_id","user.fields": "username",'max_results':'100',}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers



def connect_to_endpoint(url,headers,params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    headers =  create_headers (bearer_token)
  
    json_response = connect_to_endpoint(url, headers, params)
   # print(json.dumps(json_response, indent=4, sort_keys=True))


  
    with open("itumbi.json", "w") as f:
     json.dump(json_response, f, indent=4, sort_keys=True)

print("Finished crawling, saving json-file.")
if __name__ == "__main__":
    main()
