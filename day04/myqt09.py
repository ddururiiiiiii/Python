import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

# 짝수의 합
form_class = uic.loadUiType("myqt09.ui")[0]

class windowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.btnClick) 
        
    def btnClick(self):
        def myClick("1"):
        
    def myClick(self):
        
        str_old = self.le1.text()
        
        self.le1.setText()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = windowClass()
    myWindow.show()
    sys.exit(app.exec_())
