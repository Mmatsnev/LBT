#!/usr/bin/python
#-*- coding: UTF-8 -*-

class BugStruct(object):
    """
    记录bug
    获取bug记录
    """

    def __init__(self):
        super().__init__()
        self.BugTextList = {}
        self.counter = {}

    def addBug(self, Model, BugText):
        if Model not in self.BugTextList:
            self.BugTextList.update({Model: {}})
            self.counter.update({Model: 0})
        self.BugTextList[Model]["Bug" + str(self.counter[Model])] = BugText
        self.counter[Model] += 1


    def GetBugList(self):
        return self.BugTextList

    def GetBugListNumber(self, Model):
        if Model in self.counter:
            return self.counter[Model]
        else:
            return 0

    def GetBugData(self, Model):
        if Model in self.BugTextList:
            return self.BugTextList[Model]
        else:
            return 0
if __name__ == "__main__":
    buglist = BugStruct()
    buglist.addBug("uart0", "bug text1")
    buglist.addBug("uart0", "bug text2")
    buglist.addBug("spi0", "bug text2")
    # buglist.addBug("bug2")
    # buglist.addBug("bug3")
    # for i in buglist.GetBugList():
    #     print(i)
    print(buglist.GetBugList())
    print("uart0 bug:")
    print(buglist.GetBugData("uart0"))