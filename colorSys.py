import PySide.QtGui as gui
import PySide.QtCore as QtCore

class ColorView(gui.QWidget):

    def __init__(self, name, parent=None):
        super(ColorView, self).__init__(parent)
        self.__createComponents(name)
        self.__setupComponents()
        self.__layoutComponents()

    def __createComponents(self, name):
        # Labels
        self.__headerLbl = gui.QLabel(name, self)
        
        # Spinboxes & Slider
        self.__red = ColorAdjuster("RED", self)
        self.__green = ColorAdjuster("GREEN", self)
        self.__blue = ColorAdjuster("BLUE", self)

        # Color display
        self.__display = gui.QFrame(self)

    def __setupComponents(self):
        self.__display.setStyleSheet("QFrame { background-color: %s; }" % "green")
        self.__display.setMinimumSize(60,60)
        
    def __layoutComponents(self):
        mainLayout = gui.QHBoxLayout()
        mainLayout.addWidget(self.__headerLbl)
        mainLayout.addWidget(self.__red)
        mainLayout.addWidget(self.__green)
        mainLayout.addWidget(self.__blue)
        mainLayout.addWidget(self.__display)

        self.setLayout(mainLayout)
        

    def getRed(self):
        return self.__red.getValue()

    def getGreen(self):
        return self.__green.getValue()

    def getBlue(self):
        return self.__blue.getValue()
        
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

    def __layoutComponents(self):
        mainLayout = gui.QVBoxLayout()
        formLayout = gui.QFormLayout()

        formLayout.addRow(self.__label, self.__spinBox)
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(self.__slider)

        self.setLayout(mainLayout)

    def getValue(self):
        return self.__slider.value()