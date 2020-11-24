import sys
from random import choice
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.flag = False

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Жёлтые окружности')
        pb = QPushButton('Кнопка', self)
        pb.resize(90, 30)
        pb.move(10, 10)
        pb.clicked.connect(self.drawf)

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
        self.qp.setBrush(QColor(choice(range(256)), choice(range(256)), choice(range(256))))
        coord = choice(range(5, 100))
        self.qp.drawEllipse(choice(range(500)), choice(range(40, 400)), coord, coord)


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
