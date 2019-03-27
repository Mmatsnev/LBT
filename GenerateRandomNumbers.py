

def GenerateRandomNumbers(number):
    import random
    counter = 0

    with open("data.txt", 'w') as filewrite:
        while counter < number:
            counter += 1
            databyte = hex(random.randint(0,255))
            if len(databyte) == 3:
                databyte = databyte[0 : 2] + '0' + databyte[2 : ]
            filewrite.write(databyte + ', ')
            if counter % 16 == 0:
                filewrite.write("\n")

if __name__ == "__main__":
    GenerateRandomNumbers(100)    
