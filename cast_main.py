import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QFileDialog, QPushButton, QTextEdit, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, QRect
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
import qtawesome as qta
import css_settings as css
from cast_register import CastRegister
from cast_db import CastDB


class CastMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_title = 'SOFT-CAST'
        self.window_icon_PATH = 'windows_icon.png'
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.window_top = 50
        self.window_left = 300
        self.window_width = 800
        self.window_height = 600
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.window_left, self.window_top,
                         self.window_width, self.window_height)
        self.initUI()
        self.getDataBase()
        self.show()

    def initUI(self):

        self.labelImage = QLabel(self)
        self.pixmap = QPixmap("autismo.png")
        self.labelImage.setPixmap(self.pixmap)
        self.labelImage.setGeometry(80, 55, 100, 100)

        self.btn_register = QPushButton(self)
        self.btn_register.setText("REGISTRAR")
        self.btn_register.setIcon(qta.icon('fa5s.address-card'))
        self.btn_register.setGeometry(50, 200, 150, 60)
        self.btn_register.setStyleSheet(css.btn_register)
        self.btn_register.clicked.connect(self.register_clicked)

        self.btn_progress = QPushButton(self)
        self.btn_progress.setText("ACTUALIZAR")
        self.btn_progress.setIcon(qta.icon('fa5s.edit'))
        self.btn_progress.setGeometry(50, 280, 150, 60)
        self.btn_progress.setStyleSheet(css.btn_progress)

        self.btn_progress = QPushButton(self)
        self.btn_progress.setText("PROGRESO")
        self.btn_progress.setIcon(qta.icon('fa5s.chart-line'))
        self.btn_progress.setGeometry(50, 360, 150, 60)
        self.btn_progress.setStyleSheet(css.btn_sugerency)

        self.btn_quit = QPushButton(self)
        self.btn_quit.setText("SALIR")
        self.btn_quit.setIcon(qta.icon('fa5s.sign-out-alt'))
        self.btn_quit.setGeometry(50, 440, 150, 60)
        self.btn_quit.setStyleSheet(css.btn_exit)
        self.btn_quit.clicked.connect(QtCore.QCoreApplication.quit)

        self.label_titleTable = QLabel(self)
        self.label_titleTable.setText("REGISTRO DE DATOS")
        self.label_titleTable.setGeometry(240, 40, 350, 100)
        self.label_titleTable.setStyleSheet(css.lbl_titleTable)

        self.txtbox_searchbar = QLineEdit(self)
        self.txtbox_searchbar.setGeometry(250, 150, 450, 30)
        self.txtbox_searchbar.addAction(
            qta.icon('fa5s.search'), QLineEdit.LeadingPosition)
        self.txtbox_searchbar.setStyleSheet(css.txt_search)
        self.txtbox_searchbar.textChanged.connect(self.updateDisplay)

        self.table_database = QTableWidget(self)
        self.table_database.setGeometry(250, 200, 452, 300)
        self.table_database.setRowCount(20)
        self.table_database.setColumnCount(4)
        self.table_database.setHorizontalHeaderLabels(
            ['D.N.I', 'NOMBRES', 'APELLIDOS', 'INGRESO'])
        self.table_database.setStyleSheet('font-size: 12px')

        self.btn_refresh = QPushButton(self)
        self.btn_refresh.setGeometry(652, 500, 50, 40)
        self.btn_refresh.setIcon(qta.icon('fa5s.sync-alt'))
        self.btn_refresh.clicked.connect(self.getDataBase)

    def register_clicked(self):
        self.new_register = CastRegister()

    def getDataBase(self):
        self.bd = CastDB('', '', '', '', '')
        data = self.bd.getBD()
        rows = len(data)
        column = len(data[0])-1
        i = 1
        j = 0
        for i in range(rows):
            for j in range(column):
                self.table_database.setItem(
                    i, j, QTableWidgetItem(str(data[i][j])))
        self.table_database.sortByColumn(0, QtCore.Qt.DescendingOrder)

    def updateDisplay(self):
        pass
