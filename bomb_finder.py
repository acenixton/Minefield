# 02.12.2024, 03.12.2024
# multiple buttons, every game the position of the "bomb" is randomized
# Players take turns pressing buttons, whoever finds the bomb looses
# (like those crocodile teeth games. or just russian roulette)


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt6.QtCore import Qt
import sys
from random import *
from math import *
from time import sleep

GLOBAL_STYLE = """QPushButton[checkable="true"] {color: grey; background-color: white; font: bold 14px}"""

class Minefield(QWidget):
    def testpress(self):
        bu = self.sender()
        bu.setEnabled(False)
        bu.setText("")
           
    def bomb(self):
        bu = self.sender()
        print(bu)
        bu.setEnabled(False)
        bu.setText("Boom")
        bu.setStyleSheet("color:red")
        self.labl.setText("Boom")
        
        self.ende()
        
    def ende(self,tic=.2):
        sleep(tic)
        self.close()
    
    def __init__(self,butts):
        super().__init__()
        self.lay = QGridLayout(self)
        self.buttons = []
        self.lay.setContentsMargins(60,60,60,60)
        self.lay.setSpacing(15)
        self.bombdex = randint(0,butts-1)
        self.labl = QLabel(" ")
        
        # adds specified amount of buttons
        for i in range(0,butts):
            self.buttons.append(QPushButton(f"O"))
            self.buttons[i].setCheckable(True)
            self.buttons[i].setFixedSize(50,50)
            
            # sets bomb
            if i == self.bombdex:
                self.buttons[i].toggled.connect(self.bomb)
                self.buttons[i].setStyleSheet("background-color:red")
            else:
                self.buttons[i].toggled.connect(self.testpress)    
        self.buttongrid()
  
    # arranges the buttons into grid
    def buttongrid(self):
        # figures out how best to arrange the grid
        row = 0
        stop = len(self.buttons)+1
        while row*row <= stop:
            if row*row == len(self.buttons):
                break
            else:
                row += 1
        col = ceil(len(self.buttons)/row)
        
        # adds buttons to grid at the correct position
        k = 0
        for i in range(0,row):
            for j in range(0,col):
                self.lay.addWidget(self.buttons[k],i,j)
                k += 1
                
        lbrow = row + 1
        lbcol = int(col/2)
        self.lay.addWidget(self.labl,lbrow,lbcol)       
        self.labl.setAlignment(Qt.AlignmentFlag.AlignHCenter)

class Explosion(QWidget):
    def __init__(self):
        super().__init__()
        boom = QLabel(self)
        

# main stuff   
grid = 9
            
app = QApplication(sys.argv)
win = Minefield(grid)
win.show()
app.setStyleSheet(GLOBAL_STYLE)
sys.exit(app.exec())

            