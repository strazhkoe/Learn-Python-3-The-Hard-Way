from sys import argv


script, filename = argv

txt = open(filename)

print(f"Here is your file {filename}")
print(txt.read())

txt.close()

print("type file name to read:")
filename = input('> ')

txt = open(filename)
print(f"Here is a text: {txt.read()}")

txt.close()