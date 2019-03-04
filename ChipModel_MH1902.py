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
    mh1902.SetUartRxIO("GroupA", "Pin_0", "Remap_0")
    mh1902.SetUartTxIO("GroupA", "Pin_1", "Remap_0")
    mh1902.SetUartTxIO("GroupD", "Pin_5", "Remap_0")
    mh1902.AddUartBug("Uart Bug")
    mh1902.addSpiBug("Spi Bug")
    print(mh1902.GetMH1902StructData("MH1902"))