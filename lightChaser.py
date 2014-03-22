import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

from serialSys import *
from colorSys import *
from effectSys import *

from mediator import *

class LightChaser(QtGui.QWidget):
   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.__mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.__mainLayout)

        self.__communicationSys = Mediator()

        self.__setupSerialSys()
        self.__setupColorSys()
        self.__seperator()
        self.__setupEffectSys()

     

    def __setupSerialSys(self):
        # Call Serial MVC
        serialView = SerialView(self, self.__communicationSys)
        self.__serialModel = SerialPort()
        self.__serialController = SerialController(self.__serialModel, serialView)
        self.__mainLayout.addWidget(serialView)
        
        self.__communicationSys.registerSerialView(serialView)
         
    def __setupColorSys(self):

        targetStat = ColorView("Target", self, self.__communicationSys)
        currentStat = ColorView("Current", self, self.__communicationSys)
        currentStat.addObserver(self.__serialController)

        self.__colorController = ColorController(targetStat, currentStat)

        self.__mainLayout.addWidget(targetStat)
        self.__mainLayout.addWidget(currentStat)

        self.__communicationSys.registerCurrentColorView(currentStat)
        self.__communicationSys.registerTargetColorView(targetStat)

    def __setupEffectSys(self):
        effectView = EffectView(self, self.__communicationSys)
        self.__mainLayout.addWidget(effectView)

        self.__communicationSys.registerEffectView(effectView)

    def __seperator(self):
        line = QtGui.QFrame(self)
        line.setFrameShape(QtGui.QFrame.HLine)
        line.setFrameShadow(QtGui.QFrame.Sunken)
        self.__mainLayout.addWidget(line) 

    def closeEvent(self, event):
        self.__serialModel.closePort()
        super(LightChaser, self).closeEvent(event)

        
