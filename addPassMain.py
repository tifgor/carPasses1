from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtCore import QRegExp, QDate

from addPass import Ui_addPassWindow
import sys, os.path
#from dbSettings import dbPath

import configparser
my_config_parser = configparser.ConfigParser()
my_config_parser.read('carPasses.cfg')
payload = {
    'dbPath': my_config_parser.get('DEFAULT','dbPath')
}

app = QApplication(sys.argv)

#init
addPassWindow = QMainWindow()
ui = Ui_addPassWindow()
ui.setupUi(addPassWindow)

#SETTINGS
dig50rx= QRegExp("[0-9]{50}")
ui.memoNumBox.setValidator(QRegExpValidator(dig50rx))
ui.memoDateBox.setDate(QDate.currentDate())
ui.passDateBox.setDate(QDate.currentDate())
ui.passDate2Box.setDate(QDate.currentDate())
addPassWindow.setFixedSize(addPassWindow.size())

#carRx = QtCore.QRegExp("[а-я][0-9]{3}[а-я]{2}")
#ui.carnumBox.setValidator(QtGui.QRegExpValidator(carRx))
#--оставить только для российских гос номеров

#SHOW
addPassWindow.show()
dbPath=payload.get('dbPath')
if not os.path.isfile(dbPath):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("Ошибка")
    msgbox.setIcon(QMessageBox.Critical)
    msgbox.setText("Не обнаружена база данных или нет соединения с сервером.")
    ui.addPassBtn.setEnabled(False)
    msgbox.exec()
#logic
def addMemo():
    errorTxt = ""
    memoId = ui.memoNumBox.text()
    memoDate = ui.memoDateBox.date().toString('dd-MM-yyyy')
    surname = ui.surnameBox.text()
    name = ui.nameBox.text()
    fathername = ui.fathernameBox.text()
    carnum = ui.carnumBox.text()
    carBrand = ui.autoBrandBox.text()

    passDate = ui.passDateBox.date().toString('dd-MM-yyyy')
    correct = True
    if ui.isSingleBox.isChecked():
        passDate2 = passDate
    else:
        d1 = ui.passDateBox.date().toPyDate()
        d2 = ui.passDate2Box.date().toPyDate()
        if d1 > d2:
            errorTxt = "Дата окончания пропуска не может быть меньше даты выдачи"
            correct = False
        passDate2 = ui.passDate2Box.date().toString('dd-MM-yyyy')
    lEssential = [memoDate, surname, name, fathername, carnum, passDate, passDate2]
    for i in lEssential:
        if i == "":
            correct = False
            errorTxt= "Заполните все обязательные поля и даты"
    if carBrand == '':
        carBrand = '-'
    if memoId == '':
        memoId = '-'
    lFull = [memoId, memoDate, surname, name, fathername, carnum, carBrand, passDate, passDate2]
    if correct == True:
        memo = ",".join(lFull)
        db = open(dbPath, "a", encoding="utf-8")
        print("Added memo: " + memo)
        db.write(memo + '\n')
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Успех")
        msgbox.setInformativeText("Пропуск добавлен")
        msgbox.exec()
        db.close()
    else:
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Ошибка")
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setText(errorTxt)
        msgbox.exec()

def boxToggled():
    if ui.isSingleBox.isChecked():
        ui.passDate2Box.setEnabled(False)
    else:
        ui.passDate2Box.setEnabled(True)

ui.addPassBtn.clicked.connect(addMemo)
ui.isSingleBox.toggled.connect(boxToggled)

#main loop
sys.exit(app.exec_())
