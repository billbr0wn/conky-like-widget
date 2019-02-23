#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QEvent
import psutil


#-------------------------------------------------
    
__author__ = '__Bill__'



class _Window_(QMainWindow):
    """
    -------------------(_Progress Bar_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)


        self.setMouseTracking(True)
        self.grabMouse()
        #self.QCursor.pos()
        
        self.cpu_percentage = psutil.cpu_percent(interval=0.05)
        self.cpu_cores = psutil.cpu_percent(interval=0.05, percpu=True)
        self.mem_2 = psutil.virtual_memory()[2]
        self.memory = psutil.virtual_memory()[5]
        self.memory_percent = self.memory / 800000000
        print('self.mem_2', self.mem_2)
        print('memory ', self.memory)
        print('memory_percent ', self.memory_percent)
        print()
        print('self.cpu_percentage ', self.cpu_percentage)
        self.disk = psutil.disk_usage('/')[3]
        self.freq = psutil.cpu_freq(percpu=False)[0]/1000*10
        self.cpu_freq = self.freq / 3.2 * 10
        
        
        self.total_physical_memory = 8259145728
        self.percent_mem = 100 / 8.26
        print('percent_mem ', self.percent_mem)
        self.percentage_of_used_memory = self.memory * self.percent_mem
        
        print()
        print('self.percentage_of_used_memory ', self.percentage_of_used_memory / 1000000000)

        
        print(self.cpu_percentage)
        print(self.cpu_cores[0])
        print(self.cpu_cores[1])
        print(psutil.virtual_memory()[2])
        print(psutil.disk_usage('/')[3])
        print(self.cpu_freq)


        

        self.red = (255, 0, 0)
        self.orange = (255, 128, 0, 0)
        self.yellow = (255, 255, 0, 20)
        self.green = (2, 75, 15, 70)
        self.violet = (126, 104, 255, 10)
        self.hex_green = ('#024913')
        self.blue = (100, 149, 237, 99)


        self.radius = """QProgressBar{
                            border: 2px solid grey;
                            border-radius: 5px;
                            text-align: center;
                            chunk {background: rgba(0, 0, 255, 60);
                        }"""


        self.DEFAULT_STYLE =  """QProgressBar::chunk {background-color: #ff0000; }"""

        self.new_style = """QProgressBar {
                              border: 1px solid grey;
                              border-radius: 10px;
                              text-align: center;
                              background-color: #00000000;
                              chunk: rgba(100, 149, 237, 50);
                              }
                              """



        self.chunk = """QProgressBar:vertical
                        {
                        border: 0px solid gray;
                        border-radius: 10px;
                        background: #00000000;
                        padding: 1px;
                        }
                        QProgressBar::chunk:vertical {
                        background: qlineargradient(x1: 1, y1: 1, x2: 1,
                        y2: 0, stop: 0 yellow, stop: 1 orange, stop: 2 red);
                       
                        }"""


        self.chunk_vertical = """QProgressBar:vertical
                        {
                        border: 0px solid gray;
                        border-radius: 10px;
                        background: #00000000;
                        padding: 1px;
                        }
                        QProgressBar::chunk:vertical {
                        background: qlineargradient(x1: 1, y1: 1, x2: 1,
                        y2: 0, stop: 0 rgba(2, 75, 15, 80), stop: 1 rgba(255, 128, 0, 25), stop: 2 purple);
                       
                        }"""


        self.chunk_horizontal_1 = """QProgressBar:horizontal
                                {
                                    border: 0px solid gray;
                                    border-radius: 3px;
                                    background: #00000000;
                                    padding: 1px;
                                }
                                    QProgressBar::chunk:horizontal
                                {
                                    background: qlineargradient(x1: 0, y1: 1, x2: 1, y2: 1,
                                    stop: 0 rgba(55, 128, 100, 85),
                                    stop: 1 rgba(255, 28, 0, 85));
                                }"""




        self.chunk_horizontal_2 = """QProgressBar:horizontal
                                {
                                    border: 0px solid gray;
                                    border-radius: 3px;
                                    background: #00000000;
                                    padding: 1px;
                                }
                                    QProgressBar::chunk:horizontal
                                {
                                    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5,
                                    stop: 0 rgba(55, 18, 180, 85),
                                    stop: 1 rgba(239, 231, 115, 85));
                                }"""


        self.chunk_horizontal_3 = """QProgressBar:horizontal
                                {
                                    border: 0px solid gray;
                                    border-radius: 10px;
                                    background: #00000000;
                                    padding: 0px;
                                }
                                    QProgressBar::chunk:horizontal
                                {
                                    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5,
                                    stop: 0 rgba(5, 118, 50, 85),
                                    stop: 1 rgba(25, 188, 190, 85));
                                }"""


        # mess with border-radius, thatDarklordGuy!
        self.sheet = ( """
                                color: rgba(237,174,28,70%);
                                background-color: rgba(0,0,0,100%);
                                text-align: center;
                                border-radius: 150px;
                                border: 1px solid rgba(237,174,28,70%);
                                padding: 0px;
                                """)
                        

        self.violet = """QProgressBar::chunk {background: rgba(0, 0, 255, 60);}"""
        self.cornflower_blue = """QProgressBar::chunk {background: rgba(100, 149, 237, 50);}"""
                           

        self.move_bar_1 = 0
        self.move_bar_2 = 0
        self.move_bar_3 = 0

        self.timer  = QTimer()
        self.timer.timeout.connect(self.update_bar__)
        self.timer.start(100)
        
        self.progress_bar__()
        self.initGUI()
        


    def progress_bar__(self):

        

##
        _label = QLabel  (self)
        self._label = _label 
        _label.setText   ('bar_1')
        _label.setGeometry(140,0, 150,105)


       
        progress_1_0 = QProgressBar(self)
        self.progress_1_0 = progress_1_0
        progress_1_0.setRange(0,100)    
        progress_1_0.setStyleSheet(self.chunk_horizontal_1)
        progress_1_0.setOrientation(Qt.Horizontal)
        progress_1_0.move(4,-5)
        progress_1_0.resize(120,15)

        progress_1_1 = QProgressBar(self)
        self.progress_1_1 = progress_1_1
        progress_1_1.setRange(0,100)    
        progress_1_1.setStyleSheet(self.chunk_horizontal_1)
        progress_1_1.setOrientation(Qt.Horizontal)
        progress_1_1.move(4,10)
        progress_1_1.resize(120,12)


        

        progress_2 = QProgressBar(self)
        self.progress_2 = progress_2
        progress_2.setRange(0,100)
        progress_2.setOrientation(Qt.Horizontal)
        progress_2.setStyleSheet(self.chunk_horizontal_2)
        progress_2.move(123,-7)
        progress_2.resize(120,20)




        progress_3 = QProgressBar(self)
        self.progress_3 = progress_3
        progress_3.setRange(0,100)
        progress_3.setOrientation(Qt.Horizontal)
        progress_3.setStyleSheet(self.chunk_horizontal_3)
        #progress_3.hide()
        progress_3.move(241,-7)
        progress_3.resize(120,20)

        


    def update_bar__(self):
        
                                 
        for proc in psutil.process_iter():
            pass        
        
        self.cpu_percentage = psutil.cpu_percent(interval=0.25)
        self.cpu_cores = psutil.cpu_percent(interval=0.25, percpu=True)
        self.memory = psutil.virtual_memory()[2]
        self.disk = psutil.disk_usage('/')[3]
        self.freq = psutil.cpu_freq(percpu=False)[0]/1000*10
        self.cpu_freq = self.freq / 3.2 * 10
        print(self.cpu_freq)


              

        self.progress_1_0.raise_()
        self.progress_1_1.raise_()
        
        self.setStyleSheet('font-size: 1pt; font-family: Cronyx;')

        if self.cpu_cores[0] <= (1):
            self.cpu_cores[0] += 1
        if self.cpu_cores[1] <= (1):
            self.cpu_cores[1] += 1
        
        self.progress_1_0.setValue(self.cpu_cores[0])
        self.progress_1_1.setValue(self.cpu_cores[1])
        self.new_mem = self.percentage_of_used_memory/1000000000
        self.progress_2.setValue(self.new_mem)
        self.progress_3.setValue(self.cpu_freq)

        self.raise_()
        





    def mousePressEvent(self, event):
        self.oPos = event.globalPos()
        
        if event.buttons() == Qt.NoButton:
            self.raise_()
##        elif event.buttons() == Qt.LeftButton:
##            self.raise_()
##        elif event.buttons() == Qt.RightButton:
##            self.raise_()
##        print('pressevent')
        
        elif event.buttons() == (Qt.RightButton): 
            #quit()
            print('mouse')
        else:
            pass





    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls
                | Qt.WindowStaysOnTopHint # forces window to top... maybe
                #| Qt.SplashScreen # this one hides it from the task bar!
                | Qt.WindowStaysOnTopHint
                | Qt.Tool)
        
       
        self.setAttribute(Qt.WA_TranslucentBackground, True)
                        #position  #size
        self.setGeometry(1350,0, 365,25)
        self.setWindowTitle('Conky Like Widget')
        self.setVisible(False)
        self.exitOnClose = False


        self.show()





        

if __name__ == '__main__':
    app = QApplication([])
    _Win_ = _Window_()
    app.exec_()
