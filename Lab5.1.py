import requests
import urllib.parse
from htmlconfig import config as cfg #importing the correct packages

targetUrl = "https://en.wikipedia.org" #the attended website to change to pdf

apiKey = cfg["htmltopdfkey"] #setting up the key 


apiurl = 'https://api.html2pdf.app/v1/generate' 
params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams
response = requests.get(requestUrl)
print (response.status_code)
result =response.content



with open("document.pdf", "wb") as handler:
    handler.write(result)
