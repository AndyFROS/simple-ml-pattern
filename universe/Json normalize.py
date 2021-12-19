import json
import glob
import pandas as pd

#Reading json documents
q = pd.read_json('data.json')

#Parsing values ​​from json to DataFrame (df)
_list=[]  #Making a list for all data from json files
for filename in glob.glob("data/*.json"): #Loop through all files
    with open(filename, encoding='utf-8-sig') as json_data:  #Opening each file in turn
        data = json.load(json_data)#Download the file and place it in the data variable
        #Normalize (we bring them to an acceptable form for further work through pandas) files and add them to the list
        _list.append(pd.json_normalize(data, record_path=['firstLvl', 'SecondLvl', 'ThirdLvl'], 
            meta=[
            ['firstLvl', 'SecondLvl', 'Your meta']], errors='ignore'))
        
df=pd.concat(_list) #Combine (concatenate) all the list in one date frame