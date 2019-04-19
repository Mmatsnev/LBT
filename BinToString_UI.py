#usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import os
from PyQt5 import QtWidgets

class BinToString(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.BinToStringUI()

    def BinToStringUI(self):
        # 获取当前程序文件位置
        self.cwd = os.getcwd()

        # 创建一个按钮，点击后触发 chooseFile 槽
        self.ButtonChooseFile = QtWidgets.QPushButton(self)
        self.ButtonChooseFile.setText("选择文件")
        self.ButtonChooseFile.clicked.connect(self.slot_btn_chooseFile)

        # 创建一个单行文本框显示文件目录
        self.LineEditShowFilePath = QtWidgets.QLineEdit(self)
        
        # 创建一个多行文本框显示文件数据
        self.TextEditShowFileData = QtWidgets.QTextEdit(self)

        self.LableShowFileCounter = QtWidgets.QLabel(self)
        
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.addWidget(self.LineEditShowFilePath, 0, 0)
        self.GridLayout.addWidget(self.ButtonChooseFile, 0, 1)
        self.GridLayout.addWidget(self.TextEditShowFileData, 1, 0, 1, 2)
        self.GridLayout.addWidget(self.LableShowFileCounter, 2, 0)

        self.setLayout(self.GridLayout)
        return self.GridLayout
    


    def TransfromToString(self):
        counter = 0
        fileName = input("输入要转换的文件名称")
        with open(fileName + ".txt", 'w') as fileWrite:
            with open(fileName, 'rb') as fileRead:
                data = fileRead.read(1)
                while data:
                    if counter == 16:
                        fileWrite.write("\n")
                        counter
                    writedata = bytearray(data).hex()
                    fileWrite.write('0x' + writedata + ",")
                    counter += 1
                    data = fileRead.read(1)


    def slot_btn_chooseFile(self):
        self.fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

        if self.fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(self.fileName_choose)
        print("文件筛选器类型: ",filetype)
        self.LineEditShowFilePath.setText(self.fileName_choose)
        self.ReadBinFile()
        self.TextEditShowFileData.setText('0x' + ', 0x'.join([str(x) for x in self.FileData]))
        self.LableShowFileCounter.setText("字节数：" + str(self.FileDataCounter))

    def ReadBinFile(self):
        self.FileData = []
        self.FileDataCounter = 0
        with open(self.fileName_choose, 'rb') as fileRead:
            data = fileRead.read(1)
            while data:
                self.FileDataCounter += 1
                self.FileData.append(bytearray(data).hex())
                data = fileRead.read(1)
        print(self.FileData)
        print(self.FileDataCounter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = BinToString()
    test.initUI()
    test.show()
    sys.exit(app.exec_())