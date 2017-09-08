import requests
import os


# payload = {'token' : os.environ["OAUTHTOKEN"]}
# url = "https://www.eventbriteapi.com/v3/categories"


# response = requests.get(url,params=payload)

# data = response.json()

# print data




payload = {'token' : os.environ["OAUTHTOKEN"], 'q':"macaron", }

url = "https://www.eventbriteapi.com/v3/events/search/?"


response = requests.get(url,params=payload)

data = response.json()

print data