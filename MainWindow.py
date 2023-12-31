# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json,hashlib
from docxtpl import DocxTemplate

import AllFunctions
import RRK



class Ui_MainWindow(object):

    NDoc=0
    Ntime=0
    def __init__(self):
        super().__init__()
        self.window=QtWidgets.QMainWindow()
        # self.setupUi(self.window)
        self.window.show()
        self.update_all_files()

    def update_all_files(self):
        self.DataToTable = AllFunctions.load_DataToTable()
        self.differetn_docs = AllFunctions.load_Different_docks()
        self.HeshData = AllFunctions.load_HeshData()
    def setupUi(self, MainWindow,DocumentWindowClass):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 570)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 80, 771, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        count = AllFunctions.load_DataToTable()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 80, 151, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.treeWidget.setFont(font)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 440, 111, 41))
        self.pushButton.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_2.setGeometry(QtCore.QRect(10, 190, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.treeWidget_2.setFont(font)
        self.treeWidget_2.setObjectName("treeWidget_2")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.treeWidget_2.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 20, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())








        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        try:
            for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                    if item is not None:
                        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEnabled)
        except:
            pass

        '''Заполнение данных таблицами'''
        striing = 0
        rolls = 0
        for i in self.DataToTable:
            for j in i:
                item1 = QtWidgets.QTableWidgetItem(str(j))
                self.tableWidget.setItem(striing, rolls, item1)
                rolls += 1

            pushButton3 = QtWidgets.QPushButton(f'Открыть_{striing+1}')
            pushButton3.clicked.connect(
                lambda ch, btn=pushButton3: AllFunctions.both_find_convert_docs(btn, DocumentWindowClass,
                                                                                self.differetn_docs))
            pushButton3.clicked.connect(DocumentWindowClass.window.show)
            self.tableWidget.setCellWidget(striing, 4, pushButton3)
            rolls = 0
            striing += 1

        # try:

        # except:
        #     pass



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Учетный №"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Тема"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата рагистрации"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", " Документы"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Все"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Входящие"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Исходящие"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Внутренние"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Проверить"))
        self.lineEdit.setText(_translate("MainWindow", "Пользователь"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", " Фильтр"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "Приказы"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "Акты"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "Директивы"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_2.setText(_translate("MainWindow", "Найти"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Пользователи"))
        self.action.setText(_translate("MainWindow", "Сменить пользователя"))
        self.action_2.setText(_translate("MainWindow", "Добавить"))

    def check_for_changes_all_files(self):
        self.update_all_files()
        for i in range(len(self.differetn_docs)):
            self.check_for_changes(i)
            for j in range(1,len(self.differetn_docs[i])):
                self.check_for_changes_Ntime(i,j)

    def check_for_changes(self,Ndoc): #первый период документа t=0

        ''''''
        error=False
        ''''''
        count_for_hash=0
        open_text_in_str=''
        try:
            different_times_in_hash=self.HeshData[Ndoc][0]
        except:
            different_times_in_hash =[]
        for k in self.differetn_docs[Ndoc][0]:
            open_text_in_str += k
            HeshData_in_attributes = hashlib.md5(k.encode()).hexdigest()
            if different_times_in_hash[count_for_hash]!=HeshData_in_attributes:
                error=True
            count_for_hash+=1

        admin_key,admin_cert,user=AllFunctions.Load_Admin_key_and_cert()
        admin_signature = AllFunctions.load_Admin_signature(Ndoc,0)
        AllFunctions.verify_signature(admin_key, open_text_in_str, admin_signature, user)

        user_key,user_cert,user=AllFunctions.Load_User_key_and_cert()
        user_signature = AllFunctions.load_User_signature(Ndoc,0)
        AllFunctions.verify_signature(user_key, open_text_in_str, user_signature, user)
    def check_for_changes_Ntime(self,Ndoc,Ntime): #первый период документа t=0

        ''''''
        error=False
        ''''''
        count_for_hash=0
        open_text_in_str=''
        try:
            different_times_in_hash=self.HeshData[Ndoc][Ntime]
        except:
            different_times_in_hash =[]

        for k in self.differetn_docs[Ndoc][Ntime]:
            open_text_in_str += k
            HeshData_in_attributes = hashlib.md5(k.encode()+self.differetn_docs[Ndoc][Ntime][count_for_hash].encode()).hexdigest()
            if different_times_in_hash[count_for_hash]!=HeshData_in_attributes:
                error=True
            count_for_hash+=1


        admin_key,admin_cert,user=AllFunctions.Load_Admin_key_and_cert()
        admin_signature = AllFunctions.load_Admin_signature(Ndoc,Ntime)
        last_admin_signature = AllFunctions.load_Admin_signature(Ndoc, Ntime-1)
        AllFunctions.verify_signature(admin_key, open_text_in_str + last_admin_signature.hex(), admin_signature, user)

        user_key,user_cert,user=AllFunctions.Load_User_key_and_cert()
        user_signature = AllFunctions.load_User_signature(Ndoc,Ntime)
        last_user_signature = AllFunctions.load_User_signature(Ndoc, Ntime-1)
        AllFunctions.verify_signature(user_key, open_text_in_str + last_user_signature.hex(), user_signature, user)



