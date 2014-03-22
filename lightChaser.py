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

        self.__createView()
        self.__setupSerialSys()
        self.__setupColorSys()
        self.__seperator()
        self.__setupEffectSys()

    def __createView(self):
        self.__serialView = SerialView(self, self.__communicationSys)
        self.__targetStat = ColorView("Target", self, self.__communicationSys)
        self.__currentStat = ColorView("Current", self, self.__communicationSys)
        self.__effectView = EffectView(self, self.__communicationSys)

    def __setupSerialSys(self):
        # Call Serial MVC
        self.__serialModel = SerialPort()
        self.__serialController = SerialController(self.__serialModel, self.__serialView)
        self.__mainLayout.addWidget(self.__serialView)
        
        self.__communicationSys.registerSerialView(self.__serialView)
         
    def __setupColorSys(self):

        currentStat.addObserver(self.__serialController)

        self.__colorController = ColorController(self.__targetStat, self.__currentStat)

        self.__mainLayout.addWidget(self.__targetStat)
        self.__mainLayout.addWidget(self.__currentStat)

        self.__communicationSys.registerCurrentColorView(self.__currentStat)
        self.__communicationSys.registerTargetColorView(self.__targetStat)

    def __setupEffectSys(self):
        self.__mainLayout.addWidget(self.__effectView)

        self.__communicationSys.registerEffectView(self.__effectView)

    def __seperator(self):
        line = QtGui.QFrame(self)
        line.setFrameShape(QtGui.QFrame.HLine)
        line.setFrameShadow(QtGui.QFrame.Sunken)
        self.__mainLayout.addWidget(line) 

    def closeEvent(self, event):
        self.__serialModel.closePort()
        super(LightChaser, self).closeEvent(event)

        
