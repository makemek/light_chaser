import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
from effect import *

class EffectController:
    
    def __init__(self, effectView, targetView, currentView):
        self.__view = effectView
        self.__view.setEnableSmoothTrans(False)
        self.__targetView = targetView
        self.__currentView = currentView

        self.__randomizer = ColorRandomizer()
        self.__variator = RgbVariator()

        self.__view.toggleRandomPerformed(lambda isSelected: self.setEnableEffect(isSelected, self.__randomizer))
        self.__view.toggleVariationPerformed(lambda isSelected: self.setEnableEffect(isSelected, self.__variator))

        self.__effects = {}

    def setEnableEffect(self, isSelected, effect):

        if isSelected:
            self.__effects[effect] = QtCore.QTimer()

        else:
            timer = self.__effects.pop(effect)
            timer.stop()

        self.performEffect(self.__effects)
        
    def performEffect(self, effects):  
        if self.__variator in effects and self.__randomizer in effects:
            self.__effects[self.__randomizer].stop()
            self.__effects[self.__variator].stop()

            # replace timer
            self.__effects[self.__variator] = QtCore.QTimer()
            self.__effects[self.__randomizer] = QtCore.QTimer()

        if self.__variator in effects:
            timer = self.__effects[self.__variator]
            self.__handleVariation(self.__variator, timer)
            timer.setSingleShot(False)
            timer.timeout.connect(lambda: self.__handleVariation(self.__variator, timer))
            timer.start()

        else:
            for effect, timer in effects.items():
                self.__handleCommon(effect, timer)
                timer.setSingleShot(False)
                timer.timeout.connect(lambda: self.__handleCommon(effect, timer))
                timer.start()

    def __handleVariation(self, effect, timer):
        ''' Polling method '''
        targetColor = self.__targetView.getColor()
        currentColor = self.__currentView.getColor()

        if currentColor == targetColor and self.__view.isRandom():
            targetColor = self.__randomizer.perform()
            self.__targetView.setColor(targetColor)

        self.__variator.setTargetColor(targetColor)
        self.__variator.setCurrentColor(currentColor)
        self.__handleCommon(effect, timer)
        
        
    def __handleCommon(self, effect, timer):
        colorPerSec = effect.calculateInterval(self.__view.getSpeed())
        timer.setInterval(colorPerSec*1000)
        color = effect.perform()
        self.__currentView.setColor(color)

    def interrupt(self, flag):
        if flag == False:
            for timer in self.__effects.values():
                timer.stop()
        else:
            self.performEffect(self.__effects)

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
        self.__speedSb.setMaximum(40)
        #self.__speedSb.setEnabled(False)

    def __connectSignal(self):
        #self.__randomizeCb.toggled.connect(self.__speedSb.setEnabled)
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
        
