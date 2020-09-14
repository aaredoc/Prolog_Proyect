import sys
from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QCheckBox, QTabWidget, QPushButton, QTextEdit, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
import qtawesome as qta
import css_settings as css
from cast_db import CastDB

class CastTest(QMainWindow):
    def __init__(self, dni, name, lastname, date):
        super().__init__()
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.date = date
        self.window_title = 'SOFT-CAST : TEST'
        self.window_icon_PATH = 'windows_icon.png'
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.window_top = 100
        self.window_left = 400
        self.window_width = 700
        self.window_height = 650
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.window_left, self.window_top,
                         self.window_width, self.window_height)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.initUI()
        self.show()

    def initUI(self):
        self.lbl_title_table = QLabel(self)
        self.lbl_title_table.setText('CUESTIONARIO')
        self.lbl_title_table.setGeometry(50, 40, 300, 60)
        self.lbl_title_table.setStyleSheet(css.lbl_register_title)

        self.table_questions = QTableWidget(self)
        self.table_questions.setGeometry(50, 95, 600, 450)
        self.table_questions.setRowCount(39)
        self.table_questions.setColumnCount(2)
        self.table_questions.setHorizontalHeaderLabels(
            ['Preguntas', 'Seleccionar'])
        self.table_questions.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.table_questions.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Fixed)
        self.table_questions.verticalHeader().setDefaultSectionSize(50)
        self.table_questions.setItem(0, 0, QTableWidgetItem(
            '¿Participa fácilmente en los juegos con otros niños?'))
        self.table_questions.setItem(1, 0, QTableWidgetItem(
            '¿Se le acerca espontáneamente para charlar?'))
        self.table_questions.setItem(
            2, 0, QTableWidgetItem('¿Hablaba a los 2 años?'))
        self.table_questions.setItem(
            3, 0, QTableWidgetItem('¿Le gustan los deportes?'))
        self.table_questions.setItem(4, 0, QTableWidgetItem(
            '¿Es importante para él / ella encajar en el grupo de compañeros?'))
        self.table_questions.setItem(5, 0, QTableWidgetItem(
            '¿Parece notar detalles inusuales que los demás pasan por alto?'))
        self.table_questions.setItem(6, 0, QTableWidgetItem(
            '¿Tiende a tomar las cosas literalmente?'))
        self.table_questions.setItem(7, 0, QTableWidgetItem(
            'Cuando tenía 3 años, ¿pasó mucho tiempo fingiendo?'))
        self.table_questions.setItem(8, 0, QTableWidgetItem(
            '¿Le gusta hacer las cosas una y otra vez, de la \nmisma manera todo el tiempo?'))
        self.table_questions.setItem(9, 0, QTableWidgetItem(
            '¿Le resulta fácil interactuar con otros niños?'))
        self.table_questions.setItem(10, 0, QTableWidgetItem(
            '¿Puede mantener una conversación bidireccional?'))
        self.table_questions.setItem(11, 0, QTableWidgetItem(
            '¿Puede leer apropiadamente para su edad?'))
        self.table_questions.setItem(12, 0, QTableWidgetItem(
            '¿Tiene mayoritariamente los mismos intereses que sus compañeros?'))
        self.table_questions.setItem(13, 0, QTableWidgetItem(
            '¿Tiene un interés que le ocupa tanto tiempo que hace poco más?'))
        self.table_questions.setItem(14, 0, QTableWidgetItem(
            '¿Tiene amigos y no solo conocidos?'))
        self.table_questions.setItem(15, 0, QTableWidgetItem(
            '¿A menudo te trae cosas que le interesan para mostrarte?'))
        self.table_questions.setItem(
            16, 0, QTableWidgetItem('¿Le gusta bromear?'))
        self.table_questions.setItem(17, 0, QTableWidgetItem(
            '¿Tiene dificultad para entender las reglas del comportamiento cortés?'))
        self.table_questions.setItem(18, 0, QTableWidgetItem(
            '¿Parece tener una memoria inusual para los detalles?'))
        self.table_questions.setItem(19, 0, QTableWidgetItem(
            '¿Su voz es inusual (p. Ej., Demasiado adulta, plana o muy monótona)?'))
        self.table_questions.setItem(20, 0, QTableWidgetItem(
            '¿Son las personas importantes para él / ella?'))
        self.table_questions.setItem(
            21, 0, QTableWidgetItem('¿Puede vestirse solo?'))
        self.table_questions.setItem(22, 0, QTableWidgetItem(
            '¿Es bueno tomando turnos en una conversación?'))
        self.table_questions.setItem(23, 0, QTableWidgetItem(
            '¿Juega imaginativamente con otros niños y participa en juegos de roles?'))
        self.table_questions.setItem(24, 0, QTableWidgetItem(
            '¿A menudo hace o dice cosas sin tacto o socialmente inapropiadas?'))
        self.table_questions.setItem(25, 0, QTableWidgetItem(
            '¿Puede contar hasta 50 sin omitir ningún número?'))
        self.table_questions.setItem(
            26, 0, QTableWidgetItem('¿Hace contacto visual normal?'))
        self.table_questions.setItem(27, 0, QTableWidgetItem(
            '¿Tiene movimientos inusuales y repetitivos?'))
        self.table_questions.setItem(28, 0, QTableWidgetItem(
            '¿Su comportamiento social es muy unilateral y siempre en sus propios términos?'))
        self.table_questions.setItem(29, 0, QTableWidgetItem(
            '¿A veces dice "usted" o "él / ella" cuando se refiere a "yo"?'))
        self.table_questions.setItem(30, 0, QTableWidgetItem(
            '¿Prefiere actividades imaginativas en lugar de números o listas de hechos?'))
        self.table_questions.setItem(31, 0, QTableWidgetItem(
            '¿A veces pierde al oyente por no explicar de qué está hablando?'))
        self.table_questions.setItem(32, 0, QTableWidgetItem(
            '¿Puede andar en bicicleta (incluso si tiene estabilizadores)?'))
        self.table_questions.setItem(33, 0, QTableWidgetItem(
            '¿Trata de imponerse rutinas a sí mismo, oa los demás, de tal forma que le cause problemas?'))
        self.table_questions.setItem(34, 0, QTableWidgetItem(
            '¿Le importa cómo es percibido por el resto del grupo?'))
        self.table_questions.setItem(35, 0, QTableWidgetItem(
            '¿Cambia las conversaciones a su tema favorito en lugar de seguir lo que la otra persona quiere hablar?'))
        self.table_questions.setItem(36, 0, QTableWidgetItem(
            '¿Tiene frases raras o inusuales?'))
        self.table_questions.setItem(37, 0, QTableWidgetItem(
            '¿Han expresado alguna vez los maestros alguna preocupación sobre su desarrollo?'))
        self.table_questions.setItem(38, 0, QTableWidgetItem(
            '¿Le han diagnosticado: retraso en el lenguaje, TDAH, dificultades auditivas o visuales, trast. del espectro autista?'))

        self.table_checkBox1 = QCheckBox('Marcar')
        self.table_checkBox1.setStyleSheet(css.table_checkBox)
        self.table_checkBox1.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(0, 1, self.table_checkBox1)

        self.table_checkBox2 = QCheckBox('Marcar')
        self.table_checkBox2.setStyleSheet(css.table_checkBox)
        self.table_checkBox2.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(1, 1, self.table_checkBox2)

        self.table_checkBox3 = QCheckBox('Marcar')
        self.table_checkBox3.setStyleSheet(css.table_checkBox)
        self.table_checkBox3.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(2, 1, self.table_checkBox3)

        self.table_checkBox4 = QCheckBox('Marcar')
        self.table_checkBox4.setStyleSheet(css.table_checkBox)
        self.table_checkBox4.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(3, 1, self.table_checkBox4)

        self.table_checkBox5 = QCheckBox('Marcar')
        self.table_checkBox5.setStyleSheet(css.table_checkBox)
        self.table_checkBox5.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(4, 1, self.table_checkBox5)

        self.table_checkBox6 = QCheckBox('Marcar')
        self.table_checkBox6.setStyleSheet(css.table_checkBox)
        self.table_checkBox6.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(5, 1, self.table_checkBox6)

        self.table_checkBox7 = QCheckBox('Marcar')
        self.table_checkBox7.setStyleSheet(css.table_checkBox)
        self.table_checkBox7.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(6, 1, self.table_checkBox7)

        self.table_checkBox8 = QCheckBox('Marcar')
        self.table_checkBox8.setStyleSheet(css.table_checkBox)
        self.table_checkBox8.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(7, 1, self.table_checkBox8)

        self.table_checkBox9 = QCheckBox('Marcar')
        self.table_checkBox9.setStyleSheet(css.table_checkBox)
        self.table_checkBox9.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(8, 1, self.table_checkBox9)

        self.table_checkBox10 = QCheckBox('Marcar')
        self.table_checkBox10.setStyleSheet(css.table_checkBox)
        self.table_checkBox10.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(9, 1, self.table_checkBox10)

        self.table_checkBox11 = QCheckBox('Marcar')
        self.table_checkBox11.setStyleSheet(css.table_checkBox)
        self.table_checkBox11.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(10, 1, self.table_checkBox11)

        self.table_checkBox12 = QCheckBox('Marcar')
        self.table_checkBox12.setStyleSheet(css.table_checkBox)
        self.table_checkBox12.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(11, 1, self.table_checkBox12)

        self.table_checkBox13 = QCheckBox('Marcar')
        self.table_checkBox13.setStyleSheet(css.table_checkBox)
        self.table_checkBox13.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(12, 1, self.table_checkBox13)

        self.table_checkBox14 = QCheckBox('Marcar')
        self.table_checkBox14.setStyleSheet(css.table_checkBox)
        self.table_checkBox14.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(13, 1, self.table_checkBox14)

        self.table_checkBox15 = QCheckBox('Marcar')
        self.table_checkBox15.setStyleSheet(css.table_checkBox)
        self.table_checkBox15.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(14, 1, self.table_checkBox15)

        self.table_checkBox16 = QCheckBox('Marcar')
        self.table_checkBox16.setStyleSheet(css.table_checkBox)
        self.table_checkBox16.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(15, 1, self.table_checkBox16)

        self.table_checkBox17 = QCheckBox('Marcar')
        self.table_checkBox17.setStyleSheet(css.table_checkBox)
        self.table_checkBox17.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(16, 1, self.table_checkBox17)

        self.table_checkBox18 = QCheckBox('Marcar')
        self.table_checkBox18.setStyleSheet(css.table_checkBox)
        self.table_checkBox18.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(17, 1, self.table_checkBox18)

        self.table_checkBox19 = QCheckBox('Marcar')
        self.table_checkBox19.setStyleSheet(css.table_checkBox)
        self.table_checkBox19.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(18, 1, self.table_checkBox19)

        self.table_checkBox20 = QCheckBox('Marcar')
        self.table_checkBox20.setStyleSheet(css.table_checkBox)
        self.table_checkBox20.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(19, 1, self.table_checkBox20)

        self.table_checkBox21 = QCheckBox('Marcar')
        self.table_checkBox21.setStyleSheet(css.table_checkBox)
        self.table_checkBox21.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(20, 1, self.table_checkBox21)

        self.table_checkBox22 = QCheckBox('Marcar')
        self.table_checkBox22.setStyleSheet(css.table_checkBox)
        self.table_checkBox22.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(21, 1, self.table_checkBox22)

        self.table_checkBox23 = QCheckBox('Marcar')
        self.table_checkBox23.setStyleSheet(css.table_checkBox)
        self.table_checkBox23.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(22, 1, self.table_checkBox23)

        self.table_checkBox24 = QCheckBox('Marcar')
        self.table_checkBox24.setStyleSheet(css.table_checkBox)
        self.table_checkBox24.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(23, 1, self.table_checkBox24)

        self.table_checkBox25 = QCheckBox('Marcar')
        self.table_checkBox25.setStyleSheet(css.table_checkBox)
        self.table_checkBox25.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(24, 1, self.table_checkBox25)

        self.table_checkBox26 = QCheckBox('Marcar')
        self.table_checkBox26.setStyleSheet(css.table_checkBox)
        self.table_checkBox26.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(25, 1, self.table_checkBox26)

        self.table_checkBox27 = QCheckBox('Marcar')
        self.table_checkBox27.setStyleSheet(css.table_checkBox)
        self.table_checkBox27.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(26, 1, self.table_checkBox27)

        self.table_checkBox28 = QCheckBox('Marcar')
        self.table_checkBox28.setStyleSheet(css.table_checkBox)
        self.table_checkBox28.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(27, 1, self.table_checkBox28)

        self.table_checkBox29 = QCheckBox('Marcar')
        self.table_checkBox29.setStyleSheet(css.table_checkBox)
        self.table_checkBox29.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(28, 1, self.table_checkBox29)

        self.table_checkBox30 = QCheckBox('Marcar')
        self.table_checkBox30.setStyleSheet(css.table_checkBox)
        self.table_checkBox30.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(29, 1, self.table_checkBox30)

        self.table_checkBox31 = QCheckBox('Marcar')
        self.table_checkBox31.setStyleSheet(css.table_checkBox)
        self.table_checkBox31.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(30, 1, self.table_checkBox31)

        self.table_checkBox32 = QCheckBox('Marcar')
        self.table_checkBox32.setStyleSheet(css.table_checkBox)
        self.table_checkBox32.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(31, 1, self.table_checkBox32)

        self.table_checkBox33 = QCheckBox('Marcar')
        self.table_checkBox33.setStyleSheet(css.table_checkBox)
        self.table_checkBox33.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(32, 1, self.table_checkBox33)

        self.table_checkBox34 = QCheckBox('Marcar')
        self.table_checkBox34.setStyleSheet(css.table_checkBox)
        self.table_checkBox34.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(33, 1, self.table_checkBox34)

        self.table_checkBox35 = QCheckBox('Marcar')
        self.table_checkBox35.setStyleSheet(css.table_checkBox)
        self.table_checkBox35.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(34, 1, self.table_checkBox35)

        self.table_checkBox36 = QCheckBox('Marcar')
        self.table_checkBox36.setStyleSheet(css.table_checkBox)
        self.table_checkBox36.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(35, 1, self.table_checkBox36)

        self.table_checkBox37 = QCheckBox('Marcar')
        self.table_checkBox37.setStyleSheet(css.table_checkBox)
        self.table_checkBox37.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(36, 1, self.table_checkBox37)

        self.table_checkBox38 = QCheckBox('Marcar')
        self.table_checkBox38.setStyleSheet(css.table_checkBox)
        self.table_checkBox38.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(37, 1, self.table_checkBox38)

        self.table_checkBox39 = QCheckBox('Marcar')
        self.table_checkBox39.setStyleSheet(css.table_checkBox)
        self.table_checkBox39.setCheckState(QtCore.Qt.Unchecked)
        self.table_questions.setCellWidget(38, 1, self.table_checkBox39)

        self.btn_ok = QPushButton(self)
        self.btn_ok.setText('GUARDAR')
        self.btn_ok.setGeometry(295, 575, 110, 50)
        self.btn_ok.setStyleSheet(css.btn_acept_cancel)
        self.btn_ok.clicked.connect(self.btn_ok_clicked)

    def btn_ok_clicked(self):
        self.points_test = 1
        self.bd = CastDB(self.dni, self.name, self.lastname, self.date, self.points_test)
        self.bd.addBD()
        self.close()


# if __name__=='__main__':
#    app = QtWidgets.QApplication(sys.argv)
#    mainWin = CastTest()
#    sys.exit( app.exec_())
