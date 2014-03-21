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
        pass

    def registerTargetColorView(self):
        pass

    def registerCurrentColorView(self):
        pass

    def registerEffectView(self):
        pass

    def serialReady(self):
        pass

    def colorChanged(self):
        pass

    def enableRandomize(self):
        pass

    def enableSmooth(self):
        pass