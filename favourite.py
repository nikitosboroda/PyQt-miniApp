# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favourite.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FavouriteWindow(object):
    def setupUi(self, FavouriteWindow):
        FavouriteWindow.setObjectName("FavouriteWindow")
        FavouriteWindow.resize(570, 405)
        self.centralwidget = QtWidgets.QWidget(FavouriteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(470, 30, 75, 23))
        self.backBtn.setObjectName("backBtn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 531, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label.setObjectName("label")
        FavouriteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FavouriteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName("menubar")
        FavouriteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FavouriteWindow)
        self.statusbar.setObjectName("statusbar")
        FavouriteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FavouriteWindow)
        QtCore.QMetaObject.connectSlotsByName(FavouriteWindow)

    def retranslateUi(self, FavouriteWindow):
        _translate = QtCore.QCoreApplication.translate
        FavouriteWindow.setWindowTitle(_translate("FavouriteWindow", "Favourite"))
        self.backBtn.setText(_translate("FavouriteWindow", "Back"))
        self.label.setText(_translate("FavouriteWindow", "Favourites"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FavouriteWindow = QtWidgets.QMainWindow()
    ui = Ui_FavouriteWindow()
    ui.setupUi(FavouriteWindow)
    FavouriteWindow.show()
    sys.exit(app.exec_())

