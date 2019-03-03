# #!/usr/bin/python
# #-*- coding: UTF-8 -*-

# class BugStruct(object):
#     """
#     记录bug
#     获取bug记录
#     """

#     def __init__(self):
#         super().__init__()
#         self.BugTextList = []

#     def addBugList(self, BugText):
#         super().addBugList(BugText)
#         self.BugTextList.append(BugText)

#     def GetBugList(self):
#         super().__init__()
#         return self.BugTextList

#     def GetBugListNumber(self):
#         super().__init__()
#         return len(self.BugTextList)

#     def GetBugStructData(self):
#         super().__init__()
#         self.BugStructData = {}
#         counter = 0
#         for i in self.GetBugList():
#             counter += 1
#             self.BugStructData["Bug" + str(counter)] = i

#         return self.BugStructData
    
# if __name__ == "__main__":
#     buglist = BugStruct()
#     buglist.addBugList("bug1")
#     buglist.addBugList("bug2")
#     buglist.addBugList("bug3")
#     for i in buglist.GetBugList():
#         print(i)
#     print(buglist.GetBugStructData())

#!/usr/bin/python
# -*- coding: UTF-8 -*-
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    def bar(self,message):
        print ("%s from Parent" % message)
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild,self).__init__()
        print ('Child')
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
