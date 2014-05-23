import PySide.QtGui as QtGui

class GuiActivity(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(GuiActivity, self).__init__(parent)

        self._createComponents()
        self._setupComponents()
        self._connectSignal()
        self._layoutComponents()

    def _createComponents(self):
        raise NotImplementedError

    def _setupComponents(self):
        raise NotImplementedError

    def _layoutComponents(self):
        raise NotImplementedError

    def _connectSignal(self):
        raise NotImplementedError