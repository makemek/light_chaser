import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

from serialSys import *
from colorSys import *
from effectSys import *

from mediator import *

class LightChaser(QtGui.QWidget):
   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.__createView()
        self.__setupSerialSys()
        self.__setupColorSys()
        self.__setupEffectSys()
        self.__layoutComponents()

        self.setFixedSize(self.minimumWidth(), self.minimumHeight())

        # testing purpose
        self.__serialView.setConnect(True)
        self.__currentStat.removeObserver(self.__serialController)
        

    def __createView(self):
        communicationSys = Mediator()

        self.__serialView = SerialView(self, communicationSys)
        self.__targetStat = ColorView("Target  ", self, communicationSys)
        self.__currentStat = ColorView("Current", self, communicationSys)
        self.__effectView = EffectView(self, communicationSys)

        self.__registerMediator(communicationSys)

    def __registerMediator(self, mediator):
        mediator.registerSerialView(self.__serialView)
        mediator.registerCurrentColorView(self.__currentStat)
        mediator.registerTargetColorView(self.__targetStat)
        mediator.registerEffectView(self.__effectView)

    def __setupSerialSys(self):
        self.__serialModel = SerialPort()
        self.__serialController = SerialController(self.__serialModel, self.__serialView)

    def __setupColorSys(self):
        self.__currentStat.addObserver(self.__serialController)
        #self.__colorController = ColorController(self.__targetStat, self.__currentStat)

    def __setupEffectSys(self):
        self.__effectController = EffectController(self.__effectView, self.__targetStat, self.__currentStat)
        self.__serialView.addLEDListener(self.__effectController.interrupt)

    def __layoutComponents(self):
        self.__mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.__mainLayout)

        self.__mainLayout.addWidget(self.__serialView)
        self.__mainLayout.addWidget(self.__targetStat)
        self.__mainLayout.addWidget(self.__currentStat)
        self.__seperator()
        self.__mainLayout.addWidget(self.__effectView)

    def __seperator(self):
        line = QtGui.QFrame(self)
        line.setFrameShape(QtGui.QFrame.HLine)
        line.setFrameShadow(QtGui.QFrame.Sunken)
        self.__mainLayout.addWidget(line) 

    def closeEvent(self, event):
        self.__serialModel.closePort()
        self.__currentStat.setEnabled(False)
        self.__targetStat.setEnabled(False)
        self.__effectController.interrupt(0)
        super(LightChaser, self).closeEvent(event)

        
