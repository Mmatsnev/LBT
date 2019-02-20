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

    def GetStruct(self):
        return IOStructure.__IOStructure_Remap
        return IOStructure.__IOStructure_Mode

print(IOStructure.__doc__)
test = IOStructure()
test.SetRemap(2, "OutPut", )
print(test.GetRemap())
print(IOStructure.__dict__)
# 可以随便增加类中的变量？？？
IOStructure.age = 1
print(IOStructure.age)
print(IOStructure.__dict__)

