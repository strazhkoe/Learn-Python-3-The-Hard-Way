from sys import argv

script, username = argv
prompt = '> '

print(f"Hello, {username}! My name is {script}")
print(f"Do you like me?")
like = input(prompt);

print(f"Where do you live, {username}")
live = input(prompt)

print(f"""
So you said {like} about me
And you live in {live}
""")

