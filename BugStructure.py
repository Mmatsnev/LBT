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

    def addBugList(self, BugText):
        self.BugTextList.append(BugText)

    def GetBugList(self):
        return self.BugTextList

    def GetBugListNumber(self):
        return len(self.BugTextList)

    
