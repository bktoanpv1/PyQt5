from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Learn_QComboBox(QMainWindow):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #Set Wimdow Tittle
        self.setWindowTitle("QComboBox")

        #Create QcomboBox instance with label
        combobox = QComboBox()
        #Add item to QComboBox
        combobox.addItems(["Option 1","Option 2","Option 3"])
        #Add slot for signal "index changed"
        combobox.currentIndexChanged.connect(self.idxChanged_callback)
        #Add slot for signal "text changed"
        combobox.currentTextChanged.connect(self.textChanged_callback)

        #Set centralWidget
        self.setCentralWidget(combobox)
    
    #define idxChanged_callback()
    def idxChanged_callback(self,state):
        print(state)
    #define textChanged_callback()
    def textChanged_callback(self,state):
        print(state)

app = QApplication(sys.argv)
window = Learn_QComboBox()
window.show()
app.exec()