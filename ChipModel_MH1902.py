#!usr/bin/python3
#-*- coding: utf-8 -*-

import UARTStructure, SPIStructure

class ChipMH1902(UARTStructure.UARTStruct, SPIStructure.SPIStruct):
    def GetMH1902StructData(self, ChipName):
        super().__init__()
        self.MH1902StructData = {"ChipName": ChipName}
        self.MH1902StructData["UART"] = self.GetUARTStructData("UART0")
        self.MH1902StructData["UART"] = self.GetUARTStructData("UART1")
        self.MH1902StructData["SPI"] = self.GetSPIStructData("SPI0")
        self.MH1902StructData["SPI"] = self.GetSPIStructData("SPI2")
        return self.MH1902StructData

if __name__ == "__main__":
    mh1902 = ChipMH1902()
    print(mh1902.GetMH1902StructData("MH1902"))