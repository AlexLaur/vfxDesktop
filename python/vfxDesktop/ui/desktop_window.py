from PySide6 import QtWidgets

from vfxDesktop.ui.desktop_window_ui import Ui_DesktopWindow


class DesktopWindow(QtWidgets.QMainWindow, Ui_DesktopWindow):
    def __init__(self, parent=None):
        super(DesktopWindow, self).__init__(parent)

        self.setupUi(self)
