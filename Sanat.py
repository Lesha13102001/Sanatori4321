import sys
import datetime
import re
from datetime import date

d=date.today()

import pymysql
from Config import host, user, password, db_name

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QMessageBox

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
except Exception as ex:
    print("Connection refused...")
    print(ex)

pattern=re.compile(r"^[+-9-0]")
pattern2=re.compile("[a-zA-Z-а-яА-Я]")


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        layout = QHBoxLayout()
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 588)
        self.pushButton_admin = QtWidgets.QPushButton(Dialog)
        self.pushButton_admin.setGeometry(QtCore.QRect(650, 10, 101, 23))
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.label_main = QtWidgets.QLabel(Dialog)
        self.label_main.setGeometry(QtCore.QRect(200, 0, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_main.setFont(font)
        self.label_main.setTabletTracking(False)
        self.label_main.setStyleSheet("")
        self.label_main.setTextFormat(QtCore.Qt.AutoText)
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setWordWrap(False)
        self.label_main.setObjectName("label_main")
        self.dateEdit_start = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_start.setGeometry(QtCore.QRect(10, 110, 110, 22))
        self.dateEdit_start.setDate(QtCore.QDate(d.year, d.month, d.day))
        self.dateEdit_start.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.label_data_main = QtWidgets.QLabel(Dialog)
        self.label_data_main.setGeometry(QtCore.QRect(20, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("ScriptS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_data_main.setFont(font)
        self.label_data_main.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_data_main.setScaledContents(False)
        self.label_data_main.setObjectName("label_data_main")
        self.label_data_start = QtWidgets.QLabel(Dialog)
        self.label_data_start.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_data_start.setFont(font)
        self.label_data_start.setObjectName("label_data_start")
        self.label_data_end = QtWidgets.QLabel(Dialog)
        self.label_data_end.setGeometry(QtCore.QRect(150, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_data_end.setFont(font)
        self.label_data_end.setObjectName("label_data_end")
        self.dateEdit_end = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_end.setGeometry(QtCore.QRect(150, 110, 110, 22))
        self.dateEdit_end.setDate(QtCore.QDate(d.year, d.month, d.day))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.label_info_main = QtWidgets.QLabel(Dialog)
        self.label_info_main.setGeometry(QtCore.QRect(20, 140, 351, 41))
        font = QtGui.QFont()
        font.setFamily("ScriptS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_info_main.setFont(font)
        self.label_info_main.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_info_main.setScaledContents(False)
        self.label_info_main.setObjectName("label_info_main")
        self.label_info_telephone = QtWidgets.QLabel(Dialog)
        self.label_info_telephone.setGeometry(QtCore.QRect(20, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_info_telephone.setFont(font)
        self.label_info_telephone.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_info_telephone.setObjectName("label_info_telephone")
        self.lineEdit_telephone = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_telephone.setGeometry(QtCore.QRect(30, 210, 111, 20))
        self.lineEdit_telephone.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_telephone.setMaxLength(13)
        self.lineEdit_telephone.setObjectName("lineEdit_telephone")
        self.label_info_name2 = QtWidgets.QLabel(Dialog)
        self.label_info_name2.setGeometry(QtCore.QRect(30, 240, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_name2.setFont(font)
        self.label_info_name2.setObjectName("label_info_name2")
        self.label_info_name1 = QtWidgets.QLabel(Dialog)
        self.label_info_name1.setGeometry(QtCore.QRect(160, 240, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_name1.setFont(font)
        self.label_info_name1.setObjectName("label_info_name1")
        self.label_info_name3 = QtWidgets.QLabel(Dialog)
        self.label_info_name3.setGeometry(QtCore.QRect(290, 240, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_name3.setFont(font)
        self.label_info_name3.setObjectName("label_info_name3")
        self.lineEdit_name2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name2.setGeometry(QtCore.QRect(30, 270, 111, 20))
        self.lineEdit_name2.setObjectName("lineEdit_name2")
        self.lineEdit_name1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name1.setGeometry(QtCore.QRect(160, 270, 111, 20))
        self.lineEdit_name1.setObjectName("lineEdit_name1")
        self.lineEdit_name3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name3.setGeometry(QtCore.QRect(290, 270, 111, 20))
        self.lineEdit_name3.setObjectName("lineEdit_name3")
        self.label_info_name3_2 = QtWidgets.QLabel(Dialog)
        self.label_info_name3_2.setGeometry(QtCore.QRect(490, 240, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_name3_2.setFont(font)
        self.label_info_name3_2.setObjectName("label_info_name3_2")
        self.comboBox_birthday = QtWidgets.QComboBox(Dialog)
        self.comboBox_birthday.setGeometry(QtCore.QRect(490, 270, 101, 22))
        self.comboBox_birthday.setObjectName("comboBox_birthday")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.comboBox_birthday.addItem("")
        self.label_diagnoz = QtWidgets.QLabel(Dialog)
        self.label_diagnoz.setGeometry(QtCore.QRect(20, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("ScriptS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_diagnoz.setFont(font)
        self.label_diagnoz.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_diagnoz.setScaledContents(False)
        self.label_diagnoz.setObjectName("label_diagnoz")
        self.comboBox_diagnoz1 = QtWidgets.QComboBox(Dialog)
        self.comboBox_diagnoz1.setGeometry(QtCore.QRect(40, 370, 231, 22))
        self.comboBox_diagnoz1.setObjectName("comboBox_diagnoz1")
        self.comboBox_diagnoz1.addItem("Желудочно-кишечное заболевание", ["Физиотерапевтические процедуры", "Очистка кишечника", "Массаж", "Курсовой прием минеральных вод"])
        self.comboBox_diagnoz1.addItem("Остеохондроз", ["Ультразвуковая остеоденситометрия", "Ударно-волновая терапия на аппарате Вакумед", "Ванны нафталоновые", "Кедровая бочка"])
        self.comboBox_diagnoz1.addItem("Ангина", ["Системная антибактериальная терапия", "Местное симптоматическое лечение", "А.Т. с назначением аитигистаминных препаратов"])
        self.comboBox_diagnoz1.addItem("Сколиоз", ["Массаж спины", "Лечебная физкультура (ЛФК)", "Интерференцтерапия", "Грязелечение"])
        layout.addWidget(self.comboBox_diagnoz1)
        self.label_diagnoz1 = QtWidgets.QLabel(Dialog)
        self.label_diagnoz1.setGeometry(QtCore.QRect(30, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_diagnoz1.setFont(font)
        self.label_diagnoz1.setObjectName("label_diagnoz1")
        self.label_diagnoz2 = QtWidgets.QLabel(Dialog)
        self.label_diagnoz2.setGeometry(QtCore.QRect(330, 330, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_diagnoz2.setFont(font)
        self.label_diagnoz2.setObjectName("label_diagnoz2")
        self.comboBox_diagnoz2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_diagnoz2.setGeometry(QtCore.QRect(340, 370, 281, 22))
        self.comboBox_diagnoz2.setObjectName("comboBox_diagnoz2")
        layout.addWidget(self.comboBox_diagnoz2)
        self.pushButton_accept = QtWidgets.QPushButton(Dialog)
        self.pushButton_accept.setGeometry(QtCore.QRect(190, 510, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.pushButton_accept.setFont(font)
        self.pushButton_accept.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.506091, y1:0.586, x2:0.489, y2:0, stop:0.573864 rgba(255, 106, 5, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.pushButton_cancle = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancle.setGeometry(QtCore.QRect(400, 510, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.pushButton_cancle.setFont(font)
        self.pushButton_cancle.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.506091, y1:0.586, x2:0.489, y2:0, stop:0.573864 rgba(255, 106, 5, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_cancle.setObjectName("pushButton_cancle")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add_functions()

        self.comboBox_diagnoz1.currentIndexChanged.connect(self.updatediagnoz)

        self.updatediagnoz(self.comboBox_diagnoz1.currentIndex())


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Санаторий"))
        self.pushButton_admin.setText(_translate("Dialog", "Администратор"))
        self.label_main.setText(_translate("Dialog", "Заявка в санаторий"))
        self.dateEdit_start.setDisplayFormat(_translate("Dialog", "yyyy.MM.dd"))
        self.label_data_main.setText(_translate("Dialog", "1. Даты завезда"))
        self.label_data_start.setText(_translate("Dialog", "Дата заезда *"))
        self.label_data_end.setText(_translate("Dialog", "Дата отъезда *"))
        self.dateEdit_end.setDisplayFormat(_translate("Dialog", "yyyy.MM.dd"))
        self.label_info_main.setText(_translate("Dialog", "2. Контактная информация"))
        self.label_info_telephone.setText(_translate("Dialog", "Мобильный телефон *"))
        self.lineEdit_telephone.setText(_translate("Dialog", "+375"))
        self.label_info_name2.setText(_translate("Dialog", "Фамилия *"))
        self.label_info_name1.setText(_translate("Dialog", "Имя *"))
        self.label_info_name3.setText(_translate("Dialog", "Отчетсво *"))
        self.label_info_name3_2.setText(_translate("Dialog", "Год рождения"))
        self.comboBox_birthday.setCurrentText(_translate("Dialog", "2004"))
        self.comboBox_birthday.setItemText(0, _translate("Dialog", "2004"))
        self.comboBox_birthday.setItemText(1, _translate("Dialog", "2003"))
        self.comboBox_birthday.setItemText(2, _translate("Dialog", "2002"))
        self.comboBox_birthday.setItemText(3, _translate("Dialog", "2001"))
        self.comboBox_birthday.setItemText(4, _translate("Dialog", "2000"))
        self.comboBox_birthday.setItemText(5, _translate("Dialog", "1999"))
        self.comboBox_birthday.setItemText(6, _translate("Dialog", "1998"))
        self.comboBox_birthday.setItemText(7, _translate("Dialog", "1997"))
        self.comboBox_birthday.setItemText(8, _translate("Dialog", "1996"))
        self.comboBox_birthday.setItemText(9, _translate("Dialog", "1995"))
        self.comboBox_birthday.setItemText(10, _translate("Dialog", "1994"))
        self.comboBox_birthday.setItemText(11, _translate("Dialog", "1993"))
        self.comboBox_birthday.setItemText(12, _translate("Dialog", "1992"))
        self.comboBox_birthday.setItemText(13, _translate("Dialog", "1991"))
        self.comboBox_birthday.setItemText(14, _translate("Dialog", "1990"))
        self.comboBox_birthday.setItemText(15, _translate("Dialog", "1989"))
        self.comboBox_birthday.setItemText(16, _translate("Dialog", "1988"))
        self.comboBox_birthday.setItemText(17, _translate("Dialog", "1987"))
        self.comboBox_birthday.setItemText(18, _translate("Dialog", "1986"))
        self.comboBox_birthday.setItemText(19, _translate("Dialog", "1985"))
        self.comboBox_birthday.setItemText(20, _translate("Dialog", "1984"))
        self.comboBox_birthday.setItemText(21, _translate("Dialog", "1983"))
        self.comboBox_birthday.setItemText(22, _translate("Dialog", "1982"))
        self.comboBox_birthday.setItemText(23, _translate("Dialog", "1981"))
        self.comboBox_birthday.setItemText(24, _translate("Dialog", "1980"))
        self.comboBox_birthday.setItemText(25, _translate("Dialog", "1979"))
        self.comboBox_birthday.setItemText(26, _translate("Dialog", "1978"))
        self.comboBox_birthday.setItemText(27, _translate("Dialog", "1977"))
        self.comboBox_birthday.setItemText(28, _translate("Dialog", "1976"))
        self.comboBox_birthday.setItemText(29, _translate("Dialog", "1975"))
        self.comboBox_birthday.setItemText(30, _translate("Dialog", "1974"))
        self.comboBox_birthday.setItemText(31, _translate("Dialog", "1973"))
        self.comboBox_birthday.setItemText(32, _translate("Dialog", "1972"))
        self.comboBox_birthday.setItemText(33, _translate("Dialog", "1971"))
        self.comboBox_birthday.setItemText(34, _translate("Dialog", "1970"))
        self.comboBox_birthday.setItemText(35, _translate("Dialog", "1969"))
        self.comboBox_birthday.setItemText(36, _translate("Dialog", "1968"))
        self.comboBox_birthday.setItemText(37, _translate("Dialog", "1967"))
        self.comboBox_birthday.setItemText(38, _translate("Dialog", "1966"))
        self.comboBox_birthday.setItemText(39, _translate("Dialog", "1965"))
        self.comboBox_birthday.setItemText(40, _translate("Dialog", "1964"))
        self.comboBox_birthday.setItemText(41, _translate("Dialog", "1963"))
        self.comboBox_birthday.setItemText(42, _translate("Dialog", "1962"))
        self.comboBox_birthday.setItemText(43, _translate("Dialog", "1961"))
        self.comboBox_birthday.setItemText(44, _translate("Dialog", "1960"))
        self.comboBox_birthday.setItemText(45, _translate("Dialog", "1959"))
        self.comboBox_birthday.setItemText(46, _translate("Dialog", "1958"))
        self.comboBox_birthday.setItemText(47, _translate("Dialog", "1957"))
        self.comboBox_birthday.setItemText(48, _translate("Dialog", "1956"))
        self.comboBox_birthday.setItemText(49, _translate("Dialog", "1955"))
        self.comboBox_birthday.setItemText(50, _translate("Dialog", "1954"))
        self.comboBox_birthday.setItemText(51, _translate("Dialog", "1953"))
        self.comboBox_birthday.setItemText(52, _translate("Dialog", "1952"))
        self.comboBox_birthday.setItemText(53, _translate("Dialog", "1951"))
        self.comboBox_birthday.setItemText(54, _translate("Dialog", "1950"))
        self.comboBox_birthday.setItemText(55, _translate("Dialog", "1949"))
        self.comboBox_birthday.setItemText(56, _translate("Dialog", "1948"))
        self.comboBox_birthday.setItemText(57, _translate("Dialog", "1947"))
        self.comboBox_birthday.setItemText(58, _translate("Dialog", "1946"))
        self.comboBox_birthday.setItemText(59, _translate("Dialog", "1945"))
        self.comboBox_birthday.setItemText(60, _translate("Dialog", "1944"))
        self.comboBox_birthday.setItemText(61, _translate("Dialog", "1943"))
        self.comboBox_birthday.setItemText(62, _translate("Dialog", "1942"))
        self.comboBox_birthday.setItemText(63, _translate("Dialog", "1941"))
        self.comboBox_birthday.setItemText(64, _translate("Dialog", "1940"))
        self.comboBox_birthday.setItemText(65, _translate("Dialog", "1939"))
        self.comboBox_birthday.setItemText(66, _translate("Dialog", "1938"))
        self.comboBox_birthday.setItemText(67, _translate("Dialog", "1937"))
        self.comboBox_birthday.setItemText(68, _translate("Dialog", "1936"))
        self.comboBox_birthday.setItemText(69, _translate("Dialog", "1935"))
        self.comboBox_birthday.setItemText(70, _translate("Dialog", "1933"))
        self.comboBox_birthday.setItemText(71, _translate("Dialog", "1932"))
        self.label_diagnoz.setText(_translate("Dialog", "3. Диагноз"))
        self.label_diagnoz1.setText(_translate("Dialog", "1. Поставленный диагноз"))
        self.label_diagnoz2.setText(_translate("Dialog", "2. Оздоровительная программа"))
        self.pushButton_accept.setText(_translate("Dialog", "Отправить заявку"))
        self.pushButton_cancle.setText(_translate("Dialog", "Сбросить"))

    def add_functions(self):
        self.pushButton_accept.clicked.connect(lambda: self.write_to_bd(self.lineEdit_name1.text(), self.lineEdit_name2.text(), self.lineEdit_name3.text(), self.comboBox_birthday.currentText(), self.lineEdit_telephone.text(), self.dateEdit_start.text(), self.dateEdit_end.text(), self.comboBox_diagnoz1.currentText(), self.comboBox_diagnoz2.currentText()))
        self.pushButton_cancle.clicked.connect(lambda: self.reset())


    def reset(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_telephone.setText(_translate("Dialog", "+375"))
        self.lineEdit_name1.setText("")
        self.lineEdit_name2.setText("")
        self.lineEdit_name3.setText("")
        self.dateEdit_start.setDate(d)
        self.dateEdit_end.setDate(d)
        self.comboBox_birthday.setCurrentIndex(0)
        self.comboBox_diagnoz1.setCurrentIndex(0)
        self.comboBox_diagnoz2.setCurrentIndex(0)




    def write_to_bd(self, Name, Surname, Patronymic, Age, Tel, Date_st, Date_end, Diagn, Prog):
        if (Name==''):
            add = QMessageBox()
            add.setWindowTitle("Ошибка")
            add.setText("Поле Имя пустое!")
            add.setStandardButtons(QMessageBox.Ok)
            add.exec_()
            return
        if (Surname==''):
            add = QMessageBox()
            add.setWindowTitle("Ошибка")
            add.setText("Поле Фамилия пустое!")
            add.setStandardButtons(QMessageBox.Ok)
            add.exec_()
            return
        if (Patronymic==''):
            add = QMessageBox()
            add.setWindowTitle("Ошибка")
            add.setText("Поле Отчество пустое!")
            add.setStandardButtons(QMessageBox.Ok)
            add.exec_()
            return
        if (Tel==''):
            add = QMessageBox()
            add.setWindowTitle("Ошибка")
            add.setText("Поле Номер телефона пустое!")
            add.setStandardButtons(QMessageBox.Ok)
            add.exec_()
            return
        for i in Name:
            if not pattern2.match(i):
                add = QMessageBox()
                add.setWindowTitle("Ошибка")
                add.setText("Неправильно введино Имя")
                add.setStandardButtons(QMessageBox.Ok)
                add.exec_()
                return
        for i in Surname:
            if not pattern2.match(i):
                add = QMessageBox()
                add.setWindowTitle("Ошибка")
                add.setText("Неправильно введина Фамилия")
                add.setStandardButtons(QMessageBox.Ok)
                add.exec_()
                return
        for i in Patronymic:
            if not pattern2.match(i):
                add = QMessageBox()
                add.setWindowTitle("Ошибка")
                add.setText("Неправильно введино Отчество")
                add.setStandardButtons(QMessageBox.Ok)
                add.exec_()
                return
        for i in Tel:
            if not pattern.match(i):
                add = QMessageBox()
                add.setWindowTitle("Ошибка")
                add.setText("Неправильно введён номер телефона")
                add.setStandardButtons(QMessageBox.Ok)
                add.exec_()
                return
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `usr_app` (name, surname, patronymic, age, telephone, data_st, data_end, diagnoz, programma) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (Name, Surname, Patronymic, Age, Tel, Date_st, Date_end, Diagn, Prog)
            cursor.execute(insert_query)
            connection.commit()
        add = QMessageBox()
        add.setWindowTitle("Заявка")
        add.setText("Заявка отправлена на рассмотрение")
        add.setStandardButtons(QMessageBox.Ok)
        add.exec_()


    def updatediagnoz(self, index):
        self.comboBox_diagnoz2.clear()
        programs = self.comboBox_diagnoz1.itemData(index)
        if programs:
            self.comboBox_diagnoz2.addItems(programs)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
