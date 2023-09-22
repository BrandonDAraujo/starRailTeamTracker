import requests
 
# Making a GET request
r = requests.get('https://game8.co/games/Honkai-Star-Rail')
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)