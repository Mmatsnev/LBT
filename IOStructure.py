#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os

class IOStruct(object):
    """
    外设模块的IO结构
    """

    def __init__(self):
        super().__init__()
        self.IOStruct_Remap = "Remap_1"
        self.IOStruct_Mode = "InputPullUp"
        self.IOStruct_Pin = "Pin_0"
        self.IOStruct_Group = "GPIOA"
 
    def SetIOStructRemap(self, Remap):
        if int(Remap[-1]) >= 0 and int(Remap[-1]) <= 3:
            self.IOStruct_Remap = Remap
        else:
            pass
            # TODO:抛出异常


    def GetIOStructRemap(self):
        return self.IOStruct_Remap

    def SetIOStructMode(self, Mode):
        self.IOStruct_Mode = Mode

    def GetIOStructMode(self):
        return self.IOStruct_Mode

    def SetIOStructPin(self, Pin):
        self.IOStruct_Pin = Pin

    def GetIOStructPin(self):
        return self.IOStruct_Pin

    def SetIOStructGroup(self, Group):
        self.IOStruct_Group = Group

    def GetIOStructGroup(self):
        return self.IOStruct_Group

    def GetStruct(self):
        return self.IOStruct_Remap, self.IOStruct_Mode, self.IOStruct_Pin, self.IOStruct_Group

    def IOStructTransformToJson(self):
        self.JsonData = {
            "Group":self.IOStruct_Group, 
            "Model":self.IOStruct_Mode, 
            "Pin":self.IOStruct_Pin, 
            "Remap":self.IOStruct_Remap
            }
        return json.dumps(self.JsonData)
        

if __name__ == "__main__":
    print(IOStruct.__doc__)
    test = IOStruct()
    print(test.GetStruct())
    test.SetIOStructRemap("Remap_0")
    test.SetIOStructGroup("GPIOA")
    test.SetIOStructMode("RX")
    test.SetIOStructPin("Pin_0")
    print(test.GetStruct())
    print(test.TransformToJson())
    test.SetIOStructPin("Pin_1")
    test.SetIOStructMode("Tx")
    print(test.TransformToJson())
    # print(IOStruct.__dict__)
    # # 可以随便增加类中的变量？？？
    # IOStruct.age = 1
    # print(IOStruct.age)
    # print(IOStruct.__dict__)
