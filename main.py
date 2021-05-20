from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow,QApplication,QGraphicsScene
from PyQt5.QtGui import QColor,QFont,QPen,QBrush
from random import sample,choices
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("main.ui",self)

        # Global Variables
        self.c_height = 421
        self.font=QFont()
        self.font.setPointSize(12)
        self.flag=False
        self.speed = {0: ["0.25x",1.8], 1: ["0.5x",1.4], 2: ["0.75x",1.2],3: ["1x",1], 4: ["1.25x",0.8], 5: ["1.5x",0.4], 6: ["1.75x",0.2]}
        self.colors = {"red":QColor(255,0,0),"green":QColor(0,255,0),"blue":QColor(0,0,255),"black":QColor(0,0,0)}
        self.sorts_desc = {"Bubble Sort":["O(n²)","O(1)"],"Insertion Sort":["O(n²)","O(1)"],"Selection Sort":["O(n²)","O(1)"],"Quick Sort":["O(n²)","O(nlogn)"],"Merge Sort":["O(nlogn)","O(n)"]}
        self.pen = QPen(self.colors["black"],3)
        self.generate.clicked.connect(self.generateArray)
        self.lenslider.valueChanged.connect(self.updatelength)
        self.minslider.valueChanged.connect(self.updatemin)
        self.maxslider.valueChanged.connect(self.updatemax)
        self.speedslider.valueChanged.connect(self.updatespeed)
        self.start.clicked.connect(self.startalgorithm)
        self.stop.clicked.connect(self.stopalgorithm)
        self.show()

    def updatelength(self):
        self.len = self.lenslider.value()
        self.lenval.setText(str(self.len))

    def updatemin(self):
        self.mn = self.minslider.value()
        self.minval.setText(str(self.mn))

    def updatemax(self):
        self.mx = self.maxslider.value()
        self.maxval.setText(str(self.mx))

    def updatespeed(self):
        self.sd = self.speedslider.value()
        self.speedval.setText(self.speed[self.sd][0])


    def generateArray(self):
        self.start.setDisabled(False)
        self.tmcomp.setText("")
        self.spcomp.setText("")
        self.comparisions.setText("")
        self.len = self.lenslider.value()
        self.mn = self.minslider.value()
        self.mx = self.maxslider.value()
        if (self.mx-self.mn+1) >= self.len:
            self.arr = sample(range(self.mn, self.mx+1), self.len)
        else:
            self.arr = choices(range(self.mn, self.mx+1), k=self.len)

        self.drawData(["red"]*(self.len))

    def drawData(self,color):
        self.scene = QGraphicsScene()
        self.c_width = 831 - 13*self.len
        x_width = self.c_width/(self.len+1)
        self.graphicsView.setScene(self.scene)
        maxele=max(self.arr)
        normalizedData=[i/maxele for i in self.arr]
        for i,height in enumerate(normalizedData):
            x0 = i*(x_width+13)
            y0 = self.c_height - height *370
            x1 = x_width
            y1 = self.c_height-y0
            self.brush = QBrush(self.colors[color[i]])
            self.scene.addRect(x0,y0,x1,y1,self.pen,self.brush)
            num=self.scene.addText(str(self.arr[i]))
            num.setPos(x0,y0-30)
            num.setFont(self.font)


    def stopalgorithm(self):
        if not self.start.isEnabled() and not self.generate.isEnabled():
            self.flag = True
        QApplication.processEvents()


    def startalgorithm(self):
        self.generate.setDisabled(True)
        self.start.setDisabled(True)
        self.selected_algo=self.algorithm.currentText()
        self.sd = self.speed[self.speedslider.value()][1]
        if self.selected_algo == "Bubble Sort":
            self.BubbleSort(self.sd)
        elif self.selected_algo == "Insertion Sort":
            pass
        elif self.selected_algo == "Selection Sort":
            pass
        elif self.selected_algo == "Merge Sort":
            pass
        elif self.selected_algo == "Quick Sort":
            pass
        else:
            pass
        self.flag=False
        self.generate.setDisabled(False)
        self.tmcomp.setText(self.sorts_desc[self.selected_algo][0])
        self.spcomp.setText(self.sorts_desc[self.selected_algo][1])


    def BubbleSort(self,speed):
        count=0
        for i in range(self.len-1):
            for j in range(self.len-1-i):
                if self.flag:
                    return
                self.drawData(["blue" if x==j or x==j+1 else "red" for x in range(self.len-i)]+["green"]*(i+1))
                QApplication.processEvents()
                sleep(speed)
                count+=1
                self.comparisions.setText(str(count))
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
                self.drawData(["red" for x in range(self.len-i)]+["green"]*(i+1))
                QApplication.processEvents()
                sleep(speed)
        self.drawData(["green"]*self.len)
        QApplication.processEvents()
        sleep(speed)











    def InsertionSort():
        pass
    def SelectionSort():
        pass
    def MergeSort():
        pass
    def QuickSort():
        pass







if __name__ == "__main__":
    app = QApplication([])
    mainwindow = MainWindow()
    app.exec()
