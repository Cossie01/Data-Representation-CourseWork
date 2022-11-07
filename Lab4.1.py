from Lab4 import getAllBooks #importing the other program


books = getAllBooks() #naming the variable as the function from the other program
total = 0
count = 0

for book in books:
    total += book["Price"] 
    count +=1
print("Average of ", count, "books is " , total/count) #printing the average. 