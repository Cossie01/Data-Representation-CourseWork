
from github import Github
from config import config as cfg

from github.MainClass import Github




apikey = cfg["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"]

g = Github(apikey)
for repo in g.get_user().get_repos():
 print(repo.name)


g = Github(apikey)
repo = g.get_repo("yourccount/yourrepo")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)


