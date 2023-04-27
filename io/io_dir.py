import os

print("Start")


def printDir():
    for files in os.listdir():
        print(files)
