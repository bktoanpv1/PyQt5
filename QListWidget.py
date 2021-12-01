from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Learn_QListWidget(QMainWindow):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #Set Wimdow Tittle
        self.setWindowTitle("QListWidget")

        #Create QListWdget instance with label
        listwidget = QListWidget()
        #Add item to listwidget
        listwidget.addItems(["Option 1","Option 2","Option 3"])
        #Add slot for signal "Double Clicked"
        listwidget.doubleClicked.connect(self.dbClicked_callback)

        #Set centralWidget
        self.setCentralWidget(listwidget)
    
    #define dbClicked_callback()
    def dbClicked_callback(self,item):
        item.setText("Double Clicked!")

app = QApplication(sys.argv)
window = Learn_QListWidget()
window.show()
app.exec()