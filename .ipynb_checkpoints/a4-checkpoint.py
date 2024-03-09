# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883
#from Profile import *


from pathlib import Path
import os
from Profile import Profile, Post
from ui import printDirectories, outputFiles, searchFile, outputFileExtension, deleteFile, readFile, commandC, commandO, commandE, commandP, allprofile, allposts
from ds_client import send

def printIntro():
    print()
    print("[COMMAND] [DIRECTORY] [[-]OPTION] [INPUT]")
    print("L: List directory contents")
    print("    -r: prints directory and files")
    print("    -f: prints files only in directory")
    print("    -s: searches directory by file name")
    print("    -e: searches directory by extension")
    print()
    print("C: Create a dsu file")
    print("    -n: allows you to name the file")
    print("(Example: C TestFolder/ -n myjournal)")
    print()
    print("[COMMAND] [PATH]")
    print("D: Delete a dsu file")
    print()
    print("R: Read a dsu file")
    print()
    print("O: Open a dsu file")
    print("(Example: O TestFolder/myjournal.dsu)")
    print()
    print("Q: Quit the program\n")


def printEP():
    print("[COMMAND] [[-]OPTION] [INPUT]...")
    print("Note: Make sure to include the '-' sign!")
    print("Commands (E or P)-----------")
    print(" E: Edit profile content(s)")
    print("   Options & Input:")
    print('   [-usr] ["USERNAME"]')
    print('   [-pwd] ["PASSWORD"]')
    print('   [-bio] ["BIO"]')
    print('   [-addpost] ["NEW POST"]')
    print("   [-delpost] [ID#]")
    print()
    print("[COMMAND] [[-]OPTION]")
    print(" P: Print profile content")
    print("   -usr")
    print("   -pwd")
    print("   -bio")
    print("   -posts")
    print("   -post [ID#]")
    print("   -all")
    print()


def run():
    printIntro()
    userinput = input("What would you like to do?\n")
    inputlist = userinput.split(" ")
    commandList = ["admin", "Q", "L", "C", "D", "R", "O", "E", "P"]
    command = inputlist[0]

    if command in commandList:
        if command == "Q":
            print("\nThank you, goodbye.\n")

        elif command == "L":
            directory = inputlist[1]
            nextCommand = inputlist[2]
            if nextCommand == "-r":
                if len(inputlist) > 3:
                    if inputlist[-1] == "-f":
                        print("rf")
                    elif inputlist[-1] == "-s":
                        print("rs")
                    elif inputlist[-1] == "-e":
                        print("re")
                elif len(inputlist) == 3:
                    printDirectories(directory)

            elif nextCommand == "-f":
                outputFiles(directory)

            elif nextCommand == "-s":
                filename = inputlist[3]
                searchFile(directory, filename)

            elif nextCommand == "-e":
                extension = inputlist[3]
                outputFileExtension(directory, extension)

        elif command == "D":
            directory = inputlist[1]
            try:
                deleteFile(inputlist[1])
            except FileNotFoundError:
                print("ERROR. Please use an existing file.")
            except ValueError:
                print("ERROR. File does not end in .dsu")

        elif command == "R":
            directory = inputlist[1]
            try:
                readFile(directory)
            except FileNotFoundError:
                print("ERROR. Please use an existing file.")
            except ValueError:
                print("ERROR. File does not end in .dsu")

        elif command == "C":
            if inputlist[2] == "-n":
                pathString = commandC(inputlist[1], inputlist[3])
                print(inputlist[1] + inputlist[3] + ".dsu created.\n")
                print("Profile saved.")
                print("\nWant to edit or print your profile? (y/n)")
                get_input = input()
                print()
                if get_input == "y":
                    printEP()
                    cmdLineEP = input("Please enter a command beginning with E or P.\n")
                    cmdEP = cmdLineEP.split(' ')
                    cmd1 = cmdEP[0]
                    if cmd1 == "E":
                        commandE(cmdLineEP, pathString)
                    elif cmd1 == "P":
                        commandP(cmdLineEp, pathString)
                elif get_input != "y":
                    print("Thank you.")

        elif command == "O":
            pathString = inputlist[1]
            if pathString.endswith(".dsu") is True:
                commandO(pathString)
                print("\nWant to edit or print your profile? (y/n)")
                get_input = input()

                if get_input == "y":
                    printEP()
                    print("Please enter your command.")
                    cmdLineEP = input()
                    print()
                    cmdEP = cmdLineEP.split(' ')
                    cmd1 = cmdEP[0]
                    if cmd1 == "E":
                        commandE(cmdLineEP, pathString)
                    elif cmd1 == "P":
                        commandP(cmdLineEP, pathString)
                    else:
                        print("Error. Begin command with E or P.")
                elif get_input != "y":
                    print("Thank you. Goodbye.")
            elif pathString.endswith(".dsu") is False:
                print("Error. Please enter a .dsu file.")

        if command == "admin":
            print()
            print("ADMIN MODE:")
            userinput = input()
            inputlist = userinput.split(" ")
            commandList = ["admin", "Q", "L", "C", "D", "R", "O", "E", "P"]
            command = inputlist[0]

            if command in commandList:
                if command == "Q":
                    print("Quit.")

                elif command == "L":
                    directory = inputlist[1]
                    nextCommand = inputlist[2]
                    if nextCommand == "-r":
                        if len(inputlist) > 3:
                            if inputlist[-1] == "-f":
                                print("rf")
                            elif inputlist[-1] == "-s":
                                print("rs")
                            elif inputlist[-1] == "-e":
                                print("re")
                        elif len(inputlist) == 3:
                            printDirectories(directory)

                    elif nextCommand == "-f":
                        outputFiles(directory)

                    elif nextCommand == "-s":
                        filename = inputlist[3]
                        searchFile(directory, filename)

                    elif nextCommand == "-e":
                        extension = inputlist[3]
                        outputFileExtension(directory, extension)

                elif command == "D":
                    directory = inputlist[1]
                    try:
                        deleteFile(inputlist[1])
                    except FileNotFoundError:
                        print("ERROR. Please use an existing file.")
                    except ValueError:
                        print("ERROR. File does not end in .dsu")

                elif command == "R":
                    directory = inputlist[1]
                    try:
                        readFile(directory)
                    except FileNotFoundError:
                        print("ERROR. Please use an existing file.")
                    except ValueError:
                        print("ERROR. File does not end in .dsu")

                elif command == "C":
                    if inputlist[2] == "-n":
                        pathString = commandC(inputlist[1], inputlist[3])
                        print(inputlist[1] + inputlist[3] + ".dsu created.\n")
                        print("Profile saved.")
                        print("y/n")
                        print()
                        get_input = input()
                        if get_input == "y":
                            allprofile(pathString)
                            cmdLineEP = input()
                            cmdEP = cmdLineEP.split(' ')
                            cmd1 = cmdEP[0]
                            if cmd1 == "E":
                                commandE(cmdLineEP, pathString)
                            elif cmd1 == "P":
                                commandP(cmdLineEp, pathString)
                        elif get_input != "y":
                            print("Exit.")

                elif command == "O":
                    pathString = inputlist[1]
                    if pathString.endswith(".dsu") is True:
                        commandO(pathString)
                        print("y/n")
                        get_input = input()

                        if get_input == "y":
                            print("Command:")
                            cmdLineEP = input()
                            print()
                            cmdEP = cmdLineEP.split(' ')
                            cmd1 = cmdEP[0]
                            if cmd1 == "E":
                                commandE(cmdLineEP, pathString)
                            elif cmd1 == "P":
                                commandP(cmdLineEP, pathString)

                        elif get_input != "y":
                            print("Thank you. Goodbye.")
                    elif pathString.endswith(".dsu") is False:
                        print("Error. Please enter a .dsu file.")

            elif command not in commandList and command != "admin":
                print("Invalid command. Please try again.")

    elif command not in commandList and command != "admin":
        print("Invalid command. Please try again.")

def main() -> None:
    zip = "92697"
    ccode = "US"
    apikey = "6af88070b5ade9132807d7d1f4b861a5"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj['weather'][0]['description'])


if __name__ == '__main__':
    run
    main()

if __name__ == "__main__":
    run()