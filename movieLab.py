from random import *
def randomMovies():
    lst1 = ["Adventures of", "My name is", "Hello, ","The Journey of", "The Mystery of", "The Only ","The All Star","The Amazing", "White Eyes Blue ", "The "]
    lst3 = ["Spiderman","Sherlock Holmes", "Flash" "Batman","Wolverine", "John Wayne", "Computer Program", "SuperMan", "Megaman", "Google", "Code"]
    lst2 = [" The Amazing ", " The Real " ," The Wanted " ," The First "," The Second "," The Great ", " The Big Bad ", " The Good ", " The Awesome ", " The Weak "]
    lst4 = []
    for i in range(10):
       first = lst1[randrange(len(lst1))]
       second = lst2[randrange(len(lst1))]
       third = lst3[randrange(len(lst1))]
       if len(lst4) > 0:
        for i in lst4:
            if i == (first + second + third):
                print("already exist!")
            else:
                print("new item")
                lst4.append(first + second + third)
       else:
        print("somethingnew")
        lst4.append(first + second + third)
    print(lst4)
 
randomMovies()