import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtCore import QSize, QRect
from PyQt5 import QtGui
import qtawesome as qta
import css_settings as css
from cast_main import CastMain


class CastGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_title = 'SOFT-CAST'
        self.window_icon_PATH = 'windows_icon.png'
        self.window_top = 50
        self.window_left = 500
        self.window_width = 400
        self.window_height = 600
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.window_left, self.window_top, self.window_width, self.window_height)
        self.setStyleSheet(css.background_window)
        self.initUI()
        self.show()

    def initUI(self):
        self.login_lbl = QLabel(self)
        self.login_lbl.setText('Iniciar Sesión')
        self.login_lbl.setGeometry(145,210,300,100)
        self.login_lbl.setStyleSheet(css.label_login)

        self.user_name_txtBox = QLineEdit(self)
        self.user_name_txtBox.setGeometry(100,290,200,30)
        self.user_name_txtBox.setStyleSheet(css.txtbox_user_name)
        self.user_name_txtBox.addAction(qta.icon('fa5s.user'),QLineEdit.LeadingPosition)

        self.user_password_txtBox = QLineEdit(self)
        self.user_password_txtBox.setGeometry(100,350,200,30)
        self.user_password_txtBox.setStyleSheet(css.txtbox_user_password)
        self.user_password_txtBox.setEchoMode(QLineEdit.Password)
        self.user_password_txtBox.addAction(qta.icon('fa5s.lock'),QLineEdit.LeadingPosition)
        
        self.login_btn = QPushButton(self)
        self.login_btn.setGeometry(150,430, 100, 40)
        self.login_btn.setStyleSheet(css.btn_login)
        self.login_btn.setText("INGRESAR")
        self.login_btn.clicked.connect(self.loginBtn)

    def loginBtn(self):
        self.close()
        self.register = CastMain()
        

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = CastGUI()
    sys.exit( app.exec_())
    

