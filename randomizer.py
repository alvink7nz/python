from random import *

elements = input("enter elements")
listelements = elements.split(", ")
randomnum = randint(0, len(listelements))
randomelement = listelements[randomnum]
print(randomelement)