from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"I am gonna copy {from_file} to {to_file}")

#in_file=open(from_file)
#in_data=in_file.read()

#^tutto in un'unica riga
in_data = open(from_file).read()


print(f"The input file is {len(in_data)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Readt, hit RETURN to continue, press CTRL + C to abort")
input()
out_file = open(to_file, 'w')
out_file.write(in_data)

print("Fatto")

out_file.close()

