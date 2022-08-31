from PyQt5 import QtCore, QtGui, QtWidgets

from cell import Cell


class Field(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        vBoxMain = QtWidgets.QVBoxLayout()

        frame1 = QtWidgets.QFrame()
        frame1.setStyleSheet(
            "background-color:#9AA6A7;border:1px solid #9AA6A7;")

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(0)

        HEIGHT = 10
        WIDTH = 10

        self.cells = [Cell((i, j)) for i in range(HEIGHT) for j in range(WIDTH)]
#        self.cells[0].setCellFocus()
        self.idCellInFocus = 0
        i = 0
        for j in range(HEIGHT):  # Наверное, стоит изменить запихивание на оптимальный вариант
            for k in range(WIDTH):
                grid.addWidget(self.cells[i], j, k)
                i += 1

#        for cell in self.cells:
#            cell.changeCellFocus.connect(self.onChangeCellFocus)

        frame1.setLayout(grid)
        vBoxMain.addWidget(frame1, alignment=QtCore.Qt.AlignHCenter)

        frame2 = QtWidgets.QFrame()
        frame2.setFixedSize(272, 36)  # Надо поменять
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.setSpacing(1)

        self.btn_start_stop = QtWidgets.QPushButton('СТАРТ')
        self.btn_start_stop.setFixedSize(70, 27)
        self.hbox.addWidget(self.btn_start_stop)
        self.btn_start_stop.clicked.connect(self.click_start_stop)



        frame2.setLayout(self.hbox)
        vBoxMain.addWidget(frame2, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vBoxMain)

    def click_start_stop(self):
        if self.btn_start_stop.text() == 'СТАРТ':
            self.btn_start_stop.setText('СТОП')
        else:
            self.btn_start_stop.setText('СТАРТ')