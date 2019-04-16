# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thing.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThingWindow(object):
    def setupUi(self, ThingWindow):
        ThingWindow.setObjectName("ThingWindow")
        ThingWindow.setEnabled(False)
        ThingWindow.resize(438, 447)
        ThingWindow.setMinimumSize(QtCore.QSize(438, 447))
        self.centralwidget = QtWidgets.QWidget(ThingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(False)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)
        self.addFavBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addFavBtn.setObjectName("addFavBtn")
        self.gridLayout.addWidget(self.addFavBtn, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 7, 1, 1, 1)
        ThingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        ThingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThingWindow)
        self.statusbar.setObjectName("statusbar")
        ThingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThingWindow)
        QtCore.QMetaObject.connectSlotsByName(ThingWindow)

    def retranslateUi(self, ThingWindow):
        _translate = QtCore.QCoreApplication.translate
        ThingWindow.setWindowTitle(_translate("ThingWindow", "ThingPage"))
        self.label_9.setText(_translate("ThingWindow", "TextLabel"))
        self.addFavBtn.setText(_translate("ThingWindow", "Add Favourite"))
        self.label_6.setText(_translate("ThingWindow", "TextLabel"))
        self.label_2.setText(_translate("ThingWindow", "Description"))
        self.label_8.setText(_translate("ThingWindow", "TextLabel"))
        self.label_7.setText(_translate("ThingWindow", "TextLabel"))
        self.label.setText(_translate("ThingWindow", "Name"))
        self.label_3.setText(_translate("ThingWindow", "Change status"))
        self.label_4.setText(_translate("ThingWindow", "Contact"))
        self.backBtn.setText(_translate("ThingWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThingWindow = QtWidgets.QMainWindow()
    ui = Ui_ThingWindow()
    ui.setupUi(ThingWindow)
    ThingWindow.show()
    sys.exit(app.exec_())

