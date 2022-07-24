from sys import argv


script, filename = argv

print(f"We are going to clean the file {filename}")
print("Are you ok with it? Ctrl+C to exit")
input("?")

print(f"Opening file {filename}")
file = open(filename, 'w')
print("Cleaning file")
file.truncate()

print("What do you want to write there?")
text = input("> ")

file.write(text)
print("Done. Closing the file")

file.close()
