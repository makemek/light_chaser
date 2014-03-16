import PySide.QtGui as gui
import PySide.QtCore as QtCore

class ColorView(gui.QWidget):

    def __init__(self, name, parent=None):
        super(ColorView, self).__init__(parent)
        self.__createComponents(name)

    def __createComponents(self, name):
        # Labels
        self.__headerLbl = gui.QLabel(name, self)
        self.__redLbl = gui.QLabel("RED", self)
        self.__greenLbl = gui.QLabel("GREEN", self)
        self.__blueLbl = gui.QLabel("BLUE", self)

        # Spinboxes
        self.__red = ColorAdjuster(self)
        self.__green = ColorAdjuster(self)
        self.__blue = ColorAdjuster(self)

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