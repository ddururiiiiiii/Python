import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

WindowUI = 'myqt01.ui'

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(WindowUI, self)
        self.pb.clicked.connect(self.btnClick) 
        
    def btnClick(self):
            self.lbl.setText("Good Evening")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
