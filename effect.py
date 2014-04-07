import PySide.QtGui as QtGui
import random

class Effect:

    def calculateInterval(self, speed):
        raise NotImplementedError

    def perform(self):
        raise NotImplementedError

class RgbVariator(Effect):
    
    def __init__(self, target=QtGui.QColor(0)):
        self.__target = target
        self.__current = QtGui.QColor(0)
        self.__step = 1

    def setStep(self, value):
        self.__step = value

    def calculateInterval(self, speed):
        pass

    def perform(self):
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

class ColorRandomizer(Effect):
    
    def calculateInterval(self, speed):
        return 1/speed

    def perform(self):
        rgb = random.randint(0, 0xFFFFFF)
        return QtGui.QColor(rgb)