import PySide.QtGui as QtGui
class Rgb_Led:
    
    def __init__(self, rgbVal=0):
        self.__rgbVal = rgbVal

    def storeState(self, rgbVal):
        self.__rgbVal = rgbVal

    def retrieveLastState(self):
        return self.__rgbVal

    def default(self):
        self.__rgbVal = QtGui.QColor(0)
