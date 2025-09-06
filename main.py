import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Watch")
        self.setWindowIcon(QIcon("./logo.jpg"))
        self.setGeometry(500, 320, 600, 200)
        # First we will create a time object
        self.time = QTime(0, 0, 0, 0) # 0 Hours, 0 minutes, 0 Seconds, 0 Milliseconds
        self.time_label = QLabel("00:00:00:00", self)
        # Let's create buttons
        self.start_btn = QPushButton("START", self)
        self.stop_btn = QPushButton("STOP", self)
        self.reset_btn = QPushButton("RESET", self)

        self.timer = QTimer()
        # UI
        self.initUI()

    def initUI(self):
        # Give each btn an object name
        self.start_btn.setObjectName("start_btn")
        self.stop_btn.setObjectName("stop_btn")
        self.reset_btn.setObjectName("reset_btn")
        # Setting the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.stop_btn)
        vbox.addWidget(self.reset_btn)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)
        # Let's group the buttons horizontally
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.stop_btn)
        hbox.addWidget(self.reset_btn)

        vbox.addLayout(hbox)
        # CSS
        self.setStyleSheet("""
           QWidget{
              background-color: #a8f2f7;
           }
           QLabel{
              font-size: 70px;
              font-family: calibri;
              font-weight: bold;
              background-color: #6bdcf2;
              border-radius: 10px;
           }
           QPushButton#start_btn{
              background-color: #3df25e;
              font-family: sans-serif;
              font-size: 30px;
              font-weight: bold;
              border: none;
              border-radius: 5px;
           }
           QPushButton#stop_btn{
              background-color: #fc213a;
              font-family: sans-serif;
              font-size: 30px;
              font-weight: bold;
              border: none;
              border-radius: 5px;
           }
           QPushButton#reset_btn{
              background-color: #fcf921;
              font-family: sans-serif;
              font-size: 30px;
              font-weight: bold;
              border: none;
              border-radius: 5px;
           }
           QPushButton#start_btn:hover{
              border: 2px solid black;
           }
           QPushButton#stop_btn:hover{
             border: 2px solid black; 
           }
           QPushButton#reset_btn:hover{
             border: 2px solid black; 
           }
        """)
        # Now let's connect each button with its function
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10) # Interval of timeout every 10 milliseconds

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00:00")

    def time_format(self, time):
        hours = time.hour()
        minutes = time.minute()
        sec = time.second()
        msec = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{sec:02}:{msec:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10) # Adding 10 milliseconds as a time update
        self.time_label.setText(self.time_format(self.time))

def main():
    app = QApplication(sys.argv)
    window =  MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()