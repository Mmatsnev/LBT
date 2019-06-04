# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\LBT项目\LBT\UI\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(729, 513)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 160, 411, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.listWidget1 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget1.setObjectName("listWidget1")
        item = QtWidgets.QListWidgetItem()
        self.listWidget1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget1.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget1)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(100, 30, 300, 300))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "1"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "3"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget1.isSortingEnabled()
        self.listWidget1.setSortingEnabled(False)
        item = self.listWidget1.item(0)
        item.setText(_translate("Form", "a"))
        item = self.listWidget1.item(1)
        item.setText(_translate("Form", "b"))
        item = self.listWidget1.item(2)
        item.setText(_translate("Form", "c"))
        item = self.listWidget1.item(3)
        item.setText(_translate("Form", "d"))
        self.listWidget1.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "123"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "234"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Form", "345"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Form", "456"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

