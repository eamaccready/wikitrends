from urllib2 import urlopen
from json import load 
import pandas as pd
import datetime


url='https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/Donald_Trump/daily/20130101/20160401'
response = urlopen(url) 
json_obj = load(response) #-- loads the result into the python data object 
j=pd.DataFrame(json_obj['items'])
j['date']=pd.to_datetime(j["timestamp"],format="%Y%M%d00")
print j[0:8]
