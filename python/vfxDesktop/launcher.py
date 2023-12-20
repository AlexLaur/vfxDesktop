from PySide6 import QtWidgets

from vfxDesktop.ui import DesktopWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = DesktopWindow()
    win.show()
    app.exec()
