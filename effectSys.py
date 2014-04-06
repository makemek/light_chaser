import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import random

class EffectController:
    
    def __init__(self, effectView, targetView, currentView):
        self.__view = effectView
        self.__view.setEnableSmoothTrans(False)
        self.__targetView = targetView
        self.__currentView = currentView

        self.__variator = RgbVariator()
        self.__randomizer = ColorRandomizer()

        self.__view.toggleRandomPerformed(self.performEffect)
        self.__timer = QtCore.QTimer()

    def performEffect(self, isChecked):  
        if isChecked:   
            self.randomize()

            self.__timer.setSingleShot(False)
            self.__timer.timeout.connect(self.randomize)
            self.__timer.start()
        else:
            self.__timer.stop()

    def randomize(self):
        colorPerSec = self.__view.getSpeed()
        color = ColorRandomizer.randomize()
        self.__timer.setInterval(self.calculateInterval(colorPerSec)*1000)
        print(hex(color.rgb()))
        self.__targetView.setColor(color)
        self.__currentView.setColor(color)
        


    def calculateInterval(self, speed):
        return 1/speed

class EffectView(QtGui.QWidget):
    
    def __init__(self, parent=None, mediator=None):
        self.__mediator = mediator
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
        self.__speedSb.setMinimum(1)
        self.__speedSb.setMaximum(20)
        self.__speedSb.setEnabled(False)

    def __connectSignal(self):
        self.__randomizeCb.toggled.connect(self.__speedSb.setEnabled)
        self.__smoothTransCb.toggled.connect(self.__mediator.enableSmooth)
        

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

    def setEnableRandom(self, isEnable):
        self.__randomizeCb.setChecked(isEnable)

    def setEnableSmoothTrans(self, isEnable):
        self.__smoothTransCb.setChecked(isEnable)
        self.__mediator.enableSmooth(isEnable)

    def toggleRandomPerformed(self, func):
        self.__randomizeCb.toggled.connect(func)

    def toggleVariationPerformed(self, func):
        self.__smoothTransCb.toggled.connect(func)
        
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