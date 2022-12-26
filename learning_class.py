# class Person:
#     name=""
#     age=""

# aditya=Person()
# aditya.name="Aditya"
# aditya.age="20"

# print(aditya.name,aditya.age)


# class Furniture:
#     color=""
#     material=""


# table=Furniture()
# table.color="red"
# table.material="wood"

# couch=Furniture()
# couch.color="brown"
# couch.material="foam"

# print(f'this Furniture is of color {table.color} and material {table.material}')
# print("this Furniture is of color {color} and material {material}".format(color=couch.color,material=couch.material))

# class Years:
#     year=0
#     def dog_years(self):
#         return "Years for human {}, Years for dogs {}".format(self.year, self.year*7)

# doggy=Years()
# doggy.year=3
# print(doggy.dog_years())


''' CONTRUCTOR AND SPECIAL METHODS'''
# class Apple:
#     def __init__(self,colour,flavour):               #constructor function for Apple class 
#         self.colour=colour
#         self.flavour=flavour

#     def __str__(self):                               #special method to return something if only object of apple class prints 
#         return "this is Apple , its colour is {} and its flavor is {}".format(self.colour,self.flavour)


# fruit=Apple("red","sweet")
# print(fruit.colour)
# print(fruit)



# class Pet:
#     def __init__(self,name,colour):
#         self.name=name
#         self.colour=colour

#     def Pet_name(self):
#         '''This is a docstring whioch is for documentation of your code this will also show when someone use help for this class , and u can write only one Docstring for one method so keep it simple like this :  this method returns the information about pet it got'''
#         return f'Pets name is {self.name} and its colour is{self.colour}'

# dog=Pet("doggo","black")
# print(dog.Pet_name())

# help(Pet)




# '''inheritance'''
# class Clothing:
#   material = ""
#   def __init__(self,name):
#     self.name = name
#   def checkmaterial(self):
# 	  print("This {} is made of {}".format(self.name,self.material))
			
# class Shirt(Clothing):          # inherits Clothing class , child classes use contructor of parent classes here shirt class using contructor 
#   material="Cotton"              #of Clothing class

# polo = Shirt("Polo")
# polo.checkmaterial()



'''composition'''
'''when 2 classes does not have any inheritance between they are related.
 EXAMPLE : if there is package class consist of software packages and repository class consist of all packages ready for installation . while there is no inheritance but still they are related 
 In the constructor method, we initialize the packages dictionary, which will contain the package objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every instance of the Repository class has its own dictionary.'''