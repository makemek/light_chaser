from PySide.QtGui import QColor

class Observer:

    def notify(self, color : QColor):
        raise NotImplementedError

class Subject:
    
    def addObserver(self, obs : Observer):
        raise NotImplementedError

    def removeObserver(self, obs : Observer):
        raise NotImplementedError

    def notifyObserver(self):
        raise NotImplementedError
