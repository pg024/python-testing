#First python script. 
#It reads a file passed as argument and prints the content.

from sys import argv

script, filename = argv

def print_ask(f):
 print("Do you want me to open it again?\n")
 inp=input("Yes/No?")
 if (inp.lower() == 'yes'):
  print(x.read())
  x.close()
 elif (inp.lower() == 'no'):
  print("nothing to see here! Bye.")
  x.close()
 else:
  print("Specify Yes or No, press Ctrl + C to abort")
  return print_ask(f)


x = open(filename)

print(x.read())
x.close()
x = open(filename)
print_ask(x)
