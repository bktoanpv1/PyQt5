from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Learn_QCheckBox(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("QCheckBox")

        #Tạo QGroupBox instance để chứa các QRadioButton
        groupbox = QGroupBox("Option")
        layout = QVBoxLayout()
        for i in range(3):
            #Tạo QRadioButton instance với text Option #
            opt = QCheckBox(f"Option {i}")
            #Kết nối signal clicked và slot
            opt.pressed.connect(lambda x=i: print(f"option {x} is chosen"))
            #Thêm QRadioButton instance vào layout
            layout.addWidget(opt)
        #Cài đặt layout cho QGroupBox instance
        groupbox.setLayout(layout)
        self.setCentralWidget(groupbox)

    def callback(self):
        print("Clicked!")

app = QApplication(sys.argv)
window = Learn_QCheckBox()
window.show()
app.exec()