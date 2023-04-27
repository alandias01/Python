import os

print("Start")


# First you open open(file, mode) where mode=(r,w,a). Default = r
dataFile = open('./data.txt', 'r')


def readEverything():
    readEverything = dataFile.read()
    print(readEverything)


def readIntoArray():
    readEverythingArray = dataFile.readlines()
    count = 0
    for line in readEverythingArray:
        count += 1
        # strip the newline ‘\n’
        print("Line{}: {}".format(count, line.strip()))


def readLineByLine():
    count = 0
    while True:
        count += 1

        line = dataFile.readline()

        # if line is empty, end of file is reached
        # empty lines within a file should have a new line char '\n'
        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))


def readLineByLineIterateFileObject():
    # open() returns an iterable file object when opening a file
    # which lets us directly iterate the file object using for loop
    # shorter the readLine()
    count = 0
    for line in dataFile:
        count += 1
        print("Line{}: {}".format(count, line.strip()))


dataFile.close()

# "with" allows you to close without writing close()


def withRead():
    with open("data.txt") as file:
        print(file.read())
        # print(file.readlines())


def withReadIterateObject():
    with open("data.txt") as file:
        for item in file:
            print(item.rstrip())


def withReadsample1():
    with open('data.txt') as f:
        lines = [line.rstrip() for line in f]

    print(lines)


withReadIterateObject()
