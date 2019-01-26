import sys
import random
from main import*
from kkwin1 import Ui_kkwin1
from aawin1 import Ui_aawin1
from aawin2 import Ui_aawin2
from aawin3 import Ui_aawin3
from aawin4 import Ui_aawin4
from aawin5 import Ui_aawin5
from fin1 import Ui_fin1
from kkwin2 import Ui_kkwin2
from fin2 import Ui_fin2
from kkwin3 import Ui_kkwin3
from fin3 import Ui_fin3
import numpy as np
from PyQt5 import QtWidgets,QtGui,QtCore
import xlwt




class prog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rozr1.clicked.connect(self.kk1dial)
        self.ui.rozr2.clicked.connect(self.kk2_dial)
        self.ui.rozr3.clicked.connect(self.kk3_dial)

    def kk1dial(self):
        self.newkk1win = QtWidgets.QDialog()
        self.kk1ui = Ui_kkwin1()
        self.kk1ui.setupUi(self.newkk1win)
        self.newkk1win.show()
        self.kk1ui.back.clicked.connect(self.show_main)
        self.kk1ui.next.clicked.connect(self.show_aa1n)
        myapp.hide()

    def show_main(self):
        myapp.show()
        self.newkk1win.hide()

    def show_aa1n(self):
        self.newaa1win = QtWidgets.QDialog()
        self.aa1ui = Ui_aawin1()
        self.aa1ui.setupUi(self.newaa1win)
        self.aa1ui.back.clicked.connect(self.show_kk1b)
        self.aa1ui.next.clicked.connect(self.show_aa2n)
        #self.aa1ui.next.clicked.connect(self.calc_fin1)
        self.newaa1win.show()
        self.newkk1win.hide()

    def show_kk1b(self):
        self.newkk1win.show()
        self.newaa1win.hide()

    def show_aa2n(self):
        self.newaa2win = QtWidgets.QDialog()
        self.aa2ui = Ui_aawin2()
        self.aa2ui.setupUi(self.newaa2win)
        self.aa2ui.back.clicked.connect(self.show_aa1b)
        self.aa2ui.next.clicked.connect(self.show_aa3n)
        self.newaa2win.show()
        self.newaa1win.hide()

    def show_aa1b(self):
        self.newaa2win.hide()
        self.newaa1win.show()

    def show_aa3n(self):
        self.newaa3win = QtWidgets.QDialog()
        self.aa3ui = Ui_aawin3()
        self.aa3ui.setupUi(self.newaa3win)
        self.aa3ui.back.clicked.connect(self.show_aa2b)
        self.aa3ui.next.clicked.connect(self.show_aa4n)
        self.newaa3win.show()
        self.newaa2win.hide()

    def show_aa2b(self):
        self.newaa2win.show()
        self.newaa3win.hide()

    def show_aa4n(self):
        self.newaa4win = QtWidgets.QDialog()
        self.aa4ui = Ui_aawin4()
        self.aa4ui.setupUi(self.newaa4win)
        self.aa4ui.back.clicked.connect(self.show_aa3b)
        self.aa4ui.next.clicked.connect(self.show_aa5n)
        self.newaa4win.show()
        self.newaa3win.hide()

    def show_aa3b(self):
        self.newaa3win.show()
        self.newaa4win.hide()

    def show_aa5n(self):
        self.newaa5win = QtWidgets.QDialog()
        self.aa5ui = Ui_aawin5()
        self.aa5ui.setupUi(self.newaa5win)
        self.aa5ui.back.clicked.connect(self.show_aa4b)
        self.aa5ui.next.clicked.connect(self.show_fin1n)
        self.newaa5win.show()
        self.newaa4win.hide()

    def show_aa4b(self):
        self.newaa4win.show()
        self.newaa5win.hide()

    def show_fin1n(self):
        self.newfin1win = QtWidgets.QDialog()
        self.fin1ui = Ui_fin1()
        self.fin1ui.setupUi(self.newfin1win)
        self.fin1ui.tomenu.clicked.connect(self.tomenu_fin1b)
        self.fin1ui.back.clicked.connect(self.show_aa5b)
        self.fin1ui.calc.clicked.connect(self.calc_fin1)
        self.newfin1win.show()
        self.newaa5win.hide()

    def show_aa5b(self):
        self.newaa5win.show()
        self.newfin1win.hide()

    def tomenu_fin1b(self):
        myapp.show()
        self.newfin1win.hide()

    def calc_fin1(self):
        try:
            kka = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            kka[0][0] = 1
            kka[0][1]= float(self.kk1ui.k1k2.text())
            kka[0][2] = float(self.kk1ui.k1k3.text())
            kka[0][3] = float(self.kk1ui.k1k4.text())
            kka[0][4] = float(self.kk1ui.k1k5.text())
            kka[1][0] = 1/kka[0][1]
            kka[1][1] = 1
            kka[1][2] = float(self.kk1ui.k2k3.text())
            kka[1][3] = float(self.kk1ui.k2k4.text())
            kka[1][4] = float(self.kk1ui.k2k5.text())
            kka[2][0] = 1/ kka[0][2]
            kka[2][1] = 1/kka[1][2]
            kka[2][2] = 1
            kka[2][3] = float(self.kk1ui.k3k4.text())
            kka[2][4] = float(self.kk1ui.k3k5.text())
            kka[3][0] = 1/kka[0][3]
            kka[3][1] = 1/kka[1][3]
            kka[3][2] = 1/kka[2][3]
            kka[3][3] = 1
            kka[3][4] = float(self.kk1ui.k4k5.text())
            kka[4][0] = 1/kka[0][4]
            kka[4][1] = 1/kka[1][4]
            kka[4][2] = 1/kka[2][4]
            kka[4][3] = 1/kka[3][4]
            kka[4][4] = 1
            srgk1t = kka[0][0]*kka[0][1]*kka[0][2]*kka[0][3]*kka[0][4]
            srgk1 = pow(srgk1t,1/5)
            srgk2t = kka[1][0] * kka[1][1] * kka[1][2] * kka[1][3] * kka[1][4]
            srgk2 = pow(srgk2t, 1 / 5)
            srgk3t = kka[2][0] * kka[2][1] * kka[2][2] * kka[2][3] * kka[2][4]
            srgk3 = pow(srgk3t, 1 / 5)
            srgk4t = kka[3][0] * kka[3][1] * kka[3][2] * kka[3][3] * kka[3][4]
            srgk4 = pow(srgk4t, 1 / 5)
            srgk5t = kka[4][0] * kka[4][1] * kka[4][2] * kka[4][3] * kka[4][4]
            srgk5 = pow(srgk5t, 1 / 5)
            sum1 = srgk1 + srgk2 + srgk3 + srgk4 + srgk5
            nsrgk1 = srgk1 / sum1
            nsrgk2 = srgk2 / sum1
            nsrgk3 = srgk3 / sum1
            nsrgk4 = srgk4 / sum1
            nsrgk5 = srgk5 / sum1

            aaa1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa1[0][0] = 1
            aaa1[0][1] = float(self.aa1ui.a1a2.text())
            aaa1[0][2] = float(self.aa1ui.a1a3.text())
            aaa1[0][3] = float(self.aa1ui.a1a4.text())
            aaa1[0][4] = float(self.aa1ui.a1a5.text())
            aaa1[1][0] = 1/aaa1[0][1]
            aaa1[1][1] = 1
            aaa1[1][2] = float(self.aa1ui.a2a3.text())
            aaa1[1][3] = float(self.aa1ui.a2a4.text())
            aaa1[1][4] = float(self.aa1ui.a2a5.text())
            aaa1[2][0] = 1 / aaa1[0][2]
            aaa1[2][1] = 1 / aaa1[1][2]
            aaa1[2][2] = 1
            aaa1[2][3] = float(self.aa1ui.a3a4.text())
            aaa1[2][4] = float(self.aa1ui.a3a5.text())
            aaa1[3][0] = 1 / aaa1[0][3]
            aaa1[3][1] = 1 / aaa1[1][3]
            aaa1[3][2] = 1 / aaa1[2][3]
            aaa1[3][3] = 1
            aaa1[3][4] = float(self.aa1ui.a4a5.text())
            aaa1[4][0] = 1 / aaa1[0][4]
            aaa1[4][1] = 1 / aaa1[1][4]
            aaa1[4][2] = 1 / aaa1[2][4]
            aaa1[4][3] = 1 / aaa1[3][4]
            aaa1[4][4] = 1
            srga11t = aaa1[0][0] * aaa1[0][1] * aaa1[0][2] * aaa1[0][3] * aaa1[0][4]
            srga11 = pow(srga11t, 1 / 5)
            srga12t = aaa1[1][0] * aaa1[1][1] * aaa1[1][2] * aaa1[1][3] * aaa1[1][4]
            srga12 = pow(srga12t, 1 / 5)
            srga13t = aaa1[2][0] * aaa1[2][1] * aaa1[2][2] * aaa1[2][3] * aaa1[2][4]
            srga13 = pow(srga13t, 1 / 5)
            srga14t = aaa1[3][0] * aaa1[3][1] *aaa1[3][2] * aaa1[3][3] * aaa1[3][4]
            srga14 = pow(srga14t, 1 / 5)
            srga15t = aaa1[4][0] * aaa1[4][1] * aaa1[4][2] * aaa1[4][3] * aaa1[4][4]
            srga15 = pow(srga15t, 1 / 5)
            sum2 = srga11 + srga12 + srga13 + srga14 + srga15
            nsrga11 = srga11 / sum2
            nsrga12 = srga12 / sum2
            nsrga13 = srga13 / sum2
            nsrga14 = srga14 / sum2
            nsrga15 = srga15 / sum2

            aaa2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa2[0][0] = 1
            aaa2[0][1] = float(self.aa2ui.a1a2.text())
            aaa2[0][2] = float(self.aa2ui.a1a3.text())
            aaa2[0][3] = float(self.aa2ui.a1a4.text())
            aaa2[0][4] = float(self.aa2ui.a1a5.text())
            aaa2[1][0] = 1 / aaa2[0][1]
            aaa2[1][1] = 1
            aaa2[1][2] = float(self.aa2ui.a2a3.text())
            aaa2[1][3] = float(self.aa2ui.a2a4.text())
            aaa2[1][4] = float(self.aa2ui.a2a5.text())
            aaa2[2][0] = 1 / aaa2[0][2]
            aaa2[2][1] = 1 / aaa2[1][2]
            aaa2[2][2] = 1
            aaa2[2][3] = float(self.aa2ui.a3a4.text())
            aaa2[2][4] = float(self.aa2ui.a3a5.text())
            aaa2[3][0] = 1 / aaa2[0][3]
            aaa2[3][1] = 1 / aaa2[1][3]
            aaa2[3][2] = 1 / aaa2[2][3]
            aaa2[3][3] = 1
            aaa2[3][4] = float(self.aa2ui.a4a5.text())
            aaa2[4][0] = 1 / aaa2[0][4]
            aaa2[4][1] = 1 / aaa2[1][4]
            aaa2[4][2] = 1 / aaa2[2][4]
            aaa2[4][3] = 1 / aaa2[3][4]
            aaa2[4][4] = 1
            srga21t = aaa2[0][0] * aaa2[0][1] * aaa2[0][2] * aaa2[0][3] * aaa2[0][4]
            srga21 = pow(srga21t, 1 / 5)
            srga22t = aaa2[1][0] * aaa2[1][1] * aaa2[1][2] * aaa2[1][3] * aaa2[1][4]
            srga22 = pow(srga22t, 1 / 5)
            srga23t = aaa2[2][0] * aaa2[2][1] * aaa2[2][2] * aaa2[2][3] * aaa2[2][4]
            srga23 = pow(srga23t, 1 / 5)
            srga24t = aaa2[3][0] * aaa2[3][1] * aaa2[3][2] * aaa2[3][3] * aaa2[3][4]
            srga24 = pow(srga24t, 1 / 5)
            srga25t = aaa2[4][0] * aaa2[4][1] * aaa2[4][2] * aaa2[4][3] * aaa2[4][4]
            srga25 = pow(srga25t, 1 / 5)
            sum3 = srga21 + srga22 + srga23 + srga24 + srga25
            nsrga21 = srga21 / sum3
            nsrga22 = srga22 / sum3
            nsrga23 = srga23 / sum3
            nsrga24 = srga24 / sum3
            nsrga25 = srga25 / sum3

            aaa3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa3[0][0] = 1
            aaa3[0][1] = float(self.aa3ui.a1a2.text())
            aaa3[0][2] = float(self.aa3ui.a1a3.text())
            aaa3[0][3] = float(self.aa3ui.a1a4.text())
            aaa3[0][4] = float(self.aa3ui.a1a5.text())
            aaa3[1][0] = 1 / aaa3[0][1]
            aaa3[1][1] = 1
            aaa3[1][2] = float(self.aa3ui.a2a3.text())
            aaa3[1][3] = float(self.aa3ui.a2a4.text())
            aaa3[1][4] = float(self.aa3ui.a2a5.text())
            aaa3[2][0] = 1 / aaa3[0][2]
            aaa3[2][1] = 1 / aaa3[1][2]
            aaa3[2][2] = 1
            aaa3[2][3] = float(self.aa3ui.a3a4.text())
            aaa3[2][4] = float(self.aa3ui.a3a5.text())
            aaa3[3][0] = 1 / aaa3[0][3]
            aaa3[3][1] = 1 / aaa3[1][3]
            aaa3[3][2] = 1 / aaa3[2][3]
            aaa3[3][3] = 1
            aaa3[3][4] = float(self.aa3ui.a4a5.text())
            aaa3[4][0] = 1 / aaa3[0][4]
            aaa3[4][1] = 1 / aaa3[1][4]
            aaa3[4][2] = 1 / aaa3[2][4]
            aaa3[4][3] = 1 / aaa3[3][4]
            aaa3[4][4] = 1
            srga31t = aaa3[0][0] * aaa3[0][1] * aaa3[0][2] * aaa3[0][3] * aaa3[0][4]
            srga31 = pow(srga31t, 1 / 5)
            srga32t = aaa3[1][0] * aaa3[1][1] * aaa3[1][2] * aaa3[1][3] * aaa3[1][4]
            srga32 = pow(srga32t, 1 / 5)
            srga33t = aaa3[2][0] * aaa3[2][1] * aaa3[2][2] * aaa3[2][3] * aaa3[2][4]
            srga33 = pow(srga33t, 1 / 5)
            srga34t = aaa3[3][0] * aaa3[3][1] * aaa3[3][2] * aaa3[3][3] * aaa3[3][4]
            srga34 = pow(srga34t, 1 / 5)
            srga35t = aaa3[4][0] * aaa3[4][1] * aaa3[4][2] * aaa1[4][3] * aaa3[4][4]
            srga35 = pow(srga35t, 1 / 5)
            sum4 = srga31 + srga32 + srga33 + srga34 + srga35
            nsrga31 = srga31 / sum4
            nsrga32 = srga32 / sum4
            nsrga33 = srga33 / sum4
            nsrga34 = srga34 / sum4
            nsrga35 = srga35 / sum4

            aaa4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa4[0][0] = 1
            aaa4[0][1] = float(self.aa4ui.a1a2.text())
            aaa4[0][2] = float(self.aa4ui.a1a3.text())
            aaa4[0][3] = float(self.aa4ui.a1a4.text())
            aaa4[0][4] = float(self.aa4ui.a1a5.text())
            aaa4[1][0] = 1 / aaa4[0][1]
            aaa4[1][1] = 1
            aaa4[1][2] = float(self.aa4ui.a2a3.text())
            aaa4[1][3] = float(self.aa4ui.a2a4.text())
            aaa4[1][4] = float(self.aa4ui.a2a5.text())
            aaa4[2][0] = 1 / aaa4[0][2]
            aaa4[2][1] = 1 / aaa4[1][2]
            aaa4[2][2] = 1
            aaa4[2][3] = float(self.aa4ui.a3a4.text())
            aaa4[2][4] = float(self.aa4ui.a3a5.text())
            aaa4[3][0] = 1 / aaa4[0][3]
            aaa4[3][1] = 1 / aaa4[1][3]
            aaa4[3][2] = 1 / aaa4[2][3]
            aaa4[3][3] = 1
            aaa4[3][4] = float(self.aa4ui.a4a5.text())
            aaa4[4][0] = 1 / aaa4[0][4]
            aaa4[4][1] = 1 / aaa4[1][4]
            aaa4[4][2] = 1 / aaa4[2][4]
            aaa4[4][3] = 1 / aaa4[3][4]
            aaa4[4][4] = 1
            srga41t = aaa4[0][0] * aaa4[0][1] * aaa4[0][2] * aaa4[0][3] * aaa4[0][4]
            srga41 = pow(srga41t, 1 / 5)
            srga42t = aaa4[1][0] * aaa4[1][1] * aaa4[1][2] * aaa4[1][3] * aaa4[1][4]
            srga42 = pow(srga42t, 1 / 5)
            srga43t = aaa4[2][0] * aaa4[2][1] * aaa4[2][2] * aaa4[2][3] * aaa4[2][4]
            srga43 = pow(srga43t, 1 / 5)
            srga44t = aaa4[3][0] * aaa4[3][1] * aaa4[3][2] * aaa4[3][3] * aaa4[3][4]
            srga44 = pow(srga44t, 1 / 5)
            srga45t = aaa4[4][0] * aaa4[4][1] * aaa4[4][2] * aaa4[4][3] * aaa4[4][4]
            srga45 = pow(srga45t, 1 / 5)
            sum5 = srga41 + srga42 + srga43 + srga44 + srga45
            nsrga41 = srga41 / sum5
            nsrga42 = srga42 / sum5
            nsrga43 = srga43 / sum5
            nsrga44 = srga44 / sum5
            nsrga45 = srga45 / sum5

            aaa5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa5[0][0] = 1
            aaa5[0][1] = float(self.aa5ui.a1a2.text())
            aaa5[0][2] = float(self.aa5ui.a1a3.text())
            aaa5[0][3] = float(self.aa5ui.a1a4.text())
            aaa5[0][4] = float(self.aa5ui.a1a5.text())
            aaa5[1][0] = 1 / aaa5[0][1]
            aaa5[1][1] = 1
            aaa5[1][2] = float(self.aa5ui.a2a3.text())
            aaa5[1][3] = float(self.aa5ui.a2a4.text())
            aaa5[1][4] = float(self.aa5ui.a2a5.text())
            aaa5[2][0] = 1 / aaa5[0][2]
            aaa5[2][1] = 1 / aaa5[1][2]
            aaa5[2][2] = 1
            aaa5[2][3] = float(self.aa5ui.a3a4.text())
            aaa5[2][4] = float(self.aa5ui.a3a5.text())
            aaa5[3][0] = 1 / aaa5[0][3]
            aaa5[3][1] = 1 / aaa5[1][3]
            aaa5[3][2] = 1 / aaa5[2][3]
            aaa5[3][3] = 1
            aaa5[3][4] = float(self.aa5ui.a4a5.text())
            aaa5[4][0] = 1 / aaa5[0][4]
            aaa5[4][1] = 1 / aaa5[1][4]
            aaa5[4][2] = 1 / aaa5[2][4]
            aaa5[4][3] = 1 / aaa5[3][4]
            aaa5[4][4] = 1
            srga51t = aaa5[0][0] * aaa5[0][1] * aaa5[0][2] * aaa5[0][3] * aaa5[0][4]
            srga51 = pow(srga51t, 1 / 5)
            srga52t = aaa5[1][0] * aaa5[1][1] * aaa5[1][2] * aaa5[1][3] * aaa5[1][4]
            srga52 = pow(srga52t, 1 / 5)
            srga53t = aaa5[2][0] * aaa5[2][1] * aaa5[2][2] * aaa5[2][3] * aaa5[2][4]
            srga53 = pow(srga53t, 1 / 5)
            srga54t = aaa5[3][0] * aaa5[3][1] * aaa5[3][2] * aaa5[3][3] * aaa5[3][4]
            srga54 = pow(srga54t, 1 / 5)
            srga55t = aaa5[4][0] * aaa5[4][1] * aaa5[4][2] * aaa5[4][3] * aaa5[4][4]
            srga55 = pow(srga55t, 1 / 5)
            sum6 = srga51 + srga52 + srga53 + srga54 + srga55
            nsrga51 = srga51 / sum6
            nsrga52 = srga52 / sum6
            nsrga53 = srga53 / sum6
            nsrga54 = srga54 / sum6
            nsrga55 = srga55 / sum6

            gf1 = nsrga11 * nsrgk1 + nsrga21 * nsrgk2 + nsrga31 * nsrgk3 + nsrga41 * nsrgk4 + nsrga51 * nsrgk5
            gf2 = nsrga12 * nsrgk1 + nsrga22 * nsrgk2 + nsrga32 * nsrgk3 + nsrga42 * nsrgk4 + nsrga52 * nsrgk5
            gf3 = nsrga13 * nsrgk1 + nsrga23 * nsrgk2 + nsrga33 * nsrgk3 + nsrga43 * nsrgk4 + nsrga53 * nsrgk5
            gf4 = nsrga14 * nsrgk1 + nsrga24 * nsrgk2 + nsrga34 * nsrgk3 + nsrga44 * nsrgk4 + nsrga54 * nsrgk5
            gf5 = nsrga15 * nsrgk1 + nsrga25 * nsrgk2 + nsrga35 * nsrgk3 + nsrga45 * nsrgk4 + nsrga55 * nsrgk5

            pgf1 = round(gf1, 3)
            pgf2 = round(gf2, 3)
            pgf3 = round(gf3, 3)
            pgf4 = round(gf4, 3)
            pgf5 = round(gf5, 3)

            self.fin1ui.a1.setText(str(pgf1))
            self.fin1ui.a2.setText(str(pgf2))
            self.fin1ui.a3.setText(str(pgf3))
            self.fin1ui.a4.setText(str(pgf4))
            self.fin1ui.a5.setText(str(pgf5))





        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Input error!")
            msg.setText("Check input data please")
            msg.setIcon(msg.Warning)
            msg.exec()

    def kk2_dial(self):
        self.newkk2win = QtWidgets.QDialog()
        self.newkk2ui = Ui_kkwin2()
        self.newkk2ui.setupUi(self.newkk2win)
        self.newkk2ui.back.clicked.connect(self.show_main2)
        self.newkk2ui.next.clicked.connect(self.show_aa1cn)
        self.newkk2win.show()
        myapp.hide()

    def show_main2(self):
        myapp.show()
        self.newkk2win.hide()

    def show_aa1cn(self):
        self.newaa1cwin = QtWidgets.QDialog()
        self.newaa1cui = Ui_aawin1()
        self.newaa1cui.setupUi(self.newaa1cwin)
        self.newaa1cui.back.clicked.connect(self.show_kk2b)
        self.newaa1cui.next.clicked.connect(self.show_aa2cn)
        self.newaa1cwin.show()
        self.newkk2win.hide()

    def show_kk2b(self):
        self.newkk2win.show()
        self.newaa1cwin.hide()

    def show_aa2cn(self):
        self.newaa2cwin = QtWidgets.QDialog()
        self.newaa2cui = Ui_aawin2()
        self.newaa2cui.setupUi(self.newaa2cwin)
        self.newaa2cui.back.clicked.connect(self.show_aa1cb)
        self.newaa2cui.next.clicked.connect(self.show_aa3cn)
        self.newaa2cwin.show()
        self.newaa1cwin.hide()

    def show_aa1cb(self):
        self.newaa1cwin.show()
        self.newaa2cwin.hide()

    def show_aa3cn(self):
        self.newaa3cwin = QtWidgets.QDialog()
        self.newaa3cui = Ui_aawin3()
        self.newaa3cui.setupUi(self.newaa3cwin)
        self.newaa3cui.back.clicked.connect(self.show_aa2cb)
        self.newaa3cui.next.clicked.connect(self.show_aa4cn)
        self.newaa3cwin.show()
        self.newaa2cwin.hide()

    def show_aa2cb(self):
        self.newaa2cwin.show()
        self.newaa3cwin.hide()

    def show_aa4cn(self):
        self.newaa4cwin = QtWidgets.QDialog()
        self.newaa4cui = Ui_aawin4()
        self.newaa4cui.setupUi(self.newaa4cwin)
        self.newaa4cui.back.clicked.connect(self.show_aa3cb)
        self.newaa4cui.next.clicked.connect(self.show_aa5cn)
        self.newaa4cwin.show()
        self.newaa3cwin.hide()

    def show_aa3cb(self):
        self.newaa3cwin.show()
        self.newaa4cwin.hide()

    def show_aa5cn(self):
        self.newaa5cwin = QtWidgets.QDialog()
        self.newaa5cui = Ui_aawin5()
        self.newaa5cui.setupUi(self.newaa5cwin)
        self.newaa5cui.back.clicked.connect(self.show_aa4cb)
        self.newaa5cui.next.clicked.connect(self.show_fin2n)
        self.newaa5cwin.show()
        self.newaa4cwin.hide()

    def show_aa4cb(self):
        self.newaa4cwin.show()
        self.newaa5cwin.hide()

    def show_fin2n(self):
        self.fin2win = QtWidgets.QDialog()
        self.fin2ui = Ui_fin2()
        self.fin2ui.setupUi(self.fin2win)
        self.fin2ui.back.clicked.connect(self.show_aa5cb)
        self.fin2ui.tomenu.clicked.connect(self.show_main3)
        self.fin2ui.calc.clicked.connect(self.calc_fin2)
        #self.fin2ui.plot.clicked.connect(self.plot1)
        self.fin2win.show()
        self.newaa5cwin.hide()

    def show_aa5cb(self):
        self.newaa5cwin.show()
        self.fin2win.hide()

    def show_main3(self):
        myapp.show()
        self.fin2win.hide()
        self.mass = [3,5,7]

    def calc_fin2(self):
        try:
            aaa1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa1[0][0] = 1
            aaa1[0][1] = float(self.newaa1cui.a1a2.text())
            aaa1[0][2] = float(self.newaa1cui.a1a3.text())
            aaa1[0][3] = float(self.newaa1cui.a1a4.text())
            aaa1[0][4] = float(self.newaa1cui.a1a5.text())
            aaa1[1][0] = 1 / aaa1[0][1]
            aaa1[1][1] = 1
            aaa1[1][2] = float(self.newaa1cui.a2a3.text())
            aaa1[1][3] = float(self.newaa1cui.a2a4.text())
            aaa1[1][4] = float(self.newaa1cui.a2a5.text())
            aaa1[2][0] = 1 / aaa1[0][2]
            aaa1[2][1] = 1 / aaa1[1][2]
            aaa1[2][2] = 1
            aaa1[2][3] = float(self.newaa1cui.a3a4.text())
            aaa1[2][4] = float(self.newaa1cui.a3a5.text())
            aaa1[3][0] = 1 / aaa1[0][3]
            aaa1[3][1] = 1 / aaa1[1][3]
            aaa1[3][2] = 1 / aaa1[2][3]
            aaa1[3][3] = 1
            aaa1[3][4] = float(self.newaa1cui.a4a5.text())
            aaa1[4][0] = 1 / aaa1[0][4]
            aaa1[4][1] = 1 / aaa1[1][4]
            aaa1[4][2] = 1 / aaa1[2][4]
            aaa1[4][3] = 1 / aaa1[3][4]
            aaa1[4][4] = 1
            srga11t = aaa1[0][0] * aaa1[0][1] * aaa1[0][2] * aaa1[0][3] * aaa1[0][4]
            srga11 = pow(srga11t, 1 / 5)
            srga12t = aaa1[1][0] * aaa1[1][1] * aaa1[1][2] * aaa1[1][3] * aaa1[1][4]
            srga12 = pow(srga12t, 1 / 5)
            srga13t = aaa1[2][0] * aaa1[2][1] * aaa1[2][2] * aaa1[2][3] * aaa1[2][4]
            srga13 = pow(srga13t, 1 / 5)
            srga14t = aaa1[3][0] * aaa1[3][1] * aaa1[3][2] * aaa1[3][3] * aaa1[3][4]
            srga14 = pow(srga14t, 1 / 5)
            srga15t = aaa1[4][0] * aaa1[4][1] * aaa1[4][2] * aaa1[4][3] * aaa1[4][4]
            srga15 = pow(srga15t, 1 / 5)
            sum2 = srga11 + srga12 + srga13 + srga14 + srga15
            nsrga11 = srga11 / sum2
            nsrga12 = srga12 / sum2
            nsrga13 = srga13 / sum2
            nsrga14 = srga14 / sum2
            nsrga15 = srga15 / sum2



            aaa2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa2[0][0] = 1
            aaa2[0][1] = float(self.newaa2cui.a1a2.text())
            aaa2[0][2] = float(self.newaa2cui.a1a3.text())
            aaa2[0][3] = float(self.newaa2cui.a1a4.text())
            aaa2[0][4] = float(self.newaa2cui.a1a5.text())
            aaa2[1][0] = 1 / aaa2[0][1]
            aaa2[1][1] = 1
            aaa2[1][2] = float(self.newaa2cui.a2a3.text())
            aaa2[1][3] = float(self.newaa2cui.a2a4.text())
            aaa2[1][4] = float(self.newaa2cui.a2a5.text())
            aaa2[2][0] = 1 / aaa2[0][2]
            aaa2[2][1] = 1 / aaa2[1][2]
            aaa2[2][2] = 1
            aaa2[2][3] = float(self.newaa2cui.a3a4.text())
            aaa2[2][4] = float(self.newaa2cui.a3a5.text())
            aaa2[3][0] = 1 / aaa2[0][3]
            aaa2[3][1] = 1 / aaa2[1][3]
            aaa2[3][2] = 1 / aaa2[2][3]
            aaa2[3][3] = 1
            aaa2[3][4] = float(self.newaa2cui.a4a5.text())
            aaa2[4][0] = 1 / aaa2[0][4]
            aaa2[4][1] = 1 / aaa2[1][4]
            aaa2[4][2] = 1 / aaa2[2][4]
            aaa2[4][3] = 1 / aaa2[3][4]
            aaa2[4][4] = 1
            srga21t = aaa2[0][0] * aaa2[0][1] * aaa2[0][2] * aaa2[0][3] * aaa2[0][4]
            srga21 = pow(srga21t, 1 / 5)
            srga22t = aaa2[1][0] * aaa2[1][1] * aaa2[1][2] * aaa2[1][3] * aaa2[1][4]
            srga22 = pow(srga22t, 1 / 5)
            srga23t = aaa2[2][0] * aaa2[2][1] * aaa2[2][2] * aaa2[2][3] * aaa2[2][4]
            srga23 = pow(srga23t, 1 / 5)
            srga24t = aaa2[3][0] * aaa2[3][1] * aaa2[3][2] * aaa2[3][3] * aaa2[3][4]
            srga24 = pow(srga24t, 1 / 5)
            srga25t = aaa2[4][0] * aaa2[4][1] * aaa2[4][2] * aaa2[4][3] * aaa2[4][4]
            srga25 = pow(srga25t, 1 / 5)
            sum3 = srga21 + srga22 + srga23 + srga24 + srga25
            nsrga21 = srga21 / sum3
            nsrga22 = srga22 / sum3
            nsrga23 = srga23 / sum3
            nsrga24 = srga24 / sum3
            nsrga25 = srga25 / sum3

            aaa3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa3[0][0] = 1
            aaa3[0][1] = float(self.newaa3cui.a1a2.text())
            aaa3[0][2] = float(self.newaa3cui.a1a3.text())
            aaa3[0][3] = float(self.newaa3cui.a1a4.text())
            aaa3[0][4] = float(self.newaa3cui.a1a5.text())
            aaa3[1][0] = 1 / aaa3[0][1]
            aaa3[1][1] = 1
            aaa3[1][2] = float(self.newaa3cui.a2a3.text())
            aaa3[1][3] = float(self.newaa3cui.a2a4.text())
            aaa3[1][4] = float(self.newaa3cui.a2a5.text())
            aaa3[2][0] = 1 / aaa3[0][2]
            aaa3[2][1] = 1 / aaa3[1][2]
            aaa3[2][2] = 1
            aaa3[2][3] = float(self.newaa3cui.a3a4.text())
            aaa3[2][4] = float(self.newaa3cui.a3a5.text())
            aaa3[3][0] = 1 / aaa3[0][3]
            aaa3[3][1] = 1 / aaa3[1][3]
            aaa3[3][2] = 1 / aaa3[2][3]
            aaa3[3][3] = 1
            aaa3[3][4] = float(self.newaa3cui.a4a5.text())
            aaa3[4][0] = 1 / aaa3[0][4]
            aaa3[4][1] = 1 / aaa3[1][4]
            aaa3[4][2] = 1 / aaa3[2][4]
            aaa3[4][3] = 1 / aaa3[3][4]
            aaa3[4][4] = 1
            srga31t = aaa3[0][0] * aaa3[0][1] * aaa3[0][2] * aaa3[0][3] * aaa3[0][4]
            srga31 = pow(srga31t, 1 / 5)
            srga32t = aaa3[1][0] * aaa3[1][1] * aaa3[1][2] * aaa3[1][3] * aaa3[1][4]
            srga32 = pow(srga32t, 1 / 5)
            srga33t = aaa3[2][0] * aaa3[2][1] * aaa3[2][2] * aaa3[2][3] * aaa3[2][4]
            srga33 = pow(srga33t, 1 / 5)
            srga34t = aaa3[3][0] * aaa3[3][1] * aaa3[3][2] * aaa3[3][3] * aaa3[3][4]
            srga34 = pow(srga34t, 1 / 5)
            srga35t = aaa3[4][0] * aaa3[4][1] * aaa3[4][2] * aaa3[4][3] * aaa3[4][4]
            srga35 = pow(srga35t, 1 / 5)
            sum4 = srga31 + srga32 + srga33 + srga34 + srga35
            nsrga31 = srga31 / sum4
            nsrga32 = srga32 / sum4
            nsrga33 = srga33 / sum4
            nsrga34 = srga34 / sum4
            nsrga35 = srga35 / sum4

            aaa4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa4[0][0] = 1
            aaa4[0][1] = float(self.newaa4cui.a1a2.text())
            aaa4[0][2] = float(self.newaa4cui.a1a3.text())
            aaa4[0][3] = float(self.newaa4cui.a1a4.text())
            aaa4[0][4] = float(self.newaa4cui.a1a5.text())
            aaa4[1][0] = 1 / aaa4[0][1]
            aaa4[1][1] = 1
            aaa4[1][2] = float(self.newaa4cui.a2a3.text())
            aaa4[1][3] = float(self.newaa4cui.a2a4.text())
            aaa4[1][4] = float(self.newaa4cui.a2a5.text())
            aaa4[2][0] = 1 / aaa4[0][2]
            aaa4[2][1] = 1 / aaa4[1][2]
            aaa4[2][2] = 1
            aaa4[2][3] = float(self.newaa4cui.a3a4.text())
            aaa4[2][4] = float(self.newaa4cui.a3a5.text())
            aaa4[3][0] = 1 / aaa4[0][3]
            aaa4[3][1] = 1 / aaa4[1][3]
            aaa4[3][2] = 1 / aaa4[2][3]
            aaa4[3][3] = 1
            aaa4[3][4] = float(self.newaa4cui.a4a5.text())
            aaa4[4][0] = 1 / aaa4[0][4]
            aaa4[4][1] = 1 / aaa4[1][4]
            aaa4[4][2] = 1 / aaa4[2][4]
            aaa4[4][3] = 1 / aaa4[3][4]
            aaa4[4][4] = 1
            srga41t = aaa4[0][0] * aaa4[0][1] * aaa4[0][2] * aaa4[0][3] * aaa4[0][4]
            srga41 = pow(srga41t, 1 / 5)
            srga42t = aaa4[1][0] * aaa4[1][1] * aaa4[1][2] * aaa4[1][3] * aaa4[1][4]
            srga42 = pow(srga42t, 1 / 5)
            srga43t = aaa4[2][0] * aaa4[2][1] * aaa4[2][2] * aaa4[2][3] * aaa4[2][4]
            srga43 = pow(srga43t, 1 / 5)
            srga44t = aaa4[3][0] * aaa4[3][1] * aaa4[3][2] * aaa4[3][3] * aaa4[3][4]
            srga44 = pow(srga44t, 1 / 5)
            srga45t = aaa4[4][0] * aaa4[4][1] * aaa4[4][2] * aaa4[4][3] * aaa4[4][4]
            srga45 = pow(srga45t, 1 / 5)
            sum5 = srga41 + srga42 + srga43 + srga44 + srga45
            nsrga41 = srga41 / sum5
            nsrga42 = srga42 / sum5
            nsrga43 = srga43 / sum5
            nsrga44 = srga44 / sum5
            nsrga45 = srga45 / sum5

            aaa5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa5[0][0] = 1
            aaa5[0][1] = float(self.newaa5cui.a1a2.text())
            aaa5[0][2] = float(self.newaa5cui.a1a3.text())
            aaa5[0][3] = float(self.newaa5cui.a1a4.text())
            aaa5[0][4] = float(self.newaa5cui.a1a5.text())
            aaa5[1][0] = 1 / aaa5[0][1]
            aaa5[1][1] = 1
            aaa5[1][2] = float(self.newaa5cui.a2a3.text())
            aaa5[1][3] = float(self.newaa5cui.a2a4.text())
            aaa5[1][4] = float(self.newaa5cui.a2a5.text())
            aaa5[2][0] = 1 / aaa5[0][2]
            aaa5[2][1] = 1 / aaa5[1][2]
            aaa5[2][2] = 1
            aaa5[2][3] = float(self.newaa5cui.a3a4.text())
            aaa5[2][4] = float(self.newaa5cui.a3a5.text())
            aaa5[3][0] = 1 / aaa5[0][3]
            aaa5[3][1] = 1 / aaa5[1][3]
            aaa5[3][2] = 1 / aaa5[2][3]
            aaa5[3][3] = 1
            aaa5[3][4] = float(self.newaa5cui.a4a5.text())
            aaa5[4][0] = 1 / aaa5[0][4]
            aaa5[4][1] = 1 / aaa5[1][4]
            aaa5[4][2] = 1 / aaa5[2][4]
            aaa5[4][3] = 1 / aaa5[3][4]
            aaa5[4][4] = 1
            srga51t = aaa5[0][0] * aaa5[0][1] * aaa5[0][2] * aaa5[0][3] * aaa5[0][4]
            srga51 = pow(srga51t, 1 / 5)
            srga52t = aaa5[1][0] * aaa5[1][1] * aaa5[1][2] * aaa5[1][3] * aaa5[1][4]
            srga52 = pow(srga52t, 1 / 5)
            srga53t = aaa5[2][0] * aaa5[2][1] * aaa5[2][2] * aaa5[2][3] * aaa5[2][4]
            srga53 = pow(srga53t, 1 / 5)
            srga54t = aaa5[3][0] * aaa5[3][1] * aaa5[3][2] * aaa5[3][3] * aaa5[3][4]
            srga54 = pow(srga54t, 1 / 5)
            srga55t = aaa5[4][0] * aaa5[4][1] * aaa5[4][2] * aaa5[4][3] * aaa5[4][4]
            srga55 = pow(srga55t, 1 / 5)
            sum6 = srga51 + srga52 + srga53 + srga54 + srga55
            nsrga51 = srga51 / sum6
            nsrga52 = srga52 / sum6
            nsrga53 = srga53 / sum6
            nsrga54 = srga54 / sum6
            nsrga55 = srga55 / sum6

            alt1 = 0
            alt2 = 0
            alt3 = 0
            alt4 = 0
            alt5 = 0
            tm = 0

            t = float(self.newkk2ui.total.text())
            p = float(self.newkk2ui.pot.text())
            b = float(self.newkk2ui.born.text())
            y = int(self.newkk2ui.years.text())

            total = t
            potm = p
            born = b
            years = y

            for i in range (years):
                potm = total*p
                born = total*b
                v = int(potm)
                tm = tm + potm

                for j in range (v):

                    nsrgk1 = random.uniform(0.1, 0.9)
                    nsrgk2 = random.uniform(0.1, 0.9)
                    nsrgk3 = random.uniform(0.1, 0.9)
                    nsrgk4 = random.uniform(0.1, 0.9)
                    nsrgk5 = random.uniform(0.1, 0.9)
                    gf1 = nsrga11 * nsrgk1 + nsrga21 * nsrgk2 + nsrga31 * nsrgk3 + nsrga41 * nsrgk4 + nsrga51 * nsrgk5
                    gf2 = nsrga12 * nsrgk1 + nsrga22 * nsrgk2 + nsrga32 * nsrgk3 + nsrga42 * nsrgk4 + nsrga52 * nsrgk5
                    gf3 = nsrga13 * nsrgk1 + nsrga23 * nsrgk2 + nsrga33 * nsrgk3 + nsrga43 * nsrgk4 + nsrga53 * nsrgk5
                    gf4 = nsrga14 * nsrgk1 + nsrga24 * nsrgk2 + nsrga34 * nsrgk3 + nsrga44 * nsrgk4 + nsrga54 * nsrgk5
                    gf5 = nsrga15 * nsrgk1 + nsrga25 * nsrgk2 + nsrga35 * nsrgk3 + nsrga45 * nsrgk4 + nsrga55 * nsrgk5
                    gp = np.array([0, 0, 0, 0, 0], float)
                    gp[0] = gf1
                    gp[1] = gf2
                    gp[2] = gf3
                    gp[3] = gf4
                    gp[4] = gf5

                    maxi = np.argmax(gp)

                    if maxi == 0:
                        alt1 = alt1 + 1
                    elif maxi == 1:
                        alt2 = alt2 + 1
                    elif maxi == 2:
                        alt3 = alt3 + 1
                    elif maxi == 3:
                        alt4 = alt4 + 1
                    else:
                        alt5 += 1
                total = total - potm
                total = total + born

            self.fin2ui.s1.setText(str(alt1))
            self.fin2ui.s2.setText(str(alt2))
            self.fin2ui.s3.setText(str(alt3))
            self.fin2ui.s4.setText(str(alt4))
            self.fin2ui.s5.setText(str(alt5))
            self.fin2ui.total.setText(str(round(total, 2)))
            self.fin2ui.tm.setText(str(round(tm,2)))

        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Помилка вводу")
            msg.setText("Перевірте правильність вхідних даних")
            msg.setIcon(msg.Warning)
            msg.exec()



    def kk3_dial(self):
        self.kk3dialwin = QtWidgets.QDialog()
        self.kk3dialui = Ui_kkwin3()
        self.kk3dialui.setupUi(self.kk3dialwin)
        self.kk3dialui.back.clicked.connect(self.show_main4)
        self.kk3dialui.next.clicked.connect(self.show_fin3)
        self.kk3dialwin.show()
        myapp.hide()

    def show_main4(self):
        myapp.show()
        self.kk3dialwin.hide()

    def show_fin3(self):
        self.fin3win = QtWidgets.QDialog()
        self.fin3ui = Ui_fin3()
        self.fin3ui.setupUi(self.fin3win)
        self.fin3ui.back.clicked.connect(self.show_kk3b)
        self.fin3ui.tomenu.clicked.connect(self.tomenu_fin3)
        self.fin3ui.calc.clicked.connect(self.calc_fin3)
        self.fin3win.show()
        self.kk3dialwin.hide()

    def show_kk3b(self):
        self.kk3dialwin.show()
        self.fin3win.hide()

    def tomenu_fin3(self):
        myapp.show()
        self.fin3win.hide()



    def calc_fin3(self):
        try:
            aaa1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa1[0][0] = 1
            aaa1[0][1] = 1.05
            aaa1[0][2] = 0.97
            aaa1[0][3] = 1.25
            aaa1[0][4] = 0.99
            aaa1[1][0] = 0.94
            aaa1[1][1] = 1
            aaa1[1][2] = 0.92
            aaa1[1][3] = 1.18
            aaa1[1][4] = 0.93
            aaa1[2][0] = 1.02
            aaa1[2][1] = 1.08
            aaa1[2][2] = 1
            aaa1[2][3] = 1.28
            aaa1[2][4] = 1.01
            aaa1[3][0] = 0.79
            aaa1[3][1] = 0.84
            aaa1[3][2] = 0.77
            aaa1[3][3] = 1
            aaa1[3][4] = 0.79
            aaa1[4][0] = 1
            aaa1[4][1] = 1.06
            aaa1[4][2] = 0.98
            aaa1[4][3] = 1.26
            aaa1[4][4] = 1
            srga11t = aaa1[0][0] * aaa1[0][1] * aaa1[0][2] * aaa1[0][3] * aaa1[0][4]
            srga11 = pow(srga11t, 1 / 5)
            srga12t = aaa1[1][0] * aaa1[1][1] * aaa1[1][2] * aaa1[1][3] * aaa1[1][4]
            srga12 = pow(srga12t, 1 / 5)
            srga13t = aaa1[2][0] * aaa1[2][1] * aaa1[2][2] * aaa1[2][3] * aaa1[2][4]
            srga13 = pow(srga13t, 1 / 5)
            srga14t = aaa1[3][0] * aaa1[3][1] * aaa1[3][2] * aaa1[3][3] * aaa1[3][4]
            srga14 = pow(srga14t, 1 / 5)
            srga15t = aaa1[4][0] * aaa1[4][1] * aaa1[4][2] * aaa1[4][3] * aaa1[4][4]
            srga15 = pow(srga15t, 1 / 5)
            sum2 = srga11 + srga12 + srga13 + srga14 + srga15
            nsrga11 = srga11 / sum2
            nsrga12 = srga12 / sum2
            nsrga13 = srga13 / sum2
            nsrga14 = srga14 / sum2
            nsrga15 = srga15 / sum2



            aaa2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa2[0][0] = 1
            aaa2[0][1] = 0.93
            aaa2[0][2] = 0.98
            aaa2[0][3] = 1.09
            aaa2[0][4] = 1
            aaa2[1][0] = 1.06
            aaa2[1][1] = 1
            aaa2[1][2] = 1.05
            aaa2[1][3] = 1.16
            aaa2[1][4] = 1.06
            aaa2[2][0] = 1.01
            aaa2[2][1] = 0.95
            aaa2[2][2] = 1
            aaa2[2][3] = 1.11
            aaa2[2][4] = 1.01
            aaa2[3][0] = 0.91
            aaa2[3][1] = 0.85
            aaa2[3][2] = 0.89
            aaa2[3][3] = 1
            aaa2[3][4] = 0.91
            aaa2[4][0] = 0.99
            aaa2[4][1] = 0.93
            aaa2[4][2] = 0.98
            aaa2[4][3] = 1.09
            aaa2[4][4] = 1
            srga21t = aaa2[0][0] * aaa2[0][1] * aaa2[0][2] * aaa2[0][3] * aaa2[0][4]
            srga21 = pow(srga21t, 1 / 5)
            srga22t = aaa2[1][0] * aaa2[1][1] * aaa2[1][2] * aaa2[1][3] * aaa2[1][4]
            srga22 = pow(srga22t, 1 / 5)
            srga23t = aaa2[2][0] * aaa2[2][1] * aaa2[2][2] * aaa2[2][3] * aaa2[2][4]
            srga23 = pow(srga23t, 1 / 5)
            srga24t = aaa2[3][0] * aaa2[3][1] * aaa2[3][2] * aaa2[3][3] * aaa2[3][4]
            srga24 = pow(srga24t, 1 / 5)
            srga25t = aaa2[4][0] * aaa2[4][1] * aaa2[4][2] * aaa2[4][3] * aaa2[4][4]
            srga25 = pow(srga25t, 1 / 5)
            sum3 = srga21 + srga22 + srga23 + srga24 + srga25
            nsrga21 = srga21 / sum3
            nsrga22 = srga22 / sum3
            nsrga23 = srga23 / sum3
            nsrga24 = srga24 / sum3
            nsrga25 = srga25 / sum3

            aaa3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa3[0][0] = 1
            aaa3[0][1] = 0.56
            aaa3[0][2] = 1.22
            aaa3[0][3] = 1.32
            aaa3[0][4] = 1.06
            aaa3[1][0] = 1.76
            aaa3[1][1] = 1
            aaa3[1][2] = 2.16
            aaa3[1][3] = 2.33
            aaa3[1][4] = 1.87
            aaa3[2][0] = 0.81
            aaa3[2][1] = 0.46
            aaa3[2][2] = 1
            aaa3[2][3] = 1.07
            aaa3[2][4] = 0.86
            aaa3[3][0] = 0.75
            aaa3[3][1] = 0.42
            aaa3[3][2] = 0.92
            aaa3[3][3] = 1
            aaa3[3][4] = 0.8
            aaa3[4][0] = 0.93
            aaa3[4][1] = 0.53
            aaa3[4][2] = 1.15
            aaa3[4][3] = 1.24
            aaa3[4][4] = 1
            srga31t = aaa3[0][0] * aaa3[0][1] * aaa3[0][2] * aaa3[0][3] * aaa3[0][4]
            srga31 = pow(srga31t, 1 / 5)
            srga32t = aaa3[1][0] * aaa3[1][1] * aaa3[1][2] * aaa3[1][3] * aaa3[1][4]
            srga32 = pow(srga32t, 1 / 5)
            srga33t = aaa3[2][0] * aaa3[2][1] * aaa3[2][2] * aaa3[2][3] * aaa3[2][4]
            srga33 = pow(srga33t, 1 / 5)
            srga34t = aaa3[3][0] * aaa3[3][1] * aaa3[3][2] * aaa3[3][3] * aaa3[3][4]
            srga34 = pow(srga34t, 1 / 5)
            srga35t = aaa3[4][0] * aaa3[4][1] * aaa3[4][2] * aaa3[4][3] * aaa3[4][4]
            srga35 = pow(srga35t, 1 / 5)
            sum4 = srga31 + srga32 + srga33 + srga34 + srga35
            nsrga31 = srga31 / sum4
            nsrga32 = srga32 / sum4
            nsrga33 = srga33 / sum4
            nsrga34 = srga34 / sum4
            nsrga35 = srga35 / sum4

            aaa4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa4[0][0] = 1
            aaa4[0][1] = 2.92
            aaa4[0][2] = 1.68
            aaa4[0][3] = 1.15
            aaa4[0][4] = 2.92
            aaa4[1][0] = 0.34
            aaa4[1][1] = 1
            aaa4[1][2] = 0.57
            aaa4[1][3] = 0.39
            aaa4[1][4] = 1
            aaa4[2][0] = 0.59
            aaa4[2][1] = 1.73
            aaa4[2][2] = 1
            aaa4[2][3] = 0.68
            aaa4[2][4] = 1.73
            aaa4[3][0] = 0.86
            aaa4[3][1] = 2.53
            aaa4[3][2] = 1.46
            aaa4[3][3] = 1
            aaa4[3][4] = 2.53
            aaa4[4][0] = 0.34
            aaa4[4][1] = 1
            aaa4[4][2] = 0.57
            aaa4[4][3] = 0.39
            aaa4[4][4] = 1
            srga41t = aaa4[0][0] * aaa4[0][1] * aaa4[0][2] * aaa4[0][3] * aaa4[0][4]
            srga41 = pow(srga41t, 1 / 5)
            srga42t = aaa4[1][0] * aaa4[1][1] * aaa4[1][2] * aaa4[1][3] * aaa4[1][4]
            srga42 = pow(srga42t, 1 / 5)
            srga43t = aaa4[2][0] * aaa4[2][1] * aaa4[2][2] * aaa4[2][3] * aaa4[2][4]
            srga43 = pow(srga43t, 1 / 5)
            srga44t = aaa4[3][0] * aaa4[3][1] * aaa4[3][2] * aaa4[3][3] * aaa4[3][4]
            srga44 = pow(srga44t, 1 / 5)
            srga45t = aaa4[4][0] * aaa4[4][1] * aaa4[4][2] * aaa4[4][3] * aaa4[4][4]
            srga45 = pow(srga45t, 1 / 5)
            sum5 = srga41 + srga42 + srga43 + srga44 + srga45
            nsrga41 = srga41 / sum5
            nsrga42 = srga42 / sum5
            nsrga43 = srga43 / sum5
            nsrga44 = srga44 / sum5
            nsrga45 = srga45 / sum5

            aaa5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

            aaa5[0][0] = 1
            aaa5[0][1] = 1.04
            aaa5[0][2] = 1.08
            aaa5[0][3] = 0.52
            aaa5[0][4] = 0.68
            aaa5[1][0] = 0.95
            aaa5[1][1] = 1
            aaa5[1][2] = 1.04
            aaa5[1][3] = 0.5
            aaa5[1][4] = 0.65
            aaa5[2][0] = 0.92
            aaa5[2][1] = 0.96
            aaa5[2][2] = 1
            aaa5[2][3] = 0.48
            aaa5[2][4] = 0.62
            aaa5[3][0] = 1.91
            aaa5[3][1] = 2
            aaa5[3][2] = 2.08
            aaa5[3][3] = 1
            aaa5[3][4] = 1.3
            aaa5[4][0] = 1.46
            aaa5[4][1] = 1.53
            aaa5[4][2] = 1.59
            aaa5[4][3] = 0.76
            aaa5[4][4] = 1
            srga51t = aaa5[0][0] * aaa5[0][1] * aaa5[0][2] * aaa5[0][3] * aaa5[0][4]
            srga51 = pow(srga51t, 1 / 5)
            srga52t = aaa5[1][0] * aaa5[1][1] * aaa5[1][2] * aaa5[1][3] * aaa5[1][4]
            srga52 = pow(srga52t, 1 / 5)
            srga53t = aaa5[2][0] * aaa5[2][1] * aaa5[2][2] * aaa5[2][3] * aaa5[2][4]
            srga53 = pow(srga53t, 1 / 5)
            srga54t = aaa5[3][0] * aaa5[3][1] * aaa5[3][2] * aaa5[3][3] * aaa5[3][4]
            srga54 = pow(srga54t, 1 / 5)
            srga55t = aaa5[4][0] * aaa5[4][1] * aaa5[4][2] * aaa5[4][3] * aaa5[4][4]
            srga55 = pow(srga55t, 1 / 5)
            sum6 = srga51 + srga52 + srga53 + srga54 + srga55
            nsrga51 = srga51 / sum6
            nsrga52 = srga52 / sum6
            nsrga53 = srga53 / sum6
            nsrga54 = srga54 / sum6
            nsrga55 = srga55 / sum6

            alt1 = 0
            alt2 = 0
            alt3 = 0
            alt4 = 0
            alt5 = 0
            tm = 0

            total = 20000000

            years = int(self.kk3dialui.years.text())

            book = xlwt.Workbook()
            sheet1 = book.add_sheet("Таблиця міграцій за роками")
            sheet1.write(0, 6, "Роки")
            sheet1.write(0, 7, "Загальна кількість мігрантів")
            sheet1.write(0, 8, "Загальна кількість населення")
            sheet1.write(0, 1, "Обрали Польщу")
            sheet1.write(0, 2, "Обрали Чехію")
            sheet1.write(0, 3, "Обрали Литву")
            sheet1.write(0, 4, "Обрали Венгрію")
            sheet1.write(0, 5, "Обрали Естонію")

            for i in range(1, years):
                potm = total*0.1
                born = total* -0.01
                v = int(potm)
                tm = tm + potm

                for j in range (v):
                    nsrgk1 = random.uniform(0.1, 0.9)
                    nsrgk2 = random.uniform(0.1, 0.9)
                    nsrgk3 = random.uniform(0.1, 0.9)
                    nsrgk4 = random.uniform(0.1, 0.9)
                    nsrgk5 = random.uniform(0.1, 0.9)
                    gf1 = nsrga11 * nsrgk1 + nsrga21 * nsrgk2 + nsrga31 * nsrgk3 + nsrga41 * nsrgk4 + nsrga51 * nsrgk5
                    gf2 = nsrga12 * nsrgk1 + nsrga22 * nsrgk2 + nsrga32 * nsrgk3 + nsrga42 * nsrgk4 + nsrga52 * nsrgk5
                    gf3 = nsrga13 * nsrgk1 + nsrga23 * nsrgk2 + nsrga33 * nsrgk3 + nsrga43 * nsrgk4 + nsrga53 * nsrgk5
                    gf4 = nsrga14 * nsrgk1 + nsrga24 * nsrgk2 + nsrga34 * nsrgk3 + nsrga44 * nsrgk4 + nsrga54 * nsrgk5
                    gf5 = nsrga15 * nsrgk1 + nsrga25 * nsrgk2 + nsrga35 * nsrgk3 + nsrga45 * nsrgk4 + nsrga55 * nsrgk5
                    gp = np.array([0, 0, 0, 0, 0], float)
                    gp[0] = gf1
                    gp[1] = gf2
                    gp[2] = gf3
                    gp[3] = gf4
                    gp[4] = gf5

                    maxi = np.argmax(gp)

                    if maxi == 0:
                        alt1 = alt1 + 1
                    elif maxi == 1:
                        alt2 = alt2 + 1
                    elif maxi == 2:
                        alt3 = alt3 + 1
                    elif maxi == 3:
                        alt4 = alt4 + 1
                    else:
                        alt5 += 1

                total = total - potm
                total = total + born

                sheet1.write(i, 6, i)
                sheet1.write(i, 7, tm)
                sheet1.write(i, 8, total)
                sheet1.write(i, 1, alt1)
                sheet1.write(i, 2, alt2)
                sheet1.write(i, 3, alt3)
                sheet1.write(i, 4, alt4)
                sheet1.write(i, 5, alt5)


            self.fin3ui.s1.setText(str(alt1))
            self.fin3ui.s2.setText(str(alt2))
            self.fin3ui.s3.setText(str(alt3))
            self.fin3ui.s4.setText(str(alt4))
            self.fin3ui.s5.setText(str(alt5))
            self.fin3ui.total.setText(str(round(total, 2)))
            self.fin3ui.tm.setText(str(round(tm,2)))
            book.save("migrcalc2.xls")

        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Помилка вводу")
            msg.setText("Перевірте правильність вхідних даних")
            msg.setIcon(msg.Warning)
            msg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = prog()
    myapp.show()
    sys.exit(app.exec())
