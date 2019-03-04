#!/usr/bin/python
#-*- coding: UTF-8 -*-

class BugStruct(object):
    """
    记录bug
    获取bug记录
    """

    def __init__(self):
        super().__init__()
        self.BugTextList = []

    def addBug(self, BugText):
        self.BugTextList.append(BugText)

    def GetBugList(self):
        return self.BugTextList

    def GetBugListNumber(self):
        return len(self.BugTextList)

    def GetBugStructData(self):
        self.BugStructData = {}
        counter = 0
        for i in self.GetBugList():
            counter += 1
            self.BugStructData["Bug" + str(counter)] = i

        return self.BugStructData
    
if __name__ == "__main__":
    buglist = BugStruct()
    buglist.addBug("bug1")
    buglist.addBug("bug2")
    buglist.addBug("bug3")
    for i in buglist.GetBugList():
        print(i)
    print(buglist.GetBugStructData())
