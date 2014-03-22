from serialSys import SerialView
from colorSys import ColorView
from effectSys import EffectView

class Mediator:
    
    def __init__(self):
        pass

    def registerSerialView(self, view):
        self.__serialView = view

    def registerTargetColorView(self, view):
        self.__targetView = view

    def registerCurrentColorView(self, view):
        self.__currentView = view

    def registerEffectView(self, view):
        self.__effectView = view

    def serialReady(self, isReady):
        self.__targetView.setEnabled(isReady)
        self.__currentView.setEnabled(isReady)
        self.__effectView.setEnabled(isReady)

    def changeCurrentColorView(self, color):
        self.__currentView.setColor(color)

    def changeTargetColorView(self, color):
        self.__targetView.setColor(color)

    def enableSmooth(self, isEnable):
        self.__targetView.setVisible(isEnable)