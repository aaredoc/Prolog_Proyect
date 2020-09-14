import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5 import QtGui
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os

class CastProgress(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_title = 'SOFT-CAST : PROGRESO'
        self.window_icon_PATH = 'windows_icon.png'
        self.window_top = 50
        self.window_left = 500
        self.window_width = 800
        self.window_height = 600
        self.setWindowIcon(QtGui.QIcon(self.window_icon_PATH))
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.window_left, self.window_top, self.window_width, self.window_height)
        self.initUI()
        self.show()

    def initUI(self):
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setTitle('GRAFICO DE PROGRESO')
        self.line_border = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.SolidLine)

        meses = [1, 2, 3]
        puntos = [20,13,10]

        # plot data: x, y values
        self.graphWidget.plot(meses, puntos, pen=self.line_border, symbol='o', symbolSize=20)
        self.graphWidget.setBackground('w')
        
    
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = CastProgress()
    sys.exit( app.exec_())
    