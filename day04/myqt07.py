import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import random

# 가위 바위 보 게임
form_class = uic.loadUiType("myqt07.ui")[0]

class windowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick) 
        
    def btnClick(self):
        mine = self.le1.text()
        
        rnd = random.randrange(1,10)
        if rnd <= 3 :
            com = "가위"
        elif rnd <= 6 :
            com = "바위"
        else :
            com = "보" 
             
        self.le2.setText(com)

        if mine == "가위" and com =="가위" :
            result = "비김"
        elif mine == "가위" and com =="바위" :
            result = "짐"    
        elif mine == "가위" and com =="보" :
            result = "이김"
                
        elif mine == "바위" and com =="가위" :
            result = "이김"
        elif mine == "바위" and com =="바위" :
            result = "비김"    
        elif mine == "바위" and com =="보" :
            result = "짐"    
            
        elif mine == "보" and com =="가위" :
            result = "짐"
        elif mine == "보" and com =="바위" :
            result = "이김"    
        elif mine == "보" and com =="보" :
            result = "비김"    

        self.le3.setText(result)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = windowClass()
    myWindow.show()
    sys.exit(app.exec_())
