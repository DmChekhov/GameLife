from PyQt5 import QtCore, QtWidgets
from inner_logic import current_generation_set, next_generation_set, current_mask, next_mask, make_mask


class Cell(QtWidgets.QLabel):
    colorLive = "#FFFF90"
    colorDead = "#000000"

    cellClicked = QtCore.pyqtSignal(tuple)  # Наверное, тут надо будет переписать под клик мышкой

    def __init__(self, id=(0, 0), bgColor=colorDead, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setFixedSize(10, 10)
        self.setMargin(0)
        self.id = id
        self.live = False
        self.bgColorDefault = bgColor
        self.bgColorCurrent = bgColor
        self.showColorCurrent()

    def mousePressEvent(self, evt):  # переписать под логику нажимания на клетку
        if self.live:
            self.cellClicked.emit(self.id)
            self.bgColorCurrent = "#000000"
            self.live = False
            current_generation_set.remove(self.id)
            print(current_generation_set)
            self.showColorCurrent()
            QtWidgets.QLabel.mousePressEvent(self, evt)
        else:
            self.cellClicked.emit(self.id)
            self.bgColorCurrent = "#FFFF90"
            self.live = True
            current_generation_set.add(self.id)
            x, y = self.id
            make_mask(current_mask, x, y, 10, 10)
            print(current_generation_set)
            print(current_mask)
            self.showColorCurrent()
            QtWidgets.QLabel.mousePressEvent(self, evt)  # ШО ЗА НАХ

    def showColorCurrent(self):
        self.setStyleSheet('background-color:' + self.bgColorCurrent + ';')
