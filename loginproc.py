# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginproc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(491, 151)
        LoginWindow.setMinimumSize(QtCore.QSize(430, 134))
        LoginWindow.setMaximumSize(QtCore.QSize(568, 273))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.passwLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwLine.setObjectName("passwLine")
        self.gridLayout.addWidget(self.passwLine, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.loginLine = QtWidgets.QLineEdit(self.centralwidget)
        self.loginLine.setObjectName("loginLine")
        self.gridLayout.addWidget(self.loginLine, 0, 1, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmBtn.setObjectName("confirmBtn")
        self.gridLayout.addWidget(self.confirmBtn, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.errorLbl = QtWidgets.QLabel(self.centralwidget)
        self.errorLbl.setText("")
        self.errorLbl.setObjectName("errorLbl")
        self.gridLayout.addWidget(self.errorLbl, 2, 0, 1, 2)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "SIGN_IN"))
        self.label.setText(_translate("LoginWindow", "Password"))
        self.confirmBtn.setText(_translate("LoginWindow", "Confirm"))
        self.label_2.setText(_translate("LoginWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

