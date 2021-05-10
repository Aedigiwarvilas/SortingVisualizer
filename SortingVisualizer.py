# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sortingvisualizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 695)
        MainWindow.setStyleSheet("background:black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 881, 131))
        self.widget.setStyleSheet("background:silver")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lenslider = QtWidgets.QSlider(self.widget)
        self.lenslider.setGeometry(QtCore.QRect(20, 90, 101, 21))
        self.lenslider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lenslider.setMinimum(5)
        self.lenslider.setMaximum(20)
        self.lenslider.setOrientation(QtCore.Qt.Horizontal)
        self.lenslider.setObjectName("lenslider")
        self.minslider = QtWidgets.QSlider(self.widget)
        self.minslider.setGeometry(QtCore.QRect(160, 90, 91, 21))
        self.minslider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minslider.setMinimum(1)
        self.minslider.setMaximum(10)
        self.minslider.setOrientation(QtCore.Qt.Horizontal)
        self.minslider.setObjectName("minslider")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.maxslider = QtWidgets.QSlider(self.widget)
        self.maxslider.setGeometry(QtCore.QRect(290, 90, 91, 21))
        self.maxslider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maxslider.setMinimum(5)
        self.maxslider.setMaximum(30)
        self.maxslider.setOrientation(QtCore.Qt.Horizontal)
        self.maxslider.setObjectName("maxslider")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(300, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.algorithm = QtWidgets.QComboBox(self.widget)
        self.algorithm.setGeometry(QtCore.QRect(410, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.algorithm.setFont(font)
        self.algorithm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(440, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(590, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.speedslider = QtWidgets.QSlider(self.widget)
        self.speedslider.setGeometry(QtCore.QRect(570, 90, 101, 21))
        self.speedslider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.speedslider.setMaximum(6)
        self.speedslider.setPageStep(10)
        self.speedslider.setSliderPosition(3)
        self.speedslider.setOrientation(QtCore.Qt.Horizontal)
        self.speedslider.setObjectName("speedslider")
        self.generate = QtWidgets.QPushButton(self.widget)
        self.generate.setGeometry(QtCore.QRect(710, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generate.setFont(font)
        self.generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate.setStyleSheet("QPushButton\n"
"{\n"
" background:#e67300;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
" background: #cc6600;\n"
"}")
        self.generate.setObjectName("generate")
        self.start = QtWidgets.QPushButton(self.widget)
        self.start.setGeometry(QtCore.QRect(710, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setStyleSheet("QPushButton\n"
"{\n"
"  background:#00e639;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"  background: #00cc33;\n"
"}")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.widget)
        self.stop.setGeometry(QtCore.QRect(790, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stop.setFont(font)
        self.stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop.setStyleSheet("QPushButton\n"
"{\n"
" background:#e60000;\n"
"}\n"
".QPushButton::hover\n"
"{\n"
"  background:#cc0000;\n"
"}")
        self.stop.setObjectName("stop")
        self.lenval = QtWidgets.QLabel(self.widget)
        self.lenval.setGeometry(QtCore.QRect(60, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lenval.setFont(font)
        self.lenval.setObjectName("lenval")
        self.minval = QtWidgets.QLabel(self.widget)
        self.minval.setGeometry(QtCore.QRect(200, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minval.setFont(font)
        self.minval.setObjectName("minval")
        self.maxval = QtWidgets.QLabel(self.widget)
        self.maxval.setGeometry(QtCore.QRect(320, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maxval.setFont(font)
        self.maxval.setObjectName("maxval")
        self.speedval = QtWidgets.QLabel(self.widget)
        self.speedval.setGeometry(QtCore.QRect(600, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.speedval.setFont(font)
        self.speedval.setObjectName("speedval")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(20, 170, 881, 491))
        self.widget_2.setStyleSheet("background:silver")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 80, 861, 411))
        self.widget_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget_3.setStyleSheet("background:white")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(470, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tmcomp = QtWidgets.QLabel(self.widget_2)
        self.tmcomp.setGeometry(QtCore.QRect(270, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tmcomp.setFont(font)
        self.tmcomp.setStyleSheet("color:green")
        self.tmcomp.setObjectName("tmcomp")
        self.spcomp = QtWidgets.QLabel(self.widget_2)
        self.spcomp.setGeometry(QtCore.QRect(670, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spcomp.setFont(font)
        self.spcomp.setStyleSheet("color:green")
        self.spcomp.setObjectName("spcomp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Array Length"))
        self.label_4.setText(_translate("MainWindow", "Min Value"))
        self.label_5.setText(_translate("MainWindow", "Max Value"))
        self.algorithm.setPlaceholderText(_translate("MainWindow", "Select Algo"))
        self.algorithm.setItemText(0, _translate("MainWindow", "Bubble Sort"))
        self.algorithm.setItemText(1, _translate("MainWindow", "Insertion Sort"))
        self.algorithm.setItemText(2, _translate("MainWindow", "Selection Sort"))
        self.algorithm.setItemText(3, _translate("MainWindow", "Merge Sort"))
        self.algorithm.setItemText(4, _translate("MainWindow", "Quick Sort"))
        self.label_6.setText(_translate("MainWindow", "Algorithm"))
        self.label_7.setText(_translate("MainWindow", "Speed"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.lenval.setText(_translate("MainWindow", "5"))
        self.minval.setText(_translate("MainWindow", "1"))
        self.maxval.setText(_translate("MainWindow", "5"))
        self.speedval.setText(_translate("MainWindow", "1x"))
        self.label.setText(_translate("MainWindow", "Time Complexity  : "))
        self.label_2.setText(_translate("MainWindow", "Space Complexity  : "))
        self.tmcomp.setText(_translate("MainWindow", "O(n²)"))
        self.spcomp.setText(_translate("MainWindow", "O(n²)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
