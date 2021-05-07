import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt05.ui")[0]

class windowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick) 
        
    def btnClick(self):
        mine = self.le1.text()
        
        rnd = random.randrange(1,10)
        if rnd <= 5 :
            com = "홀"
        else :
            com = "짝"  
        self.le2.setText(com)

        if mine == "홀" and com =="홀" :
            result = "일치"
        elif mine == "홀" and com =="짝" :
            result = "불일치"    
            
        elif mine == "짝" and com =="짝" :
            result = "일치"    
        elif mine == "짝" and com =="홀" :
            result = "불일치"    
            
        self.le3.setText(result)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = windowClass()
    myWindow.show()
    sys.exit(app.exec_())
