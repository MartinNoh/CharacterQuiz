# importing libraries
import sys, os, random

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Recreation Character Quiz")

        # setting geometry
        self.setGeometry(800, 100, 1448, 854)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # 변수 정리
        # counter
        self.count = 40

        # creating flag
        self.flag = False

        self.abspath = "C:/Users/ehdru/PycharmProjects/pythonProject7/media"
        self.image_path = os.path.join(self.abspath, 'ready.png')

        # 이미지 확인
        # creating a label to show the time
        self.label_img = QLabel(self)

        # setting geometry of label
        self.label_img.setGeometry(10, 10, 1141, 801)

        # adding border to the label
        self.label_img.setStyleSheet("border : 4px solid black;")

        # get image
        self.label_img.setPixmap(QtGui.QPixmap(self.image_path))
        self.label_img.setScaledContents(False)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setWordWrap(False)
        self.label_img.setObjectName("label_img")





        # 정답 확인
        # creating start button
        start = QPushButton("정답 확인", self)

        # setting geometry to the button
        start.setGeometry(1170, 30, 251, 51)

        # add action to the method
        start.pressed.connect(self.Check_answer)




        # 다음 문제
        # creating reset button
        re_set = QPushButton("다음 문제", self)

        # setting geometry to the button
        re_set.setGeometry(1170, 90, 251, 51)


        # 클릭 : 다음 사진 보기
        # add action to the method
        re_set.pressed.connect(self.show_next_img)




        # 일시 정지
        # creating pause button
        pause = QPushButton("일시정지/재시작", self)

        # setting geometry to the button
        pause.setGeometry(1170, 150, 251, 51)

        # add action to the method
        pause.pressed.connect(self.Pause)




        # 시간 초기화
        # creating pause button
        pause = QPushButton("시간 초기화", self)

        # setting geometry to the button
        pause.setGeometry(1170, 210, 251, 51)

        # add action to the method
        pause.pressed.connect(self.Re_set)




        # 시간 확인
        # creating a label to show the time
        self.label = QLabel(self)

        # setting geometry of label
        self.label.setGeometry(1170, 280, 251, 81)

        # adding border to the label
        self.label.setStyleSheet("border : 4px solid black;")

        # setting text to the label
        self.label.setText(str(self.count))

        # setting font to the label
        self.label.setFont(QFont('Arial', 25))

        # setting alignment to the text of label
        self.label.setAlignment(Qt.AlignCenter)




        # creating a timer object
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every tenth second
        timer.start(100)




    # 정답 보기 함수
    def Check_answer(self):
        filename_raw = os.path.basename(self.image_path)
        filename = filename_raw.split('.')[0]
        alert = QMessageBox()
        alert.setText(str(filename))
        alert.exec_()

    # 다음화면 보기 함수
    def show_next_img(self):
        img_files = os.listdir(self.abspath)
        random_number = random.randrange(0, len(img_files))
        self.image_path = os.path.join(self.abspath, img_files[random_number])

        self.label_img.setPixmap(QtGui.QPixmap(self.image_path))

        self.count = 40
        self.flag = True


    # method called by timer
    def showTime(self):
        # checking if flag is true
        if self.flag:
            # incrementing the counter
            self.count -= 1
        if self.count == 0:
            self.flag = False
            self.count = 40
            alert = QMessageBox()
            alert.setText('그만!')
            alert.exec_()

        # getting text from count
        text = str(int(self.count / 10))

        # showing text
        self.label.setText(text)


    def Start(self):
        # making flag to true
        self.flag = True


    def Pause(self):
        # making flag to False
        if self.flag:
            self.flag = False
        else:
            self.flag = True


    def Re_set(self):
        # making flag to false
        self.flag = False

        # reseeting the count
        self.count = 40

        # setting text to label
        self.label.setText(str(self.count))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())