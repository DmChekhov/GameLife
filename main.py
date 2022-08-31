from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from field import Field
#  from modules.previewdialog import PreviewDialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent,
                                       flags=QtCore.Qt.Window |
                                             QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Game Life")

        self.setStyleSheet(
            "QFrame QPushButton {font-size:10pt;font-family:Verdana;"
            "color:black;font-weight:bold;}"
            "MyLabel {font-size:14pt;font-family:Verdana;"
            "border:1px solid #9AA6A7;}")

        self.settings = QtCore.QSettings('Conway')

        self.field = Field()
        self.setCentralWidget(self.field)

        statusBar = self.statusBar()
        statusBar.setSizeGripEnabled(False)
        # statusBar.showMessage('Выглядит убого :(', 20000)

        if self.settings.contains("X") and self.settings.contains("Y"):
            self.move(self.settings.value("X"), self.settings.value("Y"))

    def closeEvent(self, evt):
        g = self.geometry()
        self.settings.setValue("X", g.left())
        self.settings.setValue("Y", g.top())


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
# print(vars(Field.btn_start_stop))
sys.exit(app.exec_())