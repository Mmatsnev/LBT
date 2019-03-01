#!/usr/bin/python
#-*- coding: UTF-8 -*-

import IOStructure
import BugStructure
import json
class UARTStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    """
    继承IOSturct类
    """
    def SetIntroduce(self, text):
        self.Introduce = text

    def GetIntroduce(self):
        return self.Introduce
    # Introduce = "None"
    # BugTextList = []
    # def __init__(self, data):
    #     self.data = data
    def UARTStructTransformToJson(self, ModelName):
        self.JsonData = {"ModelName":ModelName}
        self.JsonData["Rx"] = self.IOStructTransformToJson()
        counter = 0
        for i in self.GetBugList():
            counter += 1
            self.JsonData["Bug" + str(counter)] = i
        return self.JsonData

if __name__ == "__main__":
    uart0 = UARTStruct()

    uart0.addBugList("DMA model0 无法使用")
    uart0.addBugList("UART FIFO")
    print(uart0.UARTStructTransformToJson("Uart0"))
    print(json.loads(uart0.UARTStructTransformToJson("Uart0")["Rx"])["Group"])
    for bugdata in uart0.GetBugList():
        print("bug: " + bugdata)
