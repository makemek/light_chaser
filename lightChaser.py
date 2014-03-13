from PySide.QtGui import *
from PySide.QtUiTools import *

from serialSys import *

class LightChaser(QWidget):
   
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.__uiFile = "SE DEV UI Design new ver.ui"
        directory = "./" + self.__uiFile

        loader = QUiLoader()
        self.__gui = QWidget
        self.__gui = loader.load(directory, self)

        self.setFixedSize(self.__gui.width(), self.__gui.height())

        self.__setupSerialSys()

    def __setupSerialSys(self):
        status = QLabel
        status = self.__gui.findChild(status, "status")
    
        connectBt = QPushButton
        connectBt = self.__gui.findChild(connectBt, "connectBt")

        # Call Serial MVC
        self.__controller = SerialController(SerialView(status, connectBt, self))
        
        
        
    def __setupColorSys(self):
        pass

    def __setupEffectSys(self):
        pass