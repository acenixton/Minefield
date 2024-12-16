# 02.12.2024, 03.12.2024, 16.12.2024
# multiple buttons, every game the position of the "bomb" is randomized
# Players take turns pressing buttons, whoever finds the bomb looses
# (like those crocodile teeth games. or just russian roulette)


from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys
from random import *
from math import *

GLOBAL_STYLE = """QPushButton[checkable="true"] {color: grey; background-color: white; font: bold 14px}
                    QLabel {font: 20px}
                    QPushButton {font: 16px}
                    QLineEdit {background: green}"""

class Minefield(QWidget):
    # attributes of this class
    # self.lay
    # self.bombdex
    # self.buttons
    
    def no_bomb(self):
        bu = self.sender()
        bu.setEnabled(False)
        bu.setText("")
<<<<<<< Updated upstream
           
    def bomb(self):
        bu = self.sender()
        bu.setEnabled(False)
        self.win2 = Explosion()
        self.win2.show()
      
    
    def __init__(self,butts):
=======
        self.counter += 1

    # opens explosion dialogue if bomb is triggered
    def bomb(self):
        bu = self.sender()
        bu.setEnabled(False)
        self.boom = ExplosionDialog(parent=self)
        self.boom.exec()
    
    def __init__(self, size):
>>>>>>> Stashed changes
        super().__init__()
        self.setWindowTitle("Find the mine!")
        self.setWindowIcon(QIcon('bombicon.png'))
        self.counter = 1
        self.lay = QGridLayout(self)
        self.buttons = []
        self.lay.setContentsMargins(60,60,60,60)
        self.lay.setSpacing(15)
        self.set_bombdex(size)
        self.set_buttongrid(size)
        
    def set_bombdex(self, butts):
        self.bombdex = randint(0,butts-1)
<<<<<<< Updated upstream
        self.labl = QLabel(" ")
        
=======
        
    # arranges the buttons into grid
    def set_buttongrid(self,butts):
>>>>>>> Stashed changes
        # adds specified amount of buttons
        for i in range(0,butts):
            self.buttons.append(QPushButton(f"o"))
            self.buttons[i].setCheckable(True)
            self.buttons[i].setFixedSize(50,50)
            
            # sets bomb
            if i == self.bombdex:
                self.buttons[i].toggled.connect(self.bomb)
            else:
<<<<<<< Updated upstream
                self.buttons[i].toggled.connect(self.testpress)    
        self.buttongrid()
  
    # arranges the buttons into grid
    def buttongrid(self):
=======
                self.buttons[i].toggled.connect(self.no_bomb)  
                
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
class Explosion(QMainWindow):
    def __init__(self):
        super().__init__()
        # layout = QGridLayout(self)
        boom = QLabel(self)
        boom.setPixmap(QPixmap('explosion.png'))
        boom.setScaledContents(True)
        # layout.addWidget(boom)
        # self.setContentsMargins(10,10,10,10)
        self.setFixedSize(400,400)
        self.setCentralWidget(boom)
       
        

# main stuff   
grid = 9
            
app = QApplication(sys.argv)
win = Minefield(grid)
win.show()
app.setStyleSheet(GLOBAL_STYLE)
sys.exit(app.exec())

            
=======
class ExplosionDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("BOOM!")
        self.setWindowIcon(QIcon('explosion.png'))
        # adds buttons from standard selection, Qt handles order
        buttons = QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No
        self.buttonBox = QDialogButtonBox(buttons)
        # connecting buttons to custom functions
        self.buttonBox.rejected.connect(self.stop)
        self.buttonBox.accepted.connect(self.play_again)

        layout = QVBoxLayout()
        message = QLabel(f"You found the bomb in {parent.counter} tries!\nWant to try again?")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def play_again(self):
        # creates new game window with same amount as before
        games.append(Minefield(len(games[-1].buttons)))
        games[-1].show()
        # closes old window and dialogue
        games[-2].close()
        self.close()

    def stop(self):
        # returns to main menu
        games[-1].close()
        self.close()

class Startmenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to the minefield!")
        self.setWindowIcon(QIcon('bombicon.png'))
        self.setFixedSize(350,350)
        text = QLabel(parent=self,text="Choose how big the field should be.")
        self.layouts = QVBoxLayout(self)
        self.layouts.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_options()
        
    def add_options(self):
        # adds buttons for different game grids
        button3 = QPushButton(text="3 x 3")
        self.layouts.addWidget(button3)
        button3.clicked.connect(lambda: self.start_game(9))
        button4 = QPushButton(text="4 x 4")
        self.layouts.addWidget(button4)
        button4.clicked.connect(lambda: self.start_game(16))
        button5 = QPushButton(text="5 x 5")
        self.layouts.addWidget(button5)
        button5.clicked.connect(lambda: self.start_game(25))
        button6 = QPushButton(text="6 x 6")
        self.layouts.addWidget(button6)
        button6.clicked.connect(lambda: self.start_game(36))
        button9 = QPushButton(text="9 x 9")
        self.layouts.addWidget(button9)
        button9.clicked.connect(lambda: self.start_game(81))
        
        # custom button
        rowlayout = QHBoxLayout()
        bu_custom = QPushButton(text="Use custom option")
        self.cusize = QLineEdit()
        self.cusize.setInputMask("90")
        self.cusize.setMaximumWidth(60)
        bu_custom.clicked.connect(self.custom_game) 
        rowlayout.addWidget(QLabel("Or enter amount of buttons:"))
        rowlayout.addWidget(self.cusize, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layouts.addLayout(rowlayout)
        self.layouts.addWidget(bu_custom)
        
        # add quit button
        bu_quit = QPushButton(parent=self, text=f"Quit")
        self.layouts.addWidget(bu_quit)
        bu_quit.clicked.connect(sys.exit)
        
    def custom_game(self):
        if self.cusize.hasAcceptableInput():
            self.start_game(int(self.cusize.text()))
            
    def start_game(self,size):
        games.append(Minefield(size))
        games[-1].show()
    
# main stuff 
games = []
app = QApplication(sys.argv)
app.setStyleSheet(GLOBAL_STYLE)
win = Startmenu()
win.show()
sys.exit(app.exec())
>>>>>>> Stashed changes
