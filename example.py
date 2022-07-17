from typing import Text
from requests.models import Response
import tweepy

import requests

import json

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

#public_tweets = api.home_timeline()
# foreach through all tweets pulled
#for tweet in public_tweets:
   # printing the text stored inside the tweet object
   #print (tweet.text)
#status = "Testing!"
#api.update_status(status=status)

search_url = "https://api.twitter.com/2/tweets/search/recent?"
#query_params = {  'query': '#Alshabaab (Alshabaab OR shabaab OR Jihad OR Mujahidin OR mandera OR wajir -is:retweet) OR #Garrissa ', 
#'tweet.fields':   'author_id', }

#Use your on topic of interest or Keywords or Lexicons at #HERE

query_params = {  'query': '#HERE ( -is:retweet)', 
'tweet.fields':   'author_id', 'tweet.fields': 'created_at', 'max_results':'100', }

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
  
   # print(json.dumps(json_response, indent=4, sort_keys=True))
#output_file = json.dumps
  
    with open("example.json", "w") as f:
     json.dump(json_response, f, indent=4, sort_keys=True)


if __name__ == "__main__":
   main()
   print("Finished crawling, saving json-file.")

