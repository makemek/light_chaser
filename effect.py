import PySide.QtGui as QtGui
import random

class RgbVariator:
    
    def __init__(self, target=QtGui.QColor(0)):
        self.__target = target
        self.__current = QtGui.QColor(0)

    def variate(self, step):
        sameRed = self.__target.red() == self.__current.red()
        sameGreen = self.__target.green() == self.__current.green()
        sameBlue = self.__target.blue() == self.__current.blue()

        if not sameRed: self.__current.setRed(self.__current.red() + step)
        if not sameGreen: self.__current.setGreen(self.__current.green() + step)
        if not sameBlue: self.__current.setRed(self.__current.blue() + step)

    def setTargetColor(self, color):
        if type(color) == int:
            self.__target.setRgb(color)

        elif type(color) == QtGui.QColor:
            self.__target = color

    def setCurrentColor(self, color):
        self.__current = color

    def getCurrentColor(self):
        return self.__current

class ColorRandomizer:
    
    @staticmethod
    def randomize():
        rgb = random.randint(0, 0xFFFFFF)
        return QtGui.QColor(rgb)