from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 556)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 20, 202, 23))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 51, 23))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 51, 23))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 51, 23))
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 101, 23))
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 101, 23))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 101, 23))
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 101, 23))
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(220, 530, 202, 23))
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 391, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog) 
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 391, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)  
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 160, 391, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)  
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 200, 391, 20))
        self.lineEdit_4.setInputMask("")  
        self.lineEdit_4.setPlaceholderText("+62xxxxxxxxxxxx")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)  
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 240, 391, 121))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.comboBox = QtWidgets.QComboBox(Dialog)  
        self.comboBox.setGeometry(QtCore.QRect(130, 380, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["", "Laki-laki", "Perempuan"])

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 420, 211, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["", "SD", "SMP", "SMA", "Diploma", "Sarjana", "Magister", "Doktor"])

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)          
        self.pushButton_3.setGeometry(QtCore.QRect(130, 480, 181, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.save_data)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)  
        self.pushButton_2.setGeometry(QtCore.QRect(340, 480, 181, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clear_fields)

        self.shortcut_quit = QtWidgets.QShortcut(QtGui.QKeySequence("Q"), Dialog)
        self.shortcut_quit.activated.connect(QtWidgets.qApp.quit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Form Data"))
        self.label.setText(_translate("Dialog", "Masukkan Data Anda"))
        self.label_2.setText(_translate("Dialog", "Nama :"))
        self.label_3.setText(_translate("Dialog", "Email :"))
        self.label_4.setText(_translate("Dialog", "Age :"))
        self.label_5.setText(_translate("Dialog", "Phone Number :"))
        self.label_6.setText(_translate("Dialog", "Address :"))
        self.label_7.setText(_translate("Dialog", "Gender :"))
        self.label_8.setText(_translate("Dialog", "Education :"))
        self.label_9.setText(_translate("Dialog", "Rizki Rahman Maulana | F1D022093"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.pushButton_3.setText(_translate("Dialog", "Save"))

    def show_warning(self, message):
        QtWidgets.QMessageBox.warning(None, "Validasi Gagal", message)

    def validate_input(self):
        name = self.lineEdit_2.text().strip()
        email = self.lineEdit.text().strip()
        age = self.lineEdit_3.text().strip()
        phone = self.lineEdit_4.text().strip()
        address = self.plainTextEdit.toPlainText().strip()
        gender = self.comboBox.currentText()
        education = self.comboBox_2.currentText()

        if not name:
            self.show_warning("Nama tidak boleh kosong.")
            return False
        if not email or not QtCore.QRegExp(r"[^@]+@[^@]+\.[^@]+").exactMatch(email):
            self.show_warning("Format email tidak valid.")
            return False
        if not age.isdigit():
            self.show_warning("Umur harus berupa angka.")
            return False
        if not phone.startswith("+62") or len(phone.replace("+", "").replace(" ", "")) != 13:
            self.show_warning("Nomor telepon harus diawali dengan +62 dan terdiri dari 13 digit angka.")
            return False
        if not address:
            self.show_warning("Alamat tidak boleh kosong.")
            return False
        if not gender:
            self.show_warning("Silakan pilih jenis kelamin.")
            return False
        if not education:
            self.show_warning("Silakan pilih pendidikan.")
            return False
        return True

    def save_data(self):
        if self.validate_input():
            print("Data berhasil disimpan:")
            print(f"Nama: {self.lineEdit_2.text()}")
            print(f"Email: {self.lineEdit.text()}")
            print(f"Umur: {self.lineEdit_3.text()}")
            print(f"No HP: {self.lineEdit_4.text()}")
            print(f"Alamat: {self.plainTextEdit.toPlainText()}")
            print(f"Gender: {self.comboBox.currentText()}")
            print(f"Pendidikan: {self.comboBox_2.currentText()}")

            QtWidgets.QMessageBox.information(None, "Sukses", "Data berhasil disimpan.")
            self.clear_fields()

    def clear_fields(self):
        self.lineEdit_2.clear()
        self.lineEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.plainTextEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
