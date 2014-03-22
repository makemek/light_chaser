import PySide.QtGui as QtGui
import random

class EffectView(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(EffectView, self).__init__(parent)
        self.__createComponents()
        self.__setupComponents()
        self.__connectSignal()
        self.__layoutComponents()

    def __createComponents(self):
        self.__randomizeCb = QtGui.QCheckBox("Randomize", parent=self)
        self.__colorPerSecLbl = QtGui.QLabel("color per second", parent=self)
        self.__smoothTransCb = QtGui.QCheckBox("Smooth transition", parent=self)
        self.__speedSb = QtGui.QSpinBox(parent=self)

    def __setupComponents(self):
        self.__speedSb.setMinimum(0)
        self.__speedSb.setMaximum(20)
        self.__speedSb.setEnabled(False)

    def __connectSignal(self):
        self.__randomizeCb.stateChanged.connect(self.__speedSb.setEnabled)

    def __layoutComponents(self):
        mainLayout = QtGui.QVBoxLayout()

        randomOpt = QtGui.QHBoxLayout()
        randomOpt.addWidget(self.__randomizeCb)

        speedLayout = QtGui.QFormLayout()
        speedLayout.addRow(self.__colorPerSecLbl, self.__speedSb)
        
        randomOpt.addLayout(speedLayout)

        mainLayout.addLayout(randomOpt)
        mainLayout.addWidget(self.__smoothTransCb)

        self.setLayout(mainLayout)

    def isVariating(self):
        return self.__smoothTransCb.isChecked()

    def isRandom(self):
        return self.__randomizeCb.isChecked()

    def getSpeed(self):
        return self.__speedSb.value()
        
class RgbVariator:
    
    def __init__(self, target=QtGui.QColor(0)):
        self.__timer

        self.__target = target
        self.__current = QtGui.QColor(0)

    def variate(self):
        pass

    def setTargetColor(self, color):
        if type(color) == int:
            self.__target.setRgb(color)

        elif type(color) == QtGui.QColor:
            self.__target = color

    def setCurrentColor(color):
        pass