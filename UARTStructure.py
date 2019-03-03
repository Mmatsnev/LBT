#!/usr/bin/python
#-*- coding: UTF-8 -*-

import IOStructure
import BugStructure
import json
class UARTStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    """
    继承IOSturct类
    """
    def addUartBug(self, text):
        # super().addBugList(text)
        self.addBugList(text)

    # Introduce = "None"
    # BugTextList = []
    # def __init__(self, data):
    #     self.data = data
    def GetUARTStructData(self, ModelName):
        self.UartStructData = {"ModelName": ModelName}
        self.UartStructData["Rx"] = self.GetIOStructData()
        self.UartStructData["BugList"] = self.GetBugStructData()
        return self.UartStructData

if __name__ == "__main__":
    uart0 = UARTStruct()

    uart0.addUartBug("DMA model0 无法使用")
    uart0.addUartBug("UART FIFO")
    print(uart0.GetUARTStructData("Uart0"))
    print(uart0.GetUARTStructData("Uart0")["Rx"]["Group"])
    # for bugdata in uart0.GetBugList():
    #     print("bug: " + bugdata)
