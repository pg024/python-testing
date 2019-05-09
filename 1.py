#First python script. 
#It reads a file passed as argument and prints the content.

from sys import argv

script, filename = argv

x = open(filename)

print(x.read())
x.close()

print("Do you want me to open it again?\nYes/No")
inp=input()
if (inp.lower() == 'yes'):
  x = open(filename)
  print(x.read())
  x.close()
elif (inp.lower() == 'no'):
  print("nothing to see here! Bye.")
else:
  print("Specify Yes or No, press Ctrl + C to abort")

  
