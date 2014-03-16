import PySide.QtGui as QtGui
from serialSys import *

class LightChaser(QtGui.QWidget):
   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.__mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.__mainLayout)

        self.__setupSerialSys()
        

    def __setupSerialSys(self):
        # Call Serial MVC
        serialView = SerialView()
        self.__serialController = SerialController(serialView)
        self.__mainLayout.addWidget(serialView)
        
         
    def __setupColorSys(self):
        pass

    def __setupEffectSys(self):
        pass


        
