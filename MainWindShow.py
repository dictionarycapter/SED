from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QTableWidgetItem
import sys
from docxtpl import DocxTemplate
import MainWindow,RRK,AllFunctions,Diffenece,TryToConvert
import json

#For compiling
from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib,json,sys,datetime,docx
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime
from cryptography.exceptions import InvalidSignature



import doucment

DataToTable=AllFunctions.load_DataToTable()
HeshData=AllFunctions.load_HeshData()
DifferentDocs=AllFunctions.load_Different_docks()



if __name__=='__main__':
    app=QApplication(sys.argv)

    # FirstClass.check_for_changes()

    SecondWindowClass=RRK.Ui_Form()


    DiffeneceClass = Diffenece.Ui_Form()


    DocumentWindowClass=doucment.Ui_Form(DiffeneceClass)
    #
    # DocumentWindowClass.setupUi(DocumentWindowClass.window)



    FirstClass = MainWindow.Ui_MainWindow()
    FirstClass.setupUi(FirstClass.window, DocumentWindowClass)


    Journal_Class=TryToConvert.Ui_Form()






    FirstClass.action_2.triggered.connect(lambda: SecondWindowClass.show_form(SecondWindowClass.window))
    SecondWindowClass.pushButton.clicked.connect(SecondWindowClass.add_new_document)
    FirstClass.pushButton.clicked.connect(lambda: FirstClass.check_for_changes_all_files())
    FirstClass.pushButton.clicked.connect(Journal_Class.window.show)





    sys.exit(app.exec_())







