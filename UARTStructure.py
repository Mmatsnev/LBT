#!/usr/bin/python
# -*- coding: UTF-8 -*-

import IOStructure
class UART_Struct(IOStructure.IOStruct):
    Introduce = "None"

    # def __init__(self, data):
    #     self.data = data

    def setdata(self, data):
        self.Introduce = data

    def getdata(self):
        return self.Introduce

test2 = UART_Struct(4, 1,2,3)
test2.setdata(2)
print(test2.getdata())
test2.data = 5
print(test2.getdata())
test2.SetIOStructGroup("B")
print(test2.GetIOStructGroup())
test3 = UART_Struct(4, 1,2,3)
test3.setdata(3)
print(test2.getdata())