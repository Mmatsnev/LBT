#!/usr/bin/python
# -*- coding: UTF-8 -*-

class IOStruct(object):
    """
    外设模块的IO结构
    """

    def __init__(self, Remap, Mode, Pin, Group):
        IOStruct.IOStruct_Remap = Remap
        IOStruct.IOStruct_Mode = Mode
        IOStruct.IOStruct_Pin = Pin
        IOStruct.IOStruct_Group = Group
 
    def SetIOStructRemap(self, Remap):
        if Remap >= 0 and Remap <= 3:
            IOStruct.IOStruct_Remap = Remap
        else:
            pass
            # TODO:抛出异常


    def GetIOStructRemap(self):
        return IOStruct.IOStruct_Remap

    def SetIOStructMode(self, Mode):
        IOStruct.IOStruct_Mode = Mode

    def GetIOStructMode(self):
        return IOStruct.IOStruct_Mode

    def SetIOStructPin(self, Pin):
        IOStruct.IOStruct_Pin = Pin

    def GetIOStructPin(self):
        return IOStruct.IOStruct_Pin

    def SetIOStructGroup(self, Group):
        IOStruct.IOStruct_Group = Group

    def GetIOStructGroup(self):
        return IOStruct.IOStruct_Group

    def GetStruct(self):
        return IOStruct.IOStruct_Remap, IOStruct.IOStruct_Mode, IOStruct.IOStruct_Pin, IOStruct.IOStruct_Group

if __name__ == "__main__":
    print(IOStruct.__doc__)
    test = IOStruct(1, "OutPut", 2, "A")
    print(test.GetStruct())
    test.SetIOStructRemap(3)
    print(test.GetStruct())
    # print(IOStruct.__dict__)
    # # 可以随便增加类中的变量？？？
    # IOStruct.age = 1
    # print(IOStruct.age)
    # print(IOStruct.__dict__)
