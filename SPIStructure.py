#!usr/bin/python3
#-*- coding: utf-8 -*-

import IOStructure, BugStructure

class SPIStruct(IOStructure.IOStruct, BugStructure.BugStruct):
    def __init__(self):
        super().__init__()
        self.SPICounterMOSI = {}
        self.SPICounterMISO = {}
        self.SPICounterClk = {}
        self.SPICounterCS = {}
        self.SpiData = {}

    def AddSpiBug(self, text):
        # super().addBugList(text)
        self.addBug("spi", text)

    def AddSpiIO_MOSI(self, Model, Group, Pin, Remap):
        if Model not in self.SpiData:
            self.SpiData.update({Model : {}})
        if Model not in self.SPICounterMOSI:
            self.SPICounterMOSI.update({Model : 0})
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("MOSI")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData[Model]["MOSI_" + str(self.SPICounterMOSI[Model])] = self.GetIOStructData()
        self.SPICounterMOSI[Model] += 1

    def AddSpiIO_MISO(self, Model, Group, Pin, Remap):
        if Model not in self.SpiData:
            self.SpiData.update({Model : {}})
        if Model not in self.SPICounterMISO:
            self.SPICounterMISO.update({Model : 0})
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("MISO")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData[Model]["MISO_" + str(self.SPICounterMISO[Model])] = self.GetIOStructData()
        self.SPICounterMISO[Model] += 1

    def AddSpiIO_CS(self, Model, Group, Pin, Remap):
        if Model not in self.SpiData:
            self.SpiData.update({Model : {}})
        if Model not in self.SPICounterCS:
            self.SPICounterCS.update({Model : 0})
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("CS")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData[Model]["CS_" + str(self.SPICounterCS[Model])] = self.GetIOStructData()
        self.SPICounterCS[Model] += 1

    def AddSpiIO_Clk(self, Model, Group, Pin, Remap):
        if Model not in self.SpiData:
            self.SpiData.update({Model : {}})
        if Model not in self.SPICounterClk:
            self.SPICounterClk.update({Model : 0})
        self.SetIOStructGroup(Group)
        self.SetIOStructMode("Clk")
        self.SetIOStructPin(Pin)
        self.SetIOStructRemap(Remap)
        self.SpiData[Model]["Clk_" + str(self.SPICounterClk[Model])] = self.GetIOStructData()
        self.SPICounterClk[Model] += 1

    def GetSPIStructData(self):
        self.SpiData["SPIBug"] = self.GetBugData("spi")
        return self.SpiData

if __name__ == "__main__":
    SPI = SPIStruct()

    SPI.AddSpiBug("CS无法持续拉低")
    SPI.AddSpiBug("SPI FIFO")
    SPI.AddSpiIO_MOSI("spi0", "GPIOB", "Pin2", "Remap_0")
    SPI.AddSpiIO_CS("spi0", "GPIOB", "Pin2", "Remap_0")
    SPI.AddSpiIO_MOSI("spi1", "GPIOB", "Pin2", "Remap_0")
    SPI.AddSpiIO_CS("spi2", "GPIOB", "Pin2", "Remap_0")
    SPI.AddSpiIO_MOSI("spi1", "GPIOB", "Pin2", "Remap_0")
    SPI.AddSpiIO_CS("spi0", "GPIOB", "Pin2", "Remap_0")
    print(SPI.GetSPIStructData())
    print(SPI.GetSPIStructData()["spi0"]["CS_0"]["Group"])