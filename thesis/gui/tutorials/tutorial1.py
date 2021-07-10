from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 200
ypos = 200
width = 300
heigth = 300


def fuction1():
    print("its clicking")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(xpos, ypos, width, heigth) # 0 , 0 top left 
    win.setWindowTitle("tutorial_1")

    label = QtWidgets.QLabel(win)
    label.setText("My big dick")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("have sex with me")
    b1.clicked.connect(fuction1)
    b1.move(100,100)

    win.show()
    sys.exit(app.exec_())

window()


