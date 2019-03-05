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
        self.UartCounterRx = {}
        self.UartCounterTx = {}
        self.UartData = {}

    def AddUartBug(self, text):
        self.addBug("uart", text)

    def AddUartRxIO(self, Model, Group, Pin, Remap):
        if Model not in self.UartData:
            self.UartData.update({Model : {}})
        if Model not in self.UartCounterRx:
            self.UartCounterRx.update({Model : 0})
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("Rx")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.UartData[Model]["Rx" + str(self.UartCounterRx[Model])] = self.GetIOStructData()
        self.UartCounterRx[Model] += 1

    def AddUartTxIO(self, Model, Group, Pin, Remap):
        if Model not in self.UartData:
            self.UartData.update({Model : {}})
        if Model not in self.UartCounterTx:
            self.UartCounterTx.update({Model : 0})
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("Tx")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.UartData[Model]["Tx" + str(self.UartCounterTx[Model])] = self.GetIOStructData()
        self.UartCounterTx[Model] += 1

    def GetUARTStructData(self):
        self.UartData["UartBug"] = self.GetBugData("uart")
        return self.UartData

if __name__ == "__main__":
    uart = UARTStruct()

    uart.AddUartBug("DMA model0 无法使用")
    uart.AddUartBug("UART FIFO")
    uart.AddUartRxIO("UART0", "GroupA", "Pin_0", "Remap_0")
    uart.AddUartTxIO("UART0", "GroupA", "Pin_1", "Remap_0")
    uart.AddUartTxIO("UART0", "GroupD", "Pin_5", "Remap_0")
    uart.AddUartRxIO("UART1", "GroupA", "Pin_0", "Remap_0")
    uart.AddUartTxIO("UART2", "GroupA", "Pin_1", "Remap_0")
    uart.AddUartTxIO("UART1", "GroupD", "Pin_5", "Remap_0")
    uart.AddUartRxIO("UART0", "GroupA", "Pin_0", "Remap_0")
    uart.AddUartTxIO("UART0", "GroupA", "Pin_1", "Remap_0")
    uart.AddUartTxIO("UART0", "GroupD", "Pin_5", "Remap_0")
    print(uart.GetUARTStructData())
    print(uart.GetUARTStructData()["UART0"]["Rx0"]["Group"])
    # for bugdata in uart0.GetBugList():
    #     print("bug: " + bugdata)
