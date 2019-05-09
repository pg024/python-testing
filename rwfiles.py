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
line1 = input("1st line:")
line2 = input("2nd line:")
line3 = input("3rd line:")
 
print("Adding the lines..")
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")

print("Reading file:")
print(file.read())

print("Closing it, bye!")
file.close()
       
  
