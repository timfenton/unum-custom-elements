import os
import csv 
import json
import time
from pathlib import Path
from itertools import groupby

def csv_to_json(csv_path,json_path):
    jsonArray = []
    tempArray = []
      
    #read csv file
    with open(csv_path, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            tempArray.append(row)

    tempArray = sorted(tempArray, key=key_on_event_func)

    for key, value in groupby(tempArray, key_on_event_func):
        jsonArray.append({key: list(value)})
        
  
    #convert python jsonArray to JSON String and write to file
    with open(json_path, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def key_on_event_func(k):
    return k['Event_Name']

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(CUR_PATH + '/data/segment-event-data.csv')
json_path = os.path.join(CUR_PATH + '/data/segment-event-data.json')

start = time.perf_counter()
csv_to_json(csv_path,json_path)
finish = time.perf_counter()

print(f"Conversion 100.000 rows completed successfully in {finish - start:0.4f} seconds")