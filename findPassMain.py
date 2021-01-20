import sys

from PyQt5.QtCore import QDate
from findPass import Ui_findPassWindow
import os.path as path
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication


import configparser
my_config_parser = configparser.ConfigParser()
my_config_parser.read('carPasses.cfg')
payload = {
    'dbPath': my_config_parser.get('DEFAULT','dbPath')
}

app = QApplication(sys.argv)
findPassWindow = QMainWindow()
ui = Ui_findPassWindow()
ui.setupUi(findPassWindow)
findPassWindow.setFixedSize(findPassWindow.size())

dbPath=payload.get('dbPath')

if not path.isfile(dbPath):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("Ошибка")
    msgbox.setIcon(QMessageBox.Critical)
    msgbox.setText("Не обнаружена база данных или нет соединения с сервером.")
    ui.findBtn.setEnabled(False)
    msgbox.exec()

def btnClicked():

    carnum = ui.carnumBox.text().lower()
    if carnum == "":
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Ошибка")
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setText("Пустой номер")
        msgbox.exec()
    else:
        db = open(dbPath, 'r',encoding='utf-8')
        for line in reversed(db.readlines()):
            l=line.split(',')
            if l[5].lower() == carnum:
                print("Found: " + line)
                QDate.fromString(l[2],'dd-MM-yyyy')
                QDate.fromString(l[7],'dd-MM-yyyy')
                if l[8] != l[7]:
                    QDate.fromString(l[7], 'dd-MM-yyyy')
                
                ui.surnameBox.setText(l[2])
                ui.nameBox.setText(l[3])
                ui.fathernameBox.setText(l[4])
                ui.fromBox.setText(l[7])
                ui.toBox.setText(l[8])
                ui.autoBrandBox.setText(l[6])
                db.close()
                return
        db.close()

ui.findBtn.clicked.connect(btnClicked)

findPassWindow.show()
sys.exit(app.exec_())
