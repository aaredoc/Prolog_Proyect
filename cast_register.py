import sys
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QTextEdit, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import QtGui
import qtawesome as qta
import css_settings as css
from cast_test import CastTest

class CastRegister(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_title = 'SOFT-CAST : NUEVO REGISTRO'
        self.window_icon_PATH = 'windows_icon.png'
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.window_top = 100
        self.window_left = 550
        self.window_width = 400
        self.window_height = 600
        self.reg_date = datetime.now()
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.window_left, self.window_top,
                         self.window_width, self.window_height)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.initUI()
        self.show()

    def initUI(self):

        self.lbl_register_title = QLabel(self)
        self.lbl_register_title.setGeometry(100, 10, 200, 100)
        self.lbl_register_title.setText('Registro')
        self.lbl_register_title.setStyleSheet(css.lbl_register_title)

        self.lbl_register_name = QLabel(self)
        self.lbl_register_name.setGeometry(100, 100, 150, 60)
        self.lbl_register_name.setText('Nombre/s')
        self.lbl_register_name.setStyleSheet(css.lbl_register)

        self.txtBox_register_name = QLineEdit(self)
        self.txtBox_register_name.setGeometry(100, 140, 200, 40)
        self.txtBox_register_name.setStyleSheet(css.txtbox_register)
        self.txtBox_register_name.addAction(
            qta.icon('fa5s.user-edit'), QLineEdit.LeadingPosition)

        self.lbl_register_lastname = QLabel(self)
        self.lbl_register_lastname.setGeometry(100, 180, 150, 60)
        self.lbl_register_lastname.setText('Apellidos')
        self.lbl_register_lastname.setStyleSheet(css.lbl_register)

        self.txtBox_register_lastname = QLineEdit(self)
        self.txtBox_register_lastname.setGeometry(100, 220, 200, 40)
        self.txtBox_register_lastname.setStyleSheet(css.txtbox_register)
        self.txtBox_register_lastname.addAction(
            qta.icon('fa5s.user-edit'), QLineEdit.LeadingPosition)

        self.lbl_register_dni = QLabel(self)
        self.lbl_register_dni.setGeometry(100, 260, 300, 60)
        self.lbl_register_dni.setText('Documento de Identidad')
        self.lbl_register_dni.setStyleSheet(css.lbl_register)

        self.txtbox_register_dni = QLineEdit(self)
        self.txtbox_register_dni.setGeometry(100, 300, 200, 40)
        self.txtbox_register_dni.setStyleSheet(css.txtbox_register)
        self.txtbox_register_dni.addAction(
            qta.icon('fa5s.id-card'), QLineEdit.LeadingPosition)

        self.lbl_register_date = QLabel(self)
        self.lbl_register_date.setGeometry(100, 340, 150, 60)
        self.lbl_register_date.setText('Fecha de Ingreso')
        self.lbl_register_date.setStyleSheet(css.lbl_register)

        self.txtBox_register_date = QLineEdit(self)
        self.txtBox_register_date.setGeometry(100, 380, 200, 40)
        self.txtBox_register_date.setStyleSheet(css.txtbox_register)
        self.txtBox_register_date.addAction(
            qta.icon('fa5s.calendar-alt'), QLineEdit.LeadingPosition)
        self.txtBox_register_date.setText(
            f'{self.reg_date.day}/{self.reg_date.month}/{self.reg_date.year}')

        self.btn_ok = QPushButton(self)
        self.btn_ok.setText('Aceptar')
        self.btn_ok.setGeometry(145, 500, 110, 50)
        self.btn_ok.setStyleSheet(css.btn_acept_cancel)
        self.btn_ok.clicked.connect(self.ok_clicked)

    def ok_clicked(self):
        dni = self.txtbox_register_dni.text()
        name = self.txtBox_register_name.text()
        lastname = self.txtBox_register_lastname.text()
        date = f'{self.reg_date.year}-{self.reg_date.month}-{self.reg_date.day}'
        self.close()
        self.new_test = CastTest(dni, name, lastname, date)
