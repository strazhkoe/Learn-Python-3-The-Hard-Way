from genericpath import exists
from sys import argv


scriptname, from_file_name, to_file_name = argv

print(f"Copying {from_file_name} to {to_file_name}")


print(f"{to_file_name} exists? {exists(to_file_name)}")

input("Enter to proceed, Ctrl+C to abort");

from_file = open(from_file_name)
from_file_content = from_file.read()

to_file = open(to_file_name, "w")
to_file.write(from_file_content)

print("Done")

from_file.close()
to_file.close()

