#!usr/bin/python3
#-*- coding: utf-8 -*-

import IOStructure, BugStructure

class SPIStruct(IOStructure.IOStruct, BugStructure.BugStruct):

    def GetSPIStructData(self, ModelName):
        super().__init__()
        self.SPIStructData = {"ModelName": ModelName}
        self.SPIStructData["MOSI"] = self.GetIOStructData()
        self.SPIStructData["MISO"] = self.GetIOStructData()
        self.SPIStructData["CLK"] = self.GetIOStructData()
        self.SPIStructData["CS"] = self.GetIOStructData()
        self.addBugList("CS无法持续拉低")
        self.addBugList("SPI FIFO")
        self.SPIStructData["BugList"] = self.GetBugStructData()
        return self.SPIStructData

if __name__ == "__main__":
    SPI0 = SPIStruct()

    SPI0.addBugList("CS无法持续拉低")
    SPI0.addBugList("SPI FIFO")
    print(SPI0.GetSPIStructData("SPI0"))
    print(SPI0.GetSPIStructData("SPI0")["CS"]["Group"])