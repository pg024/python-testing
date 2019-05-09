#First python script. 
#It reads a file passed as argument and prints the content.

from sys import argv

script, filename = argv

x = open(filename)

print(x.read())
x.close()

print("Bye!")
