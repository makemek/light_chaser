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

    def enableSmooth(self, isEnable):
        self.__targetView.setVisible(isEnable)
        self.__targetView.setColor(self.__currentView.getColor())
        parent = self.__targetView.parent()
        sizeHint = parent.minimumSizeHint()
        if sizeHint.width() > 0 and sizeHint.height() > 0:
            parent.setFixedSize(sizeHint)
        
