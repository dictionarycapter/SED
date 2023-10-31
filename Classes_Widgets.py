
from PyQt5 import QtCore, QtGui, QtWidgets
import AllFunctions,hashlib,json
from docxtpl import DocxTemplate


class Ui_Form_Try_To_Convert(object):
    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QWidget()
        self.setupUi(self.window)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(957, 655)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(280, 10, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("\n"
"border: 3px solid black;\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"border-top: 0px;")
        self.label_16.setObjectName("label_16")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 120, 961, 481))
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 201, 100);")
        self.stackedWidget.setObjectName("stackedWidget")


        #Первая страница и скролл-ба
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 945, 530))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(20, 20, 850, 400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")



        #Самодобавление в код
        grid_layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        for i in range(10):
                #добавление виджитов в область
                self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
                # self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 901, 22))
                self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit.setObjectName("lineEdit")
                self.horizontalLayout_2.addWidget(self.lineEdit)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.horizontalLayout_2.addWidget(self.lineEdit_2)
                self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.horizontalLayout_2.addWidget(self.lineEdit_3)
                self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.horizontalLayout_2.addWidget(self.lineEdit_4)
                self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.horizontalLayout_2.addWidget(self.lineEdit_5)
                self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_6.setObjectName("lineEdit_6")
                self.horizontalLayout_2.addWidget(self.lineEdit_6)
                self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_7.setObjectName("lineEdit_7")
                self.horizontalLayout_2.addWidget(self.lineEdit_7)
                self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_8.setObjectName("lineEdit_8")
                self.horizontalLayout_2.addWidget(self.lineEdit_8)
                self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_9.setObjectName("lineEdit_9")
                self.horizontalLayout_2.addWidget(self.lineEdit_9)
                self.lineEdit_11 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
                self.lineEdit_11.setObjectName("lineEdit_11")
                self.horizontalLayout_2.addWidget(self.lineEdit_11)

                widget_temp=QtWidgets.QWidget()
                widget_temp.setLayout(self.horizontalLayout_2)
                widget_temp.setMinimumHeight(50)

                grid_layout.addWidget(widget_temp, i, 0)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)

        #вторая страница
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)



        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 931, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("padding: 1 5 0 0;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout.addWidget(self.label_25)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("padding: 1 5 0 0;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("padding: 1 5 0 0;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout.addWidget(self.label_23)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("padding: 1 5 0 0;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("padding: 1 5 0 0;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("padding: 1 5 0 0;")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("padding: 1 5 0 0;")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("padding: 1 5 0 0;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("padding: 1 5 0 0;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("padding: 1 5 0 0;")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout.addWidget(self.label_20)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(800, 20, 140, 48))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("padding: 1 5 0 0;")
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout.addWidget(self.lineEdit_10)


        #Добавление кнопок
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(820, 610, 121, 31))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 610, 121, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 610, 261, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_16.setText(_translate("Form", "Журнал контроля целостности"))
        self.label_25.setText(_translate("Form", "Nизменен"))
        self.label_21.setText(_translate("Form", "    Должность"))
        self.label_23.setText(_translate("Form", "Подписал"))
        self.label_10.setText(_translate("Form", "      Номер"))
        self.label_18.setText(_translate("Form", "     Дата"))
        self.label_19.setText(_translate("Form", "   Город"))
        self.label_22.setText(_translate("Form", "Наименование"))
        self.label_17.setText(_translate("Form", "Содержание"))
        self.label_9.setText(_translate("Form", "Звание"))
        self.label_20.setText(_translate("Form", "ФИО"))
        self.label_24.setText(_translate("Form", "  Номер документа"))
        self.pushButton.setText(_translate("Form", "Следующий"))
        self.pushButton_2.setText(_translate("Form", "Предыдущий"))
        self.pushButton_3.setText(_translate("Form", "Посмотреть документ"))

class Ui_Form_RRK(object):
    TableData = AllFunctions.load_DataToTable()
    different_docs = AllFunctions.load_Different_docks()
    HeshData = AllFunctions.load_HeshData()
    NDoc=len(different_docs)
    Ntime=0

    def __init__(self):
        super().__init__()
        self.window=QtWidgets.QMainWindow()
        self.setupUi(self.window)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(904, 633)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(310, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("\n"
"border: 3px solid black;\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"border-top: 0px;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 811, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("padding: 1 5 0 0;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("padding: 1 5 0 0;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 120, 911, 521))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("\n"
":tab\n"
"{\n"
"width: 445px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 430, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(40, 90, 811, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("padding: 1 5 0 0;")
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setLineWidth(2)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(40, 120, 811, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("padding: 1 5 0 0;")
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setLineWidth(2)
        self.label_15.setObjectName("label_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 430, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 821, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("padding: 1 5 0 0;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_2.addWidget(self.lineEdit_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 851, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("padding: 1 5 0 0;")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("padding: 1 5 0 0;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("padding: 1 5 0 0;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("padding: 1 5 0 0;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("padding: 1 5 0 0;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("padding: 1 5 0 0;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("padding: 1 5 0 0;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("padding: 1 5 0 0;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 430, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 430, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.TableData=AllFunctions.load_DataToTable()
        d=QtCore.QDateTime.currentDateTime()
        self.dateEdit_2.setDateTime(d)
        self.lineEdit_7.setText(str(len(self.TableData)+1))

        # self.dateEdit.setDateTime()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_16.setText(_translate("Form", "Регистрация документа"))
        self.label_8.setText(_translate("Form", "Учетный №"))
        self.label_11.setText(_translate("Form", "Дата регистрации"))
        self.dateEdit_2.setDisplayFormat(_translate("Form", "«dd» MM yyyy г."))
        self.pushButton_4.setText(_translate("Form", "Добавить документ"))
        self.label_14.setText(_translate("Form", "Документ должен отвечать требованиям требованиям к форме жокумента."))
        self.label_15.setText(_translate("Form", "При загрузке окумента будет произведена его проверка."))
        self.pushButton_5.setText(_translate("Form", "Отклонить"))
        self.label_12.setText(_translate("Form", "Документ"))
        self.pushButton_3.setText(_translate("Form", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Загрузить докумен"))
        self.label_13.setText(_translate("Form", "Содержание"))
        self.label_5.setText(_translate("Form", "Наименование"))
        self.label_3.setText(_translate("Form", "Дата"))
        self.label.setText(_translate("Form", "Кто подписал"))
        self.dateEdit.setDisplayFormat(_translate("Form", "«dd» MM yyyy г."))
        self.label_2.setText(_translate("Form", "Номер"))
        self.label_6.setText(_translate("Form", "Звание"))
        self.label_4.setText(_translate("Form", "Город"))
        self.label_7.setText(_translate("Form", "ФИО"))
        self.pushButton_2.setText(_translate("Form", "Отклонить"))
        self.pushButton.setText(_translate("Form", "Сформировать форму для документа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Сформировать документ"))

    def clear_form(self):
        self.TableData = AllFunctions.load_DataToTable()
        d = QtCore.QDateTime.currentDateTime()
        self.dateEdit_2.setDateTime(d)
        self.lineEdit_7.setText(str(len(self.TableData) + 1))

        self.lineEdit.setText('')  # self.plus_a()
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.textEdit.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
    def show_form(self,window):
        self.clear_form()
        window.show()

    def plus_a(str1):
        buff = str1.split(' ')
        buff[0] += 'A'
        return ' '.join(buff)

    '''Создаем документ и сохраняем данные для таблицы, хэш значения и сами данные за каждый доумент.
    Сохраняются данные в файлы и создается документ'''
    def add_new_document(self):
        different_t=[]
        data_in_t = []
        defferent_hash_t=[]
        hash_in_t=[]

        open_text_in_str=''

    #Основной код
        doc = DocxTemplate('Files/Order.docx')
        dictionary = {}
        dictionary['who_a'] = self.lineEdit.text()#self.plus_a()
        dictionary['who'] = self.lineEdit.text()
        dictionary['number'] = self.lineEdit_2.text()
        dictionary['date'] = self.dateEdit.text()
        dictionary['city'] = self.lineEdit_3.text()
        dictionary['name'] = self.lineEdit_4.text()
        dictionary['context'] = self.textEdit.toPlainText()
        dictionary['rank'] = self.lineEdit_5.text()
        dictionary['FIO'] = self.lineEdit_6.text()

        open_text_in_str=''
        #Создание словаря
        for i in dictionary.values():
            open_text_in_str+=i#страка значений открытого текста
            hash_data_of_attributs = hashlib.md5(i.encode()).hexdigest()#хэш отдельного атрибута
            hash_in_t.append(hash_data_of_attributs)#хэш за документ
            data_in_t.append(i)
            defferent_hash_t.append(hash_in_t)
        different_t.append(data_in_t)#слоавь значений
        self.different_docs.append(different_t)#добавление значения открытого текста
        self.HeshData.append(defferent_hash_t)#добавление значения хэшей документа



        # Подписи администратора и пользователя
        admin_key,admin_cert,user=AllFunctions.Load_Admin_key_and_cert()
        signature = AllFunctions.sign_doc(user,open_text_in_str, admin_key, self.NDoc, self.Ntime)
        user_key,user_cert,user=AllFunctions.Load_User_key_and_cert()
        signature = AllFunctions.sign_doc(user,open_text_in_str, user_key, self.NDoc, self.Ntime)


        #Формирование данных для таблицы
        data_in_table = []
        data_in_table.append(len(self.TableData)+1)
        data_in_table.append('Приказ')
        data_in_table.append(dictionary['name'])
        date_in_str = str(self.dateEdit_2.text())
        data_in_table.append(date_in_str)
        self.TableData.append(data_in_table)



        AllFunctions.save_HeshData(self.HeshData)
        AllFunctions.save_DataToTable(self.TableData)
        AllFunctions.save_Different_docks(self.different_docs)

        doc.render(dictionary)
        doc.save(f'docs/document{self.NDoc}_{self.Ntime}.docx')
        self.clear_form()
        self.window.close()

class Ui_Form_Diffenece(object):
    different_docs=AllFunctions.load_Different_docks()
    DataToTable=AllFunctions.load_DataToTable()
    HeshData=AllFunctions.load_HeshData()
    Ndoc=0

    def __init__(self):
        super().__init__()
        self.window=QtWidgets.QMainWindow()
        self.setupUi(self.window)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 605)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(310, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("\n"
"border: 3px solid black;\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"border-top: 0px;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 811, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("padding: 1 5 0 0;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("padding: 1 5 0 0;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.dateEdit_3 = QtWidgets.QDateEdit(Form)
        self.dateEdit_3.setGeometry(QtCore.QRect(129, 170, 331, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(129, 138, 331, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(14, 480, 113, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("padding: 1 5 0 0;")
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(10, 231, 113, 235))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("padding: 1 5 0 0;")
        self.label_17.setObjectName("label_17")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(466, 138, 56, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("padding: 1 5 0 0;")
        self.label_10.setObjectName("label_10")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(10, 169, 113, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("padding: 1 5 0 0;")
        self.label_18.setObjectName("label_18")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(129, 200, 730, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(466, 169, 56, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("padding: 1 5 0 0;")
        self.label_19.setObjectName("label_19")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(532, 480, 331, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(133, 480, 331, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(470, 480, 56, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("padding: 1 5 0 0;")
        self.label_20.setObjectName("label_20")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(129, 231, 730, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(10, 138, 113, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("padding: 1 5 0 0;")
        self.label_21.setObjectName("label_21")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(528, 169, 331, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(528, 138, 331, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(10, 200, 113, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("padding: 1 5 0 0;")
        self.label_22.setObjectName("label_22")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 530, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 530, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        self.pushButton.clicked.connect(self.add_new_document)
        try:
            self.Fill_document()
        except:
            pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_16.setText(_translate("Form", "Редактирование документа"))
        self.label_8.setText(_translate("Form", "Учетный №"))
        self.label_11.setText(_translate("Form", "Дата регистрации"))
        self.dateEdit_2.setDisplayFormat(_translate("Form", "«dd» MM yyyy г."))
        self.dateEdit_3.setDisplayFormat(_translate("Form", "«dd» MM yyyy г."))
        self.label_9.setText(_translate("Form", "Звание"))
        self.label_17.setText(_translate("Form", "Содержание"))
        self.label_10.setText(_translate("Form", "Номер"))
        self.label_18.setText(_translate("Form", "Дата"))
        self.label_19.setText(_translate("Form", "Город"))
        self.label_20.setText(_translate("Form", "ФИО"))
        self.label_21.setText(_translate("Form", "Кто подписал"))
        self.label_22.setText(_translate("Form", "Наименование"))
        self.pushButton.setText(_translate("Form", "Сохранить изменения"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))

    def Fill_document(self, Ndoc):
        self.Ndoc = Ndoc


        self.lineEdit_9.setText(self.different_docs[self.Ndoc][-1][1])#who
        self.lineEdit_14.setText(self.different_docs[self.Ndoc][-1][2])#numder


        data_text = self.different_docs[self.Ndoc][-1][3]
        date_format = '«dd» MM yyyy г.'
        self.dateEdit_3.setDate(QtCore.QDate.fromString(data_text, date_format))



        self.lineEdit_13.setText(self.different_docs[self.Ndoc][-1][4])#sity
        self.lineEdit_10.setText(self.different_docs[self.Ndoc][-1][5])#name_of_document
        self.textEdit_2.setText(self.different_docs[self.Ndoc][-1][6])#text_of_doc
        self.lineEdit_12.setText(self.different_docs[self.Ndoc][-1][7])#zvanie
        self.lineEdit_11.setText(self.different_docs[self.Ndoc][-1][8])#FIO



        self.lineEdit_7.setText(str(self.DataToTable[self.Ndoc][0]))
        self.dateEdit_2.setDate(QtCore.QDate.fromString(self.DataToTable[self.Ndoc][3], date_format))

    def add_new_document(self):
        hash_in_t = []
        data_in_t = []
        Ntime = len(self.different_docs[self.Ndoc]) - 1
        Ntime_new = Ntime+1




        # Основной код
        doc = DocxTemplate('Files/Order.docx')
        dictionary = {}
        dictionary['who_a'] = self.lineEdit_9.text()  # self.plus_a()
        dictionary['who'] = self.lineEdit_9.text()
        dictionary['number'] = self.lineEdit_14.text()
        dictionary['date'] = self.dateEdit_3.text()
        dictionary['city'] = self.lineEdit_13.text()
        dictionary['name'] = self.lineEdit_10.text()
        dictionary['context'] = self.textEdit_2.toPlainText()
        dictionary['rank'] = self.lineEdit_12.text()
        dictionary['FIO'] = self.lineEdit_11.text()

        open_text_in_str = ''
        # Создание словаря
        count=0
        for i in dictionary.values():
            open_text_in_str += i  # страка значений открытого текста
            hash_data_of_attributs_before=self.HeshData[self.Ndoc][-1][count]#загружаем предыдущее значение
            hash_data_of_attributs = hashlib.md5(i.encode()+hash_data_of_attributs_before.encode()).hexdigest()  # хэш отдельного атрибута
            hash_in_t.append(hash_data_of_attributs)  # хэш за документ
            data_in_t.append(i)
            count+=1
        # слоавь значений
        self.different_docs[self.Ndoc].append(data_in_t)  # добавление значения открытого текста
        self.HeshData[self.Ndoc].append(hash_in_t)  # добавление значения хэшей документа


        #загрузка предыдущей подписи админа
        last_admin_signature=AllFunctions.load_Admin_signature(self.Ndoc,Ntime)
        last_user_signature=AllFunctions.load_User_signature(self.Ndoc,Ntime)


        # Подписи администратора и пользователя
        admin_key, admin_cert, user = AllFunctions.Load_Admin_key_and_cert()
        signature = AllFunctions.sign_doc(user, open_text_in_str + last_admin_signature.hex(), admin_key, self.Ndoc,Ntime_new)
        user_key, user_cert, user = AllFunctions.Load_User_key_and_cert()
        signature = AllFunctions.sign_doc(user, open_text_in_str + last_user_signature.hex(), user_key, self.Ndoc,Ntime_new)


        AllFunctions.save_HeshData(self.HeshData)
        AllFunctions.save_DataToTable(self.DataToTable)
        AllFunctions.save_Different_docks(self.different_docs)

        doc.render(dictionary)
        doc.save(f'docs/document{self.Ndoc}_{Ntime_new}.docx')
        self.window.close()

class Ui_MainWindow(object):
    NDoc=0
    Ntime=0
    def __init__(self):
        super().__init__()
        self.window=QtWidgets.QMainWindow()
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


