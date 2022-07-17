 
 
import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('retweet.json') as json_file:
    data = json.load(json_file)
 
bytime_data = data['data']
 
# now we will open a file for writing
data_file = open('retweet.csv', 'w', encoding="utf-8")
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for emp in bytime_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(emp.values())
    print("Finished crawling, saving csv-file.")
data_file.close()

