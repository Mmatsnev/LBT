#usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import os
from PyQt5 import QtWidgets

class BinToTxt(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.OpenFile()

    def OpenFile(self):
        # 定义一个按钮，点击后触发 chooseFile 槽
        self.ButtonChooseFile = QtWidgets.QPushButton(self)
        self.ButtonChooseFile.setText("选择文件")
        self.ButtonChooseFile.clicked.connect(self.slot_btn_chooseFile)

        self.LineEditShowFilePath = QtWidgets.QLineEdit(self)


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.ButtonChooseFile)
        layout.addWidget(self.LineEditShowFilePath)

        self.setLayout(layout)


    def TransfromToTxt(self):
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
        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(fileName_choose)
        self.LineEditShowFilePath.setText(fileName_choose)
        print("文件筛选器类型: ",filetype)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = BinToTxt()
    test.initUI()
    test.show()
    sys.exit(app.exec_())