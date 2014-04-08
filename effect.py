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
        return 1/(speed*5)

    def perform(self):
        sameRed = self.__target.red() == self.__current.red()
        sameGreen = self.__target.green() == self.__current.green()
        sameBlue = self.__target.blue() == self.__current.blue()

        newRed, newGreen, newBlue = self.__current.red(),self.__current.green(),self.__current.blue()

        if not sameRed: 
            newRed = self.__variate(self.__current.red(), self.__target.red())
        if not sameGreen: 
            newGreen = self.__variate(self.__current.green(), self.__target.green())
        if not sameBlue:
            newBlue = self.__variate(self.__current.blue(), self.__target.blue())

        return QtGui.QColor(newRed, newGreen, newBlue)

    def __variate(self, src, target):
        if src < target:
            src += self.__step
        elif src > target:
            src -= self.__step

        return src

    def setTargetColor(self, color):
        if type(color) == int:
            self.__target.setRgb(color)

        elif type(color) == QtGui.QColor:
            self.__target = color

        else:
            raise TypeError("Accept 'int' or 'QtGui.QColor' got {}".format(type(color)))

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