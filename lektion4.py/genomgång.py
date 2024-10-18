import os 
## skapa ett verktyg som kan läsa,sktriva och söka i textfiler

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.readlines()
            for line in content:
                print(line.strip())
    else:
        print(f"file: {filename} does not exist")


def create_file():
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            print(f"File was created: {filename}")
    else:
        print(f"File already exists: {filename}")

def append_file():
    if os.path.exists(filename):
        with open(filename, "a"):
            filename.write("\n" + text)
        print(f"text was added to file {filename}")
    else:
        print(f"file was not found {filename}")

def search(filename, text):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                if text in line:
                    print(f"Theword {text} was found in line {i}")
            else:
                print(f"File not found: {filename}")



#main program

while True:
    print("meny: ")
    print("1. Read File")
    print("2. Create file")
    print("3. Append text to file")
    print("4. exit")

    choice = input("choose an option (1-4): ")

    if choice == "1":
        filename = input("enter file name: ")
        read_file(filename)
    elif choice == "2":
        file_name = input("enter file name: ")
        read_file(filename)
    elif choice == "3":
        file_name = input("enter file name: ")
        text = input("Enter text to append: ")
        append_file(filename, text)
    elif choice == "4":
        print("exiting program")
        break
    else:
        print("invalid choice")