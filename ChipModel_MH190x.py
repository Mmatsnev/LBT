#!usr/bin/python3
#-*- coding: utf-8 -*-

import UARTStructure, SPIStructure
import json
import os

class ChipMH190x(UARTStructure.UARTStruct, SPIStructure.SPIStruct):
    def __init__(self, ChipName):
        super().__init__()
        self.MH190xData = {}
        if ChipName not in self.MH190xData:
            self.MH190xData.update({ChipName : {}})

    def GetMH190xData(self, ChipName):
        if ChipName not in self.MH190xData:
            return 0
        else:
            self.MH190xData[ChipName]["UART"] = self.GetUARTStructData()
            self.MH190xData[ChipName]["SPI"] = self.GetSPIStructData()
            return self.MH190xData

if __name__ == "__main__":
    mh1902 = ChipMH190x("MH1902")
    mh1902.AddUartRxIO("uart0", "GroupA", "Pin_0", "Remap_0")
    mh1902.AddUartTxIO("uart0", "GroupA", "Pin_1", "Remap_0")
    mh1902.AddUartTxIO("uart1", "GroupD", "Pin_5", "Remap_0")
    mh1902.AddSpiIO_MOSI("spi0", "GPIOB", "Pin_2", "Remap_0")
    mh1902.AddSpiIO_MISO("spi0", "GPIOB", "Pin_3", "Remap_0")
    mh1902.AddSpiIO_CS("spi0", "GPIOB", "Pin_4", "Remap_0")
    mh1902.AddSpiIO_Clk("spi0", "GPIOB", "Pin_5", "Remap_0")
    mh1902.AddUartBug("Uart Bug text")
    mh1902.AddSpiBug("Spi Bug text")
    mh1902.AddSpiBug("Spi Bug测试")
    mh1902.AddSpiIO_Clk("spi1", "GPIOD", "Pin_0", "Remap_2")
    print(mh1902.GetMH190xData("MH1902"))
    print(mh1902.GetMH190xData("MH1903"))

    mh1903 = ChipMH190x("MH1903")
    print(mh1903.GetMH190xData("MH1903"))

    mh1903.AddUartBug("1903 uart bug test")
    print(mh1903.GetMH190xData("MH1903"))

    # print(mh1902.GetMH1902StructData("MH1902"))
    # with open("data.json", "w") as writeFile:
    #     writeFile.write(json.dumps(mh1902.GetMH1902StructData("MH1902")))
    # with open("data.json", "r") as readFile:
    #     print(json.loads(readFile.readline()))