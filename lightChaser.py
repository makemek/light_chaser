from PySide.QtGui import *
from PySide.QtUiTools import *

from serialSys import *

class LightChaser(QWidget):
   
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.__mainLayout = QVBoxLayout()
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


        
