import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

# 짝수의 합
form_class = uic.loadUiType("myqt06.ui")[0]

class windowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick) 
        
    def btnClick(self):
        a = self.le1.text()
        b = self.le2.text()
        
        print(a)
        print(b)
        
        sum = 0
        for i in range(a, b+1) :
            if  i % 2 == 0 :
                sum += i
        print(sum)      
        self.le3.setText(str(sum))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = windowClass()
    myWindow.show()
    sys.exit(app.exec_())
