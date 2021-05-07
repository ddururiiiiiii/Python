import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

# 짝수의 합
form_class = uic.loadUiType("myqt08.ui")[0]

class windowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick) 
        
    def btnClick(self):
        dan = int(self.le1.text())
        
        result =""
        for i in range(1, 9) :
            result += dan + "X" + i + "=" + (dan * i) + "\n"     
        self.le3.setText(result)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = windowClass()
    myWindow.show()
    sys.exit(app.exec_())
