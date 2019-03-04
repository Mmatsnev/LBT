#!usr/bin/python3
#-*- coding: utf-8 -*-

import IOStructure, BugStructure

class SPIStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    def __init__(self):
        super().__init__()
        self.SPICounterMOSI = 0
        self.SPICounterMISO = 0
        self.SPICounterClk = 0
        self.SPICounterCS = 0
        self.SpiData = {}

    def AddSpiBug(self, text):
        # super().addBugList(text)
        self.addBug("spi", text)

    def AddSpiIO_MOSI(self, Group, Pin, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("MOSI")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData["MOSI_" + str(self.SPICounterMOSI)] = self.GetIOStructData()
        self.SPICounterMOSI += 1

    def AddSpiIO_MISO(self, Group, Pin, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("MISO")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData["MISO_" + str(self.SPICounterMISO)] = self.GetIOStructData()
        self.SPICounterMISO += 1

    def AddSpiIO_CS(self, Group, Pin, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("CS")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData["CS_" + str(self.SPICounterCS)] = self.GetIOStructData()
        self.SPICounterCS += 1

    def AddSpiIO_Clk(self, Group, Pin, Remap):
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("Clk")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData["Clk_" + str(self.SPICounterClk)] = self.GetIOStructData()
        self.SPICounterClk += 1

    def GetSPIStructData(self, ModelName):
        self.SpiData["ModelName"] = ModelName
        self.SpiData["SPIBug"] = self.GetBugData("spi")
        return self.SpiData

if __name__ == "__main__":
    SPI0 = SPIStruct()

    SPI0.AddSpiBug("CS无法持续拉低")
    SPI0.AddSpiBug("SPI FIFO")
    SPI0.AddSpiIO_MOSI("GPIOB", "Pin2", "Remap_0")
    SPI0.AddSpiIO_CS("GPIOB", "Pin2", "Remap_0")
    print(SPI0.GetSPIStructData("SPI0"))
    print(SPI0.GetSPIStructData("SPI0")["CS_0"]["Group"])