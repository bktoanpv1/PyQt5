from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Learn_QMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle("QLabel")

        label = QLabel("This is QLabel")
        #Lấy font hiện tại và đổi font size
        font = label.font()
        font.setPointSize(20)
        #Cài đặt font chữ cho QLabel instance
        label.setFont(font)
        #Điều chỉnh căn lề dòng chữ
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        #Hiển thị label hình ảnh
        #Tạo Qlabel instance
        img_label = QLabel()
        #Load ảnh từ file icon.png vào Qlabel
        img_label.setPixmap(QPixmap("icon.png"))
        #Cho phép thay đổi tỷ lệ  bức ảnh bằng cách thay đổi tywr lệ cửa sổ
        img_label.setScaledContents(True)
        img_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(img_label)

app = QApplication(sys.argv)
window = Learn_QMainWindow()
window.show()
app.exec()