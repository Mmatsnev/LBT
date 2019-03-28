
import time
def GenerateRandomNumbers(number):
    import random
    counter = 0
    tmp = ""
    logtime = time.time()

    b = range(0,11)

    # 这个接口应该是获取b 范围内的随机数个数，并且不重复
    b_list = random.sample(b, 10)
    print(b_list)
    print(time.time() - logtime)
    # print(b_list)
    logtime = time.time()
    while counter < number:
        counter += 1
        databyte = hex(random.randint(0,255))
        if len(databyte) == 3:
            databyte = databyte[0 : 2] + '0' + databyte[2 : ]
        tmp = tmp + databyte + ', '
        # filewrite.write()
        if counter % 16 == 0:
            # filewrite.write("\n")
            tmp = tmp + "\n"
    print(time.time() - logtime)
    with open("data.txt", 'w') as filewrite:
        print("write File")
        logtime = time.time()
        filewrite.write(tmp)
        print(time.time() - logtime)
if __name__ == "__main__":
    GenerateRandomNumbers(123)    
