##Git hub Key

import requests
import json



fileName = "repos-private.json"
apiKey = "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" #my own token key 


url = 'https://github.com/Cossie01/Data-Representation-CourseWork' #my github respo

response = requests.get(url, auth= ('token', apiKey))
repoJSON =response.json()
print (response.status_code) #if 404 we are in trouble


with open(fileName, "w") as fp:
   # repoJSON =response.json()
    json.dump(repoJSON,fp, indent=4) #put it into the repojson file 