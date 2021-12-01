from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Learn_QSlider(QMainWindow):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #Set Wimdow Tittle
        self.setWindowTitle("QSlider")

        layout = QVBoxLayout()
        label = QLabel("ADC value")
        # font = label.font()
        # font.setPointSize(20)
        # # font.setFont(font)
        # font.setAlignment(Qt.AlignCenter)
        #Create QSlider instance with Qt.Horizontal or Qt.Vertical
        qslider = QSlider(Qt.Horizontal)
        #Set max/min value
        qslider.setMaximum(1023)
        qslider.setMinimum(0)

        #Setup increasing/decreasing step
        qslider.setSingleStep(5)
        #Setup distance step
        qslider.setTickInterval(10)
        #Setup position
        qslider.setTickPosition(QSlider.TicksBelow)
        #callback func
        qslider.valueChanged.connect(lambda t: print(t))

        layout.addWidget(label)
        layout.addWidget(qslider)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = Learn_QSlider()
window.show()
app.exec()