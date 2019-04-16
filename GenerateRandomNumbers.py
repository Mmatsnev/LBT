
import time, threading
import random

def GenerateRandomNumbers(number):
    counter = 0
    tmp = ""
    while counter < number:
        counter += 1
        databyte = hex(random.randint(0,255))
        if len(databyte) == 3:
            databyte = databyte[0 : 2] + '0' + databyte[2 : ]
        tmp = tmp + databyte + ', '
        if counter % 16 == 0:
            tmp = tmp + "\n"
    return tmp

def RandomDataWriteToFile(strdata):
    with open("data.txt", 'w') as filewrite:
        print("write File")
        filewrite.write(strdata)

if __name__ == "__main__":
    WriteToFile(GenerateRandomNumbers(100000))