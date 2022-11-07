from urllib import response
import requests #import package
import json
url= "http://andrewbeatty1.pythonanywhere.com/books" #the link

def getAllBooks(): #function to get all the book information from the website. 
    response = requests.get(url)
    return response.json()

def getBookById(id): #function for get books by id
    geturl = url + "/" +str(id)
    response = requests.get(geturl)
    return response.json() 

def createBook(book):
    
    response = requests.post(url, json=book)
    return response.json()

def deleteBook(id):
    geturl = url + "/" +str(id)
    response = requests.delete(geturl)
    return response.json() 

def updateBook(id, bookdiff):
    updateurl = url + "/" +str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()
    pass
    

if __name__=="__main__":
    #print(getAllBooks())
    #print(getBookById(181))
    #print(deleteBook(219))
    #book ={
        #'Author':"Test",
        #'Title': "TT",
        #'Price': "123"
    #}
    #print (createBook(book))
    bookdiff = {
    
        'Price': 1000000
    }
    print(updateBook(218, bookdiff))