import sys
from random import choice
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.drawf)
        self.flag = False

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(255, 255, 0))
        coord = choice(range(5, 100))
        self.qp.drawEllipse(choice(range(510)), choice(range(40, 390)), coord, coord)


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
