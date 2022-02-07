from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random

class Ui_MainWindow(QtWidgets.QMainWindow):
    def main(self):
        self.dnum = 6 # Dice
        self.dice = 6 # Dx
        global rolls
        self.rolls = []
        self.getRolls(self.dice, self.dnum)


        self.setupUi(self, self.dice, self.dnum)
#        self.pushButton.clicked.connect(lambda: self.getRolls(self.dice, self.dnum))
        self.pushButton.clicked.connect(lambda: self.pConnect(self.dice, self.dnum))
        total = 0
        for nroll in self.rolls:
            total = int(total)+int(nroll)
        self.label.setText(str((" ".join(list(self.rolls))) + f"\n :{total}:"))


    def pConnect(self, dice, dnum):
        dnum = self.spinBox_2.value() # Dice
        dice = self.spinBox.value() # Dx
        rolls = self.getRolls(dice, dnum)
        total = 0
        for nroll in rolls:
            total = int(total)+int(nroll)
        self.label.setText(str((" ".join(list(rolls))) + f"\n :{total}:"))

    def getRolls(self, dice, dnum):
        rolls = []
        for i in range(0,dnum, +1):
            roll = random.randint(1,dice)
            rolls.append(str(roll))
        self.rolls = rolls
        return(rolls)

    def setupUi(self, MainWindow, dice, dnum):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 685)
        MainWindow.setMinimumSize(QtCore.QSize(689, 511))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setProperty("value", dice)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox.setFont(font)
        self.spinBox.setProperty("value", dnum)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout.addWidget(self.widget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1 2 3 4 5 6 "))
        self.pushButton.setText(_translate("MainWindow", "Random"))

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.main()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Ui_MainWindow()
    form.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
