#!usr/bin/python3
#-*- coding: utf-8 -*-

import UARTStructure, SPIStructure

class ChipMH1902(UARTStructure.UARTStruct, SPIStructure.SPIStruct):
    def __init__(self):
        super().__init__()

    def GetMH1902StructData(self, ChipName):
        self.MH1902StructData = {"ChipName": ChipName}
        self.MH1902StructData["UART"] = self.GetUARTStructData("UART0")
        self.MH1902StructData["UART"] = self.GetUARTStructData("UART1")
        self.MH1902StructData["SPI"] = self.GetSPIStructData("SPI0")
        self.MH1902StructData["SPI"] = self.GetSPIStructData("SPI2")
        return self.MH1902StructData

if __name__ == "__main__":
    mh1902 = ChipMH1902()
    mh1902.AddUartRxIO("GroupA", "Pin_0", "Remap_0")
    mh1902.AddUartTxIO("GroupA", "Pin_1", "Remap_0")
    mh1902.AddUartTxIO("GroupD", "Pin_5", "Remap_0")
    mh1902.AddSpiIO_MOSI("GPIOB", "Pin_2", "Remap_0")
    mh1902.AddSpiIO_MISO("GPIOB", "Pin_3", "Remap_0")
    mh1902.AddSpiIO_CS("GPIOB", "Pin_4", "Remap_0")
    mh1902.AddSpiIO_Clk("GPIOB", "Pin_5", "Remap_0")
    mh1902.AddUartBug("Uart Bug text")
    mh1902.AddSpiBug("Spi Bug text")

    print(mh1902.GetMH1902StructData("MH1902"))