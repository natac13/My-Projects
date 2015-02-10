

class Song(object):


    ## when being prompt as help to complete Song(....)
    ## 'lyrics' apears instead of 'object'
    ## therefore I see that whatever in in the __init__ spot
    ## is really what is required when inititing the class

    fy = 0
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
        
    def sing(self):
       for x in self.lyrics:
           print(x)
           
happy_bday = Song(["Happy birthday to you",
                   "I dont want to get sued",
                   "So I'll sto[ right there",])
                   
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


happy_bday.sing()

bulls_on_parade.sing()   

class Employee:
    empcount = 0
    x = 3
    
    
    def __init__(self, name):
        self.name = name
        ## seems that when written like this the Employee.empcount,
        # references back to the main class scope and not
        # the instance of the class
        Employee.empcount += 1


    def count(self):
        print("Total employee {0:d}".format(Employee.empcount))
    
    def display(self):
        print("Name is: {0}".format(self.name))

    def life(self):
        # then written like so means look at the object's scope
        self.x -=1
        
        
emp1 = Employee('rob')
emp2 = Employee('joanna')
emp1.display()
emp2.display()
print(Employee.empcount)

# so I can modify each objects x value since when life() is called it
# looks at the variables value from the objects scope
# When the variable had the class name in front instead of self,
# python then knows to look at the main class scope only, which
# would be like a clas as a module. Where ther is only one copy
# of it. That is why if I use class variables to make sure that are
# IMMUTABLE!!! meaning tey cant be modified! ie int, str, tuple only

    
