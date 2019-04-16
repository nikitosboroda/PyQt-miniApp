# -*- coding: utf-8 -*-
import app
import thing
import loginproc
import favourite

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (qApp, QWidget)
from PyQt5 import QtCore

import sys
import os

import mysql.connector
from mysql.connector import Error


class MainWin(QtWidgets.QMainWindow, app.Ui_MainWindow):
	closed = QtCore.pyqtSignal()
	def __init__(self):
		""" INIT function """
		super().__init__()
		self.setupUi(self)
		self.findBtn.clicked.connect(self.sql_settings)
		#self.logBtn.clicked.connect(self.login_proc)
		self.favBtn.clicked.connect(self.favourte_things)
		self.categBox.activated[str].connect(self.set_category)
	
	def sql_connection(self):
		self.cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='changer')

		try:
			self.cursor = self.cnx.cursor()
			print('DataBase opened')
	        #cursor.execute(sql)
		except Exception as e:
			print("ERROR -->> ", e)
			self.cnx.close()
		finally:
			return self.cursor
			
	def sql_connect_close(self, cnx):
		self.cnx.close()
		print("DataBase closed")
	
	def sql_find_btn(self, sql):
		try:
			cursor = self.sql_connection()
		except Exception as e:
			print("ERROR -->> ", e)
		else:
			print("DB Search")
			try:
				result = cursor.fetchall()
				for row_num, row_data in enumerate(result):
					self.tableF.insertRow(row_num)
					for col_num, data in enumerate(row_data):
						self.tableF.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
			except Exception as e:
				print("ResultError --> ", e)
				return
		finally:
			self.sql_connect_close(cursor)
			
	
	def sql_settings(self, text=None):
		try:
			self.text = self.lineFind.text()
			if text == '':
				sql = """SELECT * FROM users;"""
				self.sql_find_btn(sql)
			else:
				sql = " SELECT * FROM ..."
				self.sql_find_btn(sql)
		except Exception as e:
			print("ERROR -> ", e)
			
	def favourte_things(self):
		pass
	
	def set_category(self):
		pass


class ThingWin(QtWidgets.QMainWindow, thing.Ui_ThingWindow):
	def __init__(self):
		""" INIT function """
		super().__init__()
		self.setupUi(self)
		self.addFavBtn.clicked.connect(self.add_favourite)
	
	def add_favourite(self):
		pass

class LoginWin(QtWidgets.QMainWindow, loginproc.Ui_LoginWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
	
		#self.confirmBtn.clicked.connect(self.confirm_er)
		self.errorLbl.setStyleSheet("QLabel {color:rgba(255, 30, 100, 255)}")

class FavouiteWin(QtWidgets.QMainWindow, favourite.Ui_FavouriteWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
class Controller:
	def __init__(self):
		self.mainW = MainWin()
		self.logW = LoginWin()
		self.favorW = FavouiteWin()
		
		self.mainW.favBtn.clicked.connect(self.open_fav_win)
		self.favorW.backBtn.clicked.connect(self.open_main_win)
		self.mainW.logBtn.clicked.connect(self.open_log_win)
		self.logW.confirmBtn.clicked.connect(self.confirmer)
		#self.mainW.closed.connect(self.logW.show)
		self.mainW.show()
	
	def confirmer(self):
		self.log_txt = self.logW.loginLine.text()
		self.passw_txt = self.logW.passwLine.text()
		if self.log_txt == '' or self.passw_txt == '':
			self.logW.errorLbl.setText("Wrong password or login")
			self.logW.loginLine.setText('')
			self.logW.passwLine.setText('')
		else:
			self.logW.close()
			self.mainW.show()
			
	def open_fav_win(self):
		self.mainW.close()
		self.favorW.show()
		
	def open_log_win(self):
		self.mainW.close()
		self.logW.show()

	def open_main_win(self):
		try:
			self.logW.close()
			self.favorW.close()
			self.mainW.show()
		except Exception as e:
			print("ERROR == ", e)

	
		
		
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    okno = Controller()
    #window = MainWin()  # Создаём объект класса MainWin
    #window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()