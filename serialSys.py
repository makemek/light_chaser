# Serial MVC

from subjectObserver import *
from PySide.QtGui import *


from serial import Serial
from view import *
import time

class SerialController(Observer):
    
    def __init__(self, view):
        self.__port = Serial()
        self.__view = view
        self.__view.setConnectButtonListener(self.openPort)

    def openPort(self):
        print("Open port")
        comName = self.__view.getPort()
        self.__port.setPort(comName)
        self.__port.setBaudrate(9600)
        self.__port.open()
        #self.__port.setTimeout(2)
        time.sleep(1)
        self.__view.setConnect(True)

    def closePort(self):
        self.sendByte(0)
        self.sendByte(0)
        self.sendByte(0)
        self.__port.close()
        self.__view.setConnect(False)

    def sendByte(self, byte):
        self.__port.write(chr(byte).encode())

    def notify(self, color : QColor):
        color = QColor
        self.sendByte(color.red())
        self.sendByte(color.green())
        self.sendByte(color.blue())

class SerialView(View):

    def __init__(self, statusLabel, connectButton, parent=None):
        self.__parent = parent
        self.__status = statusLabel

        self.__connectBt = connectButton
        
    def getPort(self):
        
        print("getPort()")
        
        ui = PortView(self.__parent)
        ui.show()
        
        # implement prompt gui ask for COM port
        print("After")
        return ""

    def setConnect(self, isConnect):
        connectMsg = "Connected"
        disconnectMsg = "Not Connected"
        if isConnect:
            self.__status.setText(connectMsg)
            self.__connectBt.setText("Disconnect")
        else:
            self.__status.setText(disconnectMsg)
            self.__connectBt.setText("Connect")

    def setConnectButtonListener(self, func):
        self.__connectBt.clicked.connect(func)

class PortView(QDialog):
    
    def __init__(self, parent=None):
        super(PortView, self).__init__(parent)
        self.setWindowTitle("Select Port")

        # implement UI