#!/usr/bin/python
# -*- coding: UTF-8 -*-

class IOStructure:
    "外设模块的IO结构"
    __IOStructure_Remap = 1
    __IOStructure_Mode = "InPutPullUP"
    __IOStructure_Pin = 0
    __IOStructure_Group = "A"

    def SetStruct(self, Remap, Mode, Pin, Group):
        IOStructure.__IOStructure_Remap = Remap
        IOStructure.__IOStructure_Mode = Mode
        IOStructure.__IOStructure_Pin = Pin
        IOStructure.__IOStructure_Group = Group
 
    def SetIOStructRemap(self, Remap):
        if Remap >= 0 and Remap <= 3:
            IOStructure.__IOStructure_Remap = Remap
        else:
            pass
            # TODO:抛出异常


    def GetIOStructRemap(self):
        return IOStructure.__IOStructure_Remap

    def SetIOStructMode(self, Mode):
        IOStructure.__IOStructure_Mode = Mode

    def GetIOStructMode(self):
        return IOStructure.__IOStructure_Mode

    def SetIOStructPin(self, Pin):
        IOStructure.__IOStructure_Pin = Pin

    def GetIOStructPin(self, Pin):
        return IOStructure.__IOStructure_Pin

    def SetIOStructGroup(self, Group):
        IOStructure.__IOStructure_Group = Group

    def GetIOStructGroup(self, Group):
        return IOStructure.__IOStructure_Group

    def GetStruct(self):
        return IOStructure.__IOStructure_Remap, IOStructure.__IOStructure_Mode, IOStructure.__IOStructure_Pin, IOStructure.__IOStructure_Group

print(IOStructure.__doc__)
test = IOStructure()
test.SetStruct(1, "OutPut", 2, "A")
print(test.GetStruct())
test.SetIOStructRemap(3)
print(test.GetStruct())
# print(IOStructure.__dict__)
# # 可以随便增加类中的变量？？？
# IOStructure.age = 1
# print(IOStructure.age)
# print(IOStructure.__dict__)

