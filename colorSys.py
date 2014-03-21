import PySide.QtGui as gui
import PySide.QtCore as QtCore
from subjectObserver import Subject

# may use mediator design pattern instead

class ColorController():

    def __init__(self, targetView, currentView):
        self.__targetView = targetView
        self.__currentView = currentView

        self.__targetView.setVisible(False) # let effectSys manage

        



class ColorView(gui.QWidget, Subject):

    def __init__(self, name, parent=None):
        super(ColorView, self).__init__(parent)
        self.__createComponents(name)
        self.__setupComponents()
        self.__layoutComponents()
        self.__connectSignal()

        self.__obs = []
        self.actionPerformed(self.notifyObserver)

    def __createComponents(self, name):
        # Labels
        self.__headerLbl = gui.QLabel(name, self)
        
        # Spinboxes & Slider
        self.__red = ColorAdjuster("RED", self)
        self.__green = ColorAdjuster("GREEN", self)
        self.__blue = ColorAdjuster("BLUE", self)

        # Color display
        self.__display = ColorDisplay(parent=self)

    def __setupComponents(self):
        self.__display.setMinimumSize(60,60)
        
    def __layoutComponents(self):
        mainLayout = gui.QHBoxLayout()
        mainLayout.addWidget(self.__headerLbl)
        mainLayout.addWidget(self.__red)
        mainLayout.addWidget(self.__green)
        mainLayout.addWidget(self.__blue)
        mainLayout.addWidget(self.__display)

        self.setLayout(mainLayout)
        
    def __connectSignal(self):
        self.__red.connect(self.__colorChanged)
        self.__green.connect(self.__colorChanged)
        self.__blue.connect(self.__colorChanged)

    def __colorChanged(self, dummyVar):
        self.__display.setColor(self.getColorAsRGB())
        self.notifyObserver()

    def getColorAsRGB(self):
        rgb = self.getBlue()
        rgb |= self.getGreen() << 8
        rgb |= self.getRed() << 16
        return rgb

    def getRed(self):
        return self.__red.getValue()

    def getGreen(self):
        return self.__green.getValue()

    def getBlue(self):
        return self.__blue.getValue()

    def actionPerformed(self, method):
        self.__red.connect(method)
        self.__green.connect(method)
        self.__blue.connect(method)

    def addObserver(self, obs):
        self.__obs.append(obs)

    def removeObserver(self, obs):
        self.__obs.remove(obs)

    def notifyObserver(self):
        color = gui.QColor(self.getColorAsRGB())
        for o in self.__obs:
            o.notify(color)
        
class ColorAdjuster(gui.QWidget):

    def __init__(self, channel, parent=None):
        super(ColorAdjuster, self).__init__(parent)
        self.__createComponents(channel)
        self.__setupComponents()
        self.__connectSignal()
        self.__layoutComponents()

    def __createComponents(self, name):
        self.__label = gui.QLabel(name, self)
        self.__spinBox = gui.QSpinBox(self)
        self.__slider = gui.QSlider(self)

    def __setupComponents(self):
        self.__spinBox.setMinimum(0)
        self.__slider.setMinimum(0)

        self.__spinBox.setMaximum(0xFF)
        self.__slider.setMaximum(0xFF)

        self.__slider.setOrientation(QtCore.Qt.Horizontal)

    def __connectSignal(self):
        self.__spinBox.valueChanged.connect(self.__slider.setValue)
        self.__slider.valueChanged.connect(self.__spinBox.setValue)

    def connect(self, func):
        self.__spinBox.valueChanged.connect(func)
        self.__slider.valueChanged.connect(func)

    def __layoutComponents(self):
        mainLayout = gui.QVBoxLayout()
        formLayout = gui.QFormLayout()

        formLayout.addRow(self.__label, self.__spinBox)
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(self.__slider)

        self.setLayout(mainLayout)

    def getValue(self):
        return self.__slider.value()

class ColorDisplay(gui.QFrame):

    def __init__(self, initialColor=0, parent=None):
        super(ColorDisplay, self).__init__(parent)

        self.__styleSheet = "QFrame { background-color: #%s; }"
        self.setColor(initialColor)

    def setColor(self, rgbVal):
        self.setStyleSheet(self.__styleSheet % hex(rgbVal)[2:].zfill(6))