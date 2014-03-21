# Serial MVC

from subjectObserver import *
import PySide.QtGui as QtGui
import LED as led

import serial as PySerial
import os

class SerialController(Observer):
    
    def __init__(self, serialModel, view):
        self.__view = view
        self.__port = serialModel
        self.__led = led.Rgb_Led()

        self.__view.setConnectButtonListener(self.bridgeConnection)
        self.__view.setLEDListener(self.__toggleLED)

        self.__isConnected = self.__port.isOpen()
        self.__view.setConnect(self.__port.isOpen())
        
    def notify(self, color):
        try:
            self.__port.sendByte(color.red())
            self.__port.sendByte(color.green())
            self.__port.sendByte(color.blue())
        except: # unplugged
            self.__led.default()
            self.__view.setConnect(False)
            if self.__port.isOpen():
                self.__port.closePort()

    def __toggleLED(self, isChecked):
        # turn off
        if not isChecked and self.__isConnected:
            self.notify(QtGui.QColor(0))

        # turn on
        elif isChecked and self.__isConnected:
            rgb = self.__led.retrieveLastState()
            self.notify(rgb)

    def bridgeConnection(self):
        if not self.__isConnected:
            try:
                portName = self.__view.getPort()
                self.__port.openPort(portName)
                self.__view.setConnect(True)
                self.__isConnected = True

            except PySerial.serialutil.SerialException as e:
                QtGui.QMessageBox().critical(None, "Port initialization failed", e.args[0])

            # cancel seclection -> invalid port name
            except ValueError:
                pass
               
        else:
            try:
                self.__port.closePort()
                self.__view.setConnect(False)
                self.__isConnected = False

            except PySerial.serialutil.SerialException as e:
                QtGui.QMessageBox().critical(None, "Port terminaltion failed", e.args[0])

class SerialPort:
    def __init__(self):
        self.__port = PySerial.Serial()
        
    def openPort(self, portName):
        print("Open port")

        if portName == "":
            raise ValueError

        self.__port.setPort(portName)
        self.__port.setBaudrate(9600)
        self.__port.setTimeout(2)
        self.__port.open()
            
    def closePort(self):
        print("Close Port")
        try:
            self.sendByte(0)
            self.sendByte(0)
            self.sendByte(0)
            self.__port.close()
        except:
            pass
        
    def sendByte(self, byte):
        self.__port.write(chr(byte).encode())

    def isOpen(self):
        return self.__port.isOpen()

class SerialView(QtGui.QWidget):

    def __init__(self, parent=None):
        self.__parent = parent
        super(SerialView, self).__init__(self.__parent)
        
        self.__createComponents()
        self.__setupComponents()
        self.__layoutComponents()
        
    def __createComponents(self):
        self.__statusLabel = QtGui.QLabel("Arduino Status", self)
        self.__status = QtGui.QLabel(self)
        self.__connectBt = QtGui.QPushButton(self)
        self.__ledSwitch = QtGui.QRadioButton("Turn on LED", self)
            
    def __setupComponents(self):
        self.__ledSwitch.setEnabled(False)
        self.setConnect(False)

    def __layoutComponents(self):
        stat = QtGui.QHBoxLayout()
        stat.addWidget(self.__statusLabel)
        stat.addWidget(self.__status)
        stat.addWidget(self.__connectBt)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(stat)
        mainLayout.addWidget(self.__ledSwitch)

        self.setLayout(mainLayout)
        
    def getPort(self):
        
        print("getPort()")
        
        ui = PortView(self)
        ui.activateWindow()
        ui.exec_() # keep executing until it closes.
        
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

        self.__ledSwitch.setEnabled(isConnect)
        self.__ledSwitch.setChecked(isConnect)
       
    def setConnectButtonListener(self, func):
        self.__connectBt.clicked.connect(func)

    def setLEDListener(self, func):
        self.__ledSwitch.toggled.connect(func)

    def setLEDSwitch(self, isEnable):
        self.__ledSwitch.setEnabled(isEnable)


class PortView(QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(PortView, self).__init__(parent)

        self.setWindowTitle("Select Port")
        self.setFixedSize(self.minimumWidth(), self.minimumHeight()) #lock screensize

        self.__createUi()
        self.__connectSignal()

        self.__portName = ""

        self.refreshPort()
        #self.__portList.addItems(["COM1","COM2","COM3","COM4"])

    def __createUi(self):
        self.__portList = QtGui.QComboBox(self)
        self.__message = QtGui.QLabel("Port : ", self)
        self.__okBt = QtGui.QPushButton("OK", self)
        
        self.__refreshBt = QtGui.QPushButton("Refresh", self)
        
        portLayout = QtGui.QHBoxLayout()
        portLayout.addWidget(self.__message)
        portLayout.addWidget(self.__portList)
        
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.__okBt)
        buttonLayout.addWidget(self.__refreshBt)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(portLayout)
        mainLayout.addLayout(buttonLayout)
        
        self.setLayout(mainLayout)
        
    def __connectSignal(self):
        self.__refreshBt.clicked.connect(self.refreshPort)
        self.__portList.currentIndexChanged.connect(self.__setPort)
        self.__okBt.clicked.connect(lambda: QtGui.QDialog.reject(self))

    def reject(self):
        self.__portName = ""
        QtGui.QDialog.reject(self)

    def getPort(self):
        return self.__portName

    def __setPort(self, idx):
        self.__portName = self.__portList.currentText()

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



    