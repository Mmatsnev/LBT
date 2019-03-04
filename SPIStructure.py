#!usr/bin/python3
#-*- coding: utf-8 -*-

import IOStructure, BugStructure

class SPIStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    def __init__(self):
        super().__init__()

    def addSpiBug(self, text):
        # super().addBugList(text)
        self.addBug(text)

    def addSpiIO_MOSI(self, Group, Pin, Model, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode(Model)
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)

    def GetSPIStructData(self, ModelName):
        self.SPIStructData = {"ModelName": ModelName}
        self.SPIStructData["MOSI"] = self.GetIOStructData()
        self.SPIStructData["MISO"] = self.GetIOStructData()
        self.SPIStructData["CLK"] = self.GetIOStructData()
        self.SPIStructData["CS"] = self.GetIOStructData()
        self.SPIStructData["BugList"] = self.GetBugStructData()
        return self.SPIStructData

if __name__ == "__main__":
    SPI0 = SPIStruct()

    SPI0.addBug("CS无法持续拉低")
    SPI0.addBug("SPI FIFO")
    SPI0.addSpiIO_MOSI("GPIOB", "Pin2", "OutPut", "Remap_0")
    print(SPI0.GetSPIStructData("SPI0"))
    print(SPI0.GetSPIStructData("SPI0")["CS"]["Group"])