from serialSys import SerialView
from colorSys import ColorView
from effectSys import EffectView

class Mediator:
    
    def __init__(self):
        # These are type for auto complete only
        self.__serialView = SerialView
        self.__targetView = ColorView
        self.__currentView = ColorView
        self.__effectView = EffectView

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

    def colorChanged(self):
        pass

    def enableRandomize(self):
        pass

    def enableSmooth(self):
        pass