import PySide.QtGui as QtGui
from serialSys import *
from colorSys import *

class LightChaser(QtGui.QWidget):
   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.__mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.__mainLayout)

        self.__setupSerialSys()
        self.__setupColorSys()
        self.__setupEffectSys()

    def __setupSerialSys(self):
        # Call Serial MVC
        serialView = SerialView()
        self.__serialController = SerialController(serialView)
        self.__mainLayout.addWidget(serialView)
        
         
    def __setupColorSys(self):
        self.__targetStat = ColorView("Target", self)
        self.__currentStat = ColorView("Current", self)

        self.__mainLayout.addWidget(self.__targetStat)
        self.__mainLayout.addWidget(self.__currentStat)


    def __setupEffectSys(self):
        pass


        
