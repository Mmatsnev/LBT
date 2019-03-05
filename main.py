#!usr/bin/python3
#-*- coding: utf-8 -*-

from ChipModel_MH190x import ChipMH190x
import json
import os

if __name__ == "__main__":
    mh1902 = ChipMH190x("MH1902")
    mh1902.AddUartRxIO("UART0", "GroupA", "Pin_0", "Remap_0")
    mh1902.AddUartTxIO("UART0", "GroupA", "Pin_1", "Remap_0")
    mh1902.AddUartTxIO("UART0", "GroupD", "Pin_5", "Remap_0")
    mh1902.AddSpiIO_MOSI("SPI0", "GPIOB", "Pin_2", "Remap_0")
    mh1902.AddSpiIO_MISO("SPI0", "GPIOB", "Pin_3", "Remap_0")
    mh1902.AddSpiIO_CS("SPI0", "GPIOB", "Pin_4", "Remap_0")
    mh1902.AddSpiIO_Clk("SPI0", "GPIOB", "Pin_5", "Remap_0")
    mh1902.AddUartBug("Uart Bug text")
    mh1902.AddSpiBug("Spi Bug text")
    mh1902.AddSpiBug("Spi Bug测试")
    print(mh1902.GetMH190xData("MH1902"))
    with open("MH1902data.json", "w") as writeFile:
        writeFile.write(json.dumps(mh1902.GetMH190xData("MH1902")))

    mh1903 = ChipMH190x("MH1903")
    mh1903.AddUartRxIO("UART0", "GroupE", "Pin_0", "Remap_0")
    mh1903.AddUartTxIO("UART0", "GroupE", "Pin_1", "Remap_0")
    mh1903.AddUartBug("1903 Uart Bug text")
    mh1903.AddSpiBug("1903 Spi Bug text")
    mh1903.AddSpiBug("1903 Spi Bug测试")
    print(mh1903.GetMH190xData("MH1903"))
    with open("data.json", "w") as writeFile:
        writeFile.write(json.dumps(mh1903.GetMH190xData("MH1902")))