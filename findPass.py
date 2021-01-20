# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findPassWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_findPassWindow(object):
    def setupUi(self, findPassWindow):
        findPassWindow.setObjectName("findPassWindow")
        findPassWindow.resize(390, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dist/dump/propusk64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        findPassWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(findPassWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.findBtn = QtWidgets.QPushButton(self.centralwidget)
        self.findBtn.setGeometry(QtCore.QRect(280, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.findBtn.setFont(font)
        self.findBtn.setObjectName("findBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 120, 371, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.carnumBox = QtWidgets.QLineEdit(self.centralwidget)
        self.carnumBox.setGeometry(QtCore.QRect(170, 80, 91, 31))
        self.carnumBox.setObjectName("carnumBox")
        self.surnameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameBox.setGeometry(QtCore.QRect(30, 160, 331, 31))
        self.surnameBox.setFrame(True)
        self.surnameBox.setReadOnly(True)
        self.surnameBox.setObjectName("surnameBox")
        self.nameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.nameBox.setGeometry(QtCore.QRect(30, 220, 331, 31))
        self.nameBox.setReadOnly(True)
        self.nameBox.setObjectName("nameBox")
        self.fathernameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.fathernameBox.setGeometry(QtCore.QRect(30, 280, 331, 31))
        self.fathernameBox.setReadOnly(True)
        self.fathernameBox.setObjectName("fathernameBox")
        self.fromBox = QtWidgets.QLineEdit(self.centralwidget)
        self.fromBox.setGeometry(QtCore.QRect(30, 420, 161, 31))
        self.fromBox.setReadOnly(True)
        self.fromBox.setObjectName("fromBox")
        self.toBox = QtWidgets.QLineEdit(self.centralwidget)
        self.toBox.setGeometry(QtCore.QRect(210, 420, 151, 31))
        self.toBox.setReadOnly(True)
        self.toBox.setObjectName("toBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 191, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 231, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 400, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 400, 141, 16))
        self.label_7.setObjectName("label_7")
        self.autoBrandBox = QtWidgets.QLineEdit(self.centralwidget)
        self.autoBrandBox.setGeometry(QtCore.QRect(30, 340, 331, 31))
        self.autoBrandBox.setText("")
        self.autoBrandBox.setReadOnly(True)
        self.autoBrandBox.setObjectName("autoBrandBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 320, 231, 16))
        self.label_8.setObjectName("label_8")
        findPassWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(findPassWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 21))
        self.menubar.setObjectName("menubar")
        findPassWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(findPassWindow)
        self.statusbar.setObjectName("statusbar")
        findPassWindow.setStatusBar(self.statusbar)

        self.retranslateUi(findPassWindow)
        QtCore.QMetaObject.connectSlotsByName(findPassWindow)

    def retranslateUi(self, findPassWindow):
        _translate = QtCore.QCoreApplication.translate
        findPassWindow.setWindowTitle(_translate("findPassWindow", "Найти пропуск в базе"))
        self.label.setText(_translate("findPassWindow", "Найти пропуск в базе"))
        self.label_6.setText(_translate("findPassWindow", "Номер автомобиля:"))
        self.findBtn.setText(_translate("findPassWindow", "Найти"))
        self.carnumBox.setPlaceholderText(_translate("findPassWindow", "А123БВ"))
        self.label_2.setText(_translate("findPassWindow", "Фамилия"))
        self.label_3.setText(_translate("findPassWindow", "Имя"))
        self.label_4.setText(_translate("findPassWindow", "Отчество"))
        self.label_5.setText(_translate("findPassWindow", "Пропускать с"))
        self.label_7.setText(_translate("findPassWindow", "по"))
        self.label_8.setText(_translate("findPassWindow", "Марка автомобиля"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    findPassWindow = QtWidgets.QMainWindow()
    ui = Ui_findPassWindow()
    ui.setupUi(findPassWindow)
    findPassWindow.show()
    sys.exit(app.exec_())