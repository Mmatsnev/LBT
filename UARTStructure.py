#!/usr/bin/python
#-*- coding: UTF-8 -*-

import IOStructure
import BugStructure
import json
class UARTStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    """
    继承IOStruct类
    """
    def __init__(self):
        super().__init__()
        self.UartCounterRx = 0
        self.UartCounterTx = 0
        self.UartCounterBug = 0
        self.UartData = {}

    def AddUartBug(self, text):
        self.UartData["Bug" + str(self.UartCounterBug)] = text
        self.UartCounterBug += 1

    def SetUartRxIO(self, Group, Pin, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("Rx")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.UartData["Rx" + str(self.UartCounterRx)] = self.GetIOStructData()
        self.UartCounterRx += 1

    def SetUartTxIO(self, Group, Pin, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("Tx")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.UartData["Tx" + str(self.UartCounterTx)] = self.GetIOStructData()
        self.UartCounterTx += 1

    def GetUARTStructData(self, ModelName):
        self.UartData["ModelName"] = ModelName
        return self.UartData

if __name__ == "__main__":
    uart0 = UARTStruct()

    uart0.AddUartBug("DMA model0 无法使用")
    uart0.AddUartBug("UART FIFO")
    uart0.SetUartRxIO("GroupA", "Pin_0", "Remap_0")
    uart0.SetUartTxIO("GroupA", "Pin_1", "Remap_0")
    uart0.SetUartTxIO("GroupD", "Pin_5", "Remap_0")
    print(uart0.GetUARTStructData("Uart0"))
    print(uart0.GetUARTStructData("Uart0")["Rx0"]["Group"])
    # for bugdata in uart0.GetBugList():
    #     print("bug: " + bugdata)
