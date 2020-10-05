'''
Created on Nov 8, 2019

@author: Alyona
'''
import sys
from PyQt5 import QtGui, QtWidgets
#from matplotlib.backends.qt_compat import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    b1 = QtWidgets.QPushButton(w)
    
    l1.setText("Cat or Dog")
    l2.setPixmap(QtGui.QPixmap("catdog.png"))
    b1.setText(("Push me!"))

    w.setWindowTitle("Cat-Dog")
    w.setGeometry(100,100,300,200)
    l1.move(110,20)
    l2.move(10,40)
    b1.move(90,60)
    w.show()
    sys.exit(app.exec_())
    
window()

app = QApplication([])
button = QPushButton('Click')


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()