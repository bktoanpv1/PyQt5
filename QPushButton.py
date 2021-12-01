from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Learn_QPush_Button(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("QPushButton")
        #Tạo QPushButton instance với text "Click me!"
        button = QPushButton("Click me!")
        #Kết nối signal clicked và slot
        button.clicked.connect(self.callback)
        #Cho phép tính năng toggleable của button
        button.setCheckable(True)

        self.setCentralWidget(button)

    def callback(self):
        print("Clicked!")
app = QApplication(sys.argv)
window = Learn_QPush_Button()
window.show()
app.exec()