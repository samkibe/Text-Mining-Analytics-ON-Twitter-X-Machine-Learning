from twarc import Twarc2
from twarc_csv import CSVConverter
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="#")


def main():
       # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2021, 7, 10, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2021, 7, 16, 0, 0, 0, 0, datetime.timezone.utc)
   
    # This is where we specify our query as discussed in module 5
    query = "#Alshabaab OR Alshabaab OR shabaab OR Jihad OR Mujahidin OR mandera OR wajir OR #Garrissa) -is:retweet"

    # The search_recent method call the recent search endpoint to get Tweets based on the query, start and end times
    search_results = client.search_recent(
        query=query, max_results=100
    )

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # Here we are printing the recent Tweet object JSON to the console
        with open("Search.json", "w+") as f:
            f.write(json.dumps(page) + "\n")

    # Save the results as CSV
    with open("Search.json", "r", encoding="utf-8") as infile:
        with open("Search.csv", "w", encoding="utf-8") as outfile:
            converter = CSVConverter(infile, outfile)
            
            converter.process()

    print("Finished crawling, saving csv.")


if __name__ == "__main__":
    main()
