from urllib2 import urlopen
from json import load 
import pandas as pd
import datetime

#buliding URL:

#article for which page views need to be extracted
look_up="Donald_Trump"

#dates between which page views need to be extracted in the format YYYYMMDD
startdate="20130101"
enddate="20160401"

#request URL : https://wikimedia.org/api/rest_v1/?doc
url='https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/'+look_up+'/daily/'+startdate+'/'+enddate

response = urlopen(url) 

#parses the json response and creates a dictionary with key "list" and value of a  list of dictionaries where each dictionary is a day's page view data
json_obj = load(response) 

#extacting just the list of dictionaries and creating a data frame
data=pd.DataFrame(json_obj['items'])

#data cleaning begins

#step 1 : manipulate the timestamp to create a date attribute
data['date']=pd.to_datetime(data["timestamp"],format="%Y%M%d00")


print data[0:8]
