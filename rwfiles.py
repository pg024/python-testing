from sys import argv 

script, filename = argv
 
print(f"We're going to erase {filename}")
print("If you don't want to, hit CTRL-C (^C).")
print("If you agree, hit RETURN")
 
input("?")
 
print("Opening the file")
file = open(filename, 'w')
 
print("Truncating file")
file.truncate()
       
print("Now I am going to ask you to 3 lines to be added")
line = input("1st line:") + " " + input("2nd line:") + " " + input("3rd line:")

print("Adding the lines..")
file.write(line)


file.close()
file = open(filename)

print("Reading file:")
print(file.read())

print("Closing it, bye!")
file.close()
       
       
  
  
