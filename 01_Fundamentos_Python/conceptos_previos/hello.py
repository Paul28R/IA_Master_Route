# import the argparse package
import argparse

# Trigger a string output from the terminal
print('Hello from the command line!')

# Instantiate the argparse package.
parser = argparse.ArgumentParser() # description='A friendly greeting script.'
# Create an argument called name.
# --name (con guiones) el argumento deja de ser posicional y se convierte en opcional
parser.add_argument("--name", help="Creates a new name.")
args = parser.parse_args()

# Output the name within the terminal upon calling the argument.
if args.name:
    print(f"My name is {args.name}.")
else:
    print("Hello, stranger!")


