from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import ScreenShotQuestionNo as SSQN
import re

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quizzame Extender")

        self.setGeometry(100, 100, 1000, 800)

        #self.setStyleSheet('background-color: green;')

        self.UiComponents()

        self.show()

    def UiComponents(self):

        self.combo_box = QComboBox(self)

        myList = ['Buzzer 1', 'Buzzer 2', 'Buzzer 3']

        self.combo_box.addItems(myList)

        self.button1 = QPushButton("Show choice", self)

        self.button1.setGeometry(100, 100, 100, 100)

        #self.button1.pressed.connect(self.findBuzzer)

        self.combo_box.setGeometry(200, 150, 120, 30)

        self.label = QLabel(self)

        self.label.setGeometry(200, 200, 200, 30)

        self.multiplierInput = QLineEdit(self)

        self.multiplierInput.setGeometry(300, 300, 120, 30)

        self.labelMultiplier = QLabel(self)

        self.labelMultiplier.setText("Enter multiplier e.g. 0.9")

        self.labelMultiplier.setGeometry(300, 270, 130, 30)

        self.button2 = QPushButton("Confirm multiplier", self)

        self.button2.setGeometry(300, 400, 150, 30)

        #self.button2.pressed.connect(self.findMultiplier)

        self.label2 = QLabel(self)

        self.label2.setGeometry(400, 200, 200, 30)

        self.button3 = QPushButton("Press to begin", self)

        self.button3.setGeometry(300, 400, 100, 100)

        self.button3.pressed.connect(self.execute)


    def execute(self):

        buzzerChoice = self.combo_box.currentText()
        self.label.setText("Buzzer: " + buzzerChoice)
        buzzerChoice = re.search('\d{1,2}', buzzerChoice).group()
        print("buzzerchoice is: " + buzzerChoice)
        
        multiplierChoice = self.multiplierInput.text()
        self.label2.setText(multiplierChoice)
        print("Multiplier is: " + multiplierChoice)
        
        SSQN.runModifierifQ5(buzzerChoice, multiplierChoice)

App = QApplication(sys.argv)
    
window = Window()

sys.exit(App.exec())

    



