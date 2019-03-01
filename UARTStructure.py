#!/usr/bin/python
# -*- coding: UTF-8 -*-

import IOStructure
import BugStructure
class UARTStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    """
    继承IOSturct类
    """
    Introduce = "None"
    BugTextList = []
    # def __init__(self, data):
    #     self.data = data


if __name__ == "__main__":
    uart0 = UARTStruct(0, "RX", 0, "A")
    uart0.addBugList("DMA model0 无法使用")
    print(uart0.GetStruct())
    for bugdata in uart0.GetBugList():
        print("bug: " + bugdata)
