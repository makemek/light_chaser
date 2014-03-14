# Serial MVC

from subjectObserver import *
from PySide.QtGui import *

import serial as PySerial
from view import *
import time
import os

class SerialController(Observer):
    
    def __init__(self, view):
        self.__port = PySerial.Serial()
        self.__view = view
        self.__view.setConnectButtonListener(self.openPort)

    def openPort(self):
        print("Open port")
        comName = self.__view.getPort()
        if len(comName) == 0:
            return
        
        try:
            self.__port.setPort(comName)
            self.__port.setBaudrate(9600)
            self.__port.open()
            self.__port.setTimeout(2)
            
            self.__view.setConnect(True)
        except PySerial.serialutil.SerialException:
            QErrorMessage("Unable to open port: + " + comName)

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
        ui.activateWindow()
        ui.show()
        
        print("After")

        return ui.getPort()

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

class PortView(QDialog, View):
    
    def __init__(self, parent=None):
        super(PortView, self).__init__(parent)

        self.setWindowTitle("Select Port")
        self.createUi()
        self.refreshPort()

    def createUi(self):
        self.__portList = QComboBox()
        self.__message = QLabel("Port : ")
        self.__okBt = QPushButton("OK")
        
        self.__refreshBt = QPushButton("Refresh")
        self.__refreshBt.clicked.connect(self.refreshPort)
        
        portLayout = QHBoxLayout()
        portLayout.addWidget(self.__message)
        portLayout.addWidget(self.__portList)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.__okBt)
        buttonLayout.addWidget(self.__refreshBt)
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(portLayout)
        mainLayout.addLayout(buttonLayout)
        
        self.setLayout(mainLayout)

    def getPort(self):
        return self.__portList.currentText()

    def refreshPort(self):
        self.__portList.clear()
        for port in self.__serial_ports():
            self.__portList.addItem(port)

        if self.__portList.count() == 0:
            self.__okBt.setEnabled(False)

        else:
            self.__okBt.setEnabled(True)

    def __serial_ports(self):
        '''
        Returns a generator for all available serial ports
        '''
        if os.name == 'nt':
            # windows
            for i in range(256):
                try:
                    s = PySerial.Serial(i)
                    s.close()
                    yield 'COM' + str(i + 1)
                except PySerial.serialutil.SerialException:
                    pass
        else:
            # unix
            for port in list_ports.comports():
                yield port[0]



    