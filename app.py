# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 447)
        MainWindow.setMinimumSize(QtCore.QSize(438, 447))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logBtn.setObjectName("logBtn")
        self.gridLayout.addWidget(self.logBtn, 0, 4, 1, 1)
        self.tableF = QtWidgets.QTableView(self.centralwidget)
        self.tableF.setObjectName("tableF")
        self.gridLayout.addWidget(self.tableF, 5, 0, 1, 5)
        self.findBtn = QtWidgets.QPushButton(self.centralwidget)
        self.findBtn.setObjectName("findBtn")
        self.gridLayout.addWidget(self.findBtn, 1, 2, 1, 1)
        self.categBox = QtWidgets.QComboBox(self.centralwidget)
        self.categBox.setObjectName("categBox")
        self.gridLayout.addWidget(self.categBox, 4, 2, 1, 1)
        self.favBtn = QtWidgets.QPushButton(self.centralwidget)
        self.favBtn.setObjectName("favBtn")
        self.gridLayout.addWidget(self.favBtn, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.lineFind = QtWidgets.QLineEdit(self.centralwidget)
        self.lineFind.setObjectName("lineFind")
        self.gridLayout.addWidget(self.lineFind, 1, 0, 1, 2)
        self.labelregistr = QtWidgets.QLabel(self.centralwidget)
        self.labelregistr.setText("")
        self.labelregistr.setObjectName("labelregistr")
        self.gridLayout.addWidget(self.labelregistr, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logBtn.setText(_translate("MainWindow", "LogIn"))
        self.findBtn.setText(_translate("MainWindow", "Find"))
        self.favBtn.setText(_translate("MainWindow", "Favourite"))
        self.label_2.setText(_translate("MainWindow", "Set category"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

