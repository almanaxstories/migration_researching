# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kkwin3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kkwin3(object):
    def setupUi(self, kkwin3):
        kkwin3.setObjectName("kkwin3")
        kkwin3.setEnabled(True)
        kkwin3.resize(720, 297)
        kkwin3.setMinimumSize(QtCore.QSize(720, 297))
        kkwin3.setMaximumSize(QtCore.QSize(720, 297))
        kkwin3.setStyleSheet("background-color:rgb(241,222,255);")
        self.label = QtWidgets.QLabel(kkwin3)
        self.label.setGeometry(QtCore.QRect(50, 10, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(kkwin3)
        self.back.setGeometry(QtCore.QRect(130, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.next = QtWidgets.QPushButton(kkwin3)
        self.next.setGeometry(QtCore.QRect(470, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.label_14 = QtWidgets.QLabel(kkwin3)
        self.label_14.setGeometry(QtCore.QRect(40, 140, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.years = QtWidgets.QLineEdit(kkwin3)
        self.years.setEnabled(True)
        self.years.setGeometry(QtCore.QRect(270, 140, 121, 20))
        self.years.setText("")
        self.years.setAlignment(QtCore.Qt.AlignCenter)
        self.years.setObjectName("years")
        self.label_15 = QtWidgets.QLabel(kkwin3)
        self.label_15.setGeometry(QtCore.QRect(30, 80, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(kkwin3)
        self.label_16.setGeometry(QtCore.QRect(350, 80, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.retranslateUi(kkwin3)
        QtCore.QMetaObject.connectSlotsByName(kkwin3)

    def retranslateUi(self, kkwin3):
        _translate = QtCore.QCoreApplication.translate
        kkwin3.setWindowTitle(_translate("kkwin3", "Розрахунок3. Вхідні дані"))
        self.label.setText(_translate("kkwin3", "Розрахунок 3. Моделювання міграційних процесів України "))
        self.back.setText(_translate("kkwin3", "Назад"))
        self.next.setText(_translate("kkwin3", "Вперед"))
        self.label_14.setText(_translate("kkwin3", "Кількість років для розрахунку:"))
        self.label_15.setText(_translate("kkwin3", "*Основні дані для розрахунку вже включено."))
        self.label_16.setText(_translate("kkwin3", "Необхідно зазначити лише кі-сть років."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kkwin3 = QtWidgets.QDialog()
    ui = Ui_kkwin3()
    ui.setupUi(kkwin3)
    kkwin3.show()
    sys.exit(app.exec_())

