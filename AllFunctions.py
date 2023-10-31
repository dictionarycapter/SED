from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib,json,sys,datetime,docx
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime
from cryptography.exceptions import InvalidSignature




def load_DataToTable():
    try:
        with open("Files/DataToTable.txt", encoding='utf-8') as fw:
            Data = json.load(fw)
    except:
        Data = []
    finally:
        return Data
def load_Different_docks():
    try:
        with open("Files/Different_docks.txt") as fw1:  # , encoding='utf-8'
            NoConfirmedData = json.load(fw1)
    except:
        NoConfirmedData = []
    finally:
        return NoConfirmedData
def load_HeshData():
    try:
        with open("Files/HeshData.txt") as fw1:  # , encoding='utf-8'
            NoConfirmedHash = json.load(fw1)
    except:
        NoConfirmedHash = []
    finally:
        return NoConfirmedHash

def load_Admin_signature(NDoc,Ntime):
    with open(f"signautres/Admin_signature{NDoc}_{Ntime}.bin", "rb") as f:#Admin_signature{NDoc}
        signature = f.read()
    return signature
def load_User_signature(NDoc,Ntime):
    with open(f"signautres/User_signature{NDoc}_{Ntime}.bin", "rb") as f:
        signature = f.read()
    return signature

def save_DataToTable(TableData):
    with open('Files/DataToTable.txt','w') as file:
        json.dump(TableData, file)
def save_HeshData(HeshData):
    with open('Files/HeshData.txt','w') as file:
        json.dump(HeshData, file)
def save_Different_docks(different_docs):
    with open('Files/Different_docks.txt','w') as file:
        json.dump(different_docs, file)

#Возвращает 2 значения. Ключ и сертификат
def Load_Admin_key_and_cert():
    user='Admin'
    try:
        # Загрузка закрытого ключа из файла
        with open('Files/admin_key.pem', 'rb') as f:
            admin_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )

        with open('Files/admin_cert.pem', 'rb') as f:
            admin_cert = x509.load_pem_x509_certificate(
                f.read(),
            )
    except:
        # генерация и сохранения ключа администратора
        admin_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        with open('Files/admin_key.pem', 'wb') as f:
            f.write(admin_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            ))

        # Создание запроса на сертификат администратора
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u"Admin"),
        ])
        now = datetime.datetime.utcnow()
        admin_cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(admin_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now)
            .not_valid_after(now + datetime.timedelta(days=365))
            .sign(admin_key, hashes.SHA256())
        )

        with open('Files/admin_cert.pem', 'wb') as f:
            f.write(admin_cert.public_bytes(encoding=serialization.Encoding.PEM))
    finally:
        return admin_key,admin_cert,user
def Load_User_key_and_cert():
    user='User'
    try:
        # Загрузка закрытого ключа из файла
        with open('Files/user_key.pem', 'rb') as f:
            user_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )

        with open('Files/user_cert.pem', 'rb') as f:
            user_cert = x509.load_pem_x509_certificate(
                f.read(),
            )
    except:
        # генерация и сохранения ключа администратора
        user_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        with open('Files/user_key.pem', 'wb') as f:
            f.write(user_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            ))

        # Создание запроса на сертификат администратора
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u"User"),
        ])
        now = datetime.datetime.utcnow()
        user_cert = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(user_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now)
            .not_valid_after(now + datetime.timedelta(days=365))
            .sign(user_key, hashes.SHA256())
        )

        with open('Files/user_cert.pem', 'wb') as f:
            f.write(user_cert.public_bytes(encoding=serialization.Encoding.PEM))
    finally:
        return user_key,user_cert,user
def sign_doc(user,open_text_in_str,key,NDoc,Ntime):
    signature = key.sign(open_text_in_str.encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                                      salt_length=padding.PSS.MAX_LENGTH),
                               hashes.SHA256())
    # '''Изменить название подписи'''
    with open(f'signautres/{user}_signature{NDoc}_{Ntime}.bin', 'wb') as f:
        f.write(signature)
    return signature
def verify_signature(cert,open_text_in_str,signature,user):
    try:
        cert.public_key().verify(
            signature,
            open_text_in_str.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print(f'{user} signature is ok')
        # msgBox = QtWidgets.QMessageBox.information(None, "Успех", f"Подпись {user} совпадают",
        #                               QtWidgets.QMessageBox.Yes)
    except InvalidSignature:
        print('Invalid_signature')
        return True



'''Проверить первые две функции, нужны или нет?'''
#текст следует разместить в текстовом поле
def convert_docs_to_file(document_name):
    doc = docx.Document(document_name)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)
def both_find_convert_docs(btn,DocumentWindowClass,different_docs):
    Ndoc=int(btn.text().split('_')[1])-1
    Ntime=len(different_docs[Ndoc])-1
    document_name=f"docs/document{Ndoc}_{Ntime}.docx"
    doc = docx.Document(document_name)
    DocumentWindowClass.plainTextEdit.setText('')
    text = '' #[]

    for para in doc.paragraphs:

        cursor = DocumentWindowClass.plainTextEdit.textCursor()
        style = para.style.name
        alignment = para.alignment
        # добавляем первый абзац с выравниванием по левому краю

        format = QtGui.QTextBlockFormat()
        if alignment == docx.enum.text.WD_ALIGN_PARAGRAPH.LEFT:
            format.setAlignment(QtCore.Qt.AlignLeft)
        elif alignment == docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT:
            format.setAlignment(QtCore.Qt.AlignRight)
        elif alignment == docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER:
            format.setAlignment(QtCore.Qt.AlignHCenter)
        else:
            format.setAlignment(QtCore.Qt.AlignJustify)
        cursor.mergeBlockFormat(format)

        text_format = QtGui.QTextCharFormat()
        text_format.setFont(QtGui.QFont(style))
        # DocumentWindowClass.get_data_from_TextEdit()

        # cursor.mergeBlockFormat(text_format)

        DocumentWindowClass.plainTextEdit.textCursor().insertText(para.text+'\n',text_format)
        DocumentWindowClass.Ndoc=int(btn.text().split('_')[1])-1














    #     text+=para.text #.append(para.text)
    #     text+='\n'
    #     style = para.style.name
    #     alignment = para.alignment
    #     if text:  # пропускаем пустые абзацы
    #         text_format = QtGui.QTextCharFormat()
    #         if style:  # устанавливаем стиль текста
    #             text_format.setFont(QtGui.QFont(style))
    #         else:
    #             text_format.setFont(QtGui.QFont(style))
    #         if alignment == docx.enum.text.WD_ALIGN_PARAGRAPH.LEFT:
    #             DocumentWindowClass.plainTextEdit.setAlignment(QtCore.Qt.AlignRight)#AlignLeft
    #         else:
    #             DocumentWindowClass.plainTextEdit.setAlignment(QtCore.Qt.AlignHCenter)# устанавливаем выравнивание
    #         DocumentWindowClass.plainTextEdit.textCursor().insertText(text, text_format)
    #
    # DocumentWindowClass.plainTextEdit.setPlainText(text)
    # print('\n'.join(text))
    # return '\n'.join(text)

