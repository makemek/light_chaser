import PySide.QtGui as QtGui

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
        