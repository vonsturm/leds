#from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QAction,
    QMenuBar,
    QMainWindow,
    QGroupBox,
    QHBoxLayout,
    QPushButton,
    QDockWidget
)

# from pygama.flow import DataLoader


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(
            "\u269B\u269B\u269B py-LEGEND EVENT DISPLAY \u269B\u269B\u269B"
        )
        self.setGeometry(200, 200, 1700, 950)
        self.move(60, 15)

    # LAYOUT
    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        # EXIT
        self.exitAction = QAction("&Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setStatusTip("Exit application")
        self.exitAction.triggered.connect(self.close)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)

    def _createMenu(self):
        menuBar = QMenuBar(self)
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        helpMenu = menuBar.addMenu("&Help")
        self.setMenuBar(menuBar)

    def _createNavigation(self):
        hGroupBox = QGroupBox("")
        layout = QHBoxLayout()
        PrevButton = QPushButton("<<")
        NextButton = QPushButton(">>")
        PrevButton.clicked.connect(self.__prev__)
        NextButton.clicked.connect(self.__next__)
        layout.addWidget(PrevButton)
        layout.addWidget(NextButton)
        hGroupBox.setLayout(layout)

        dockWidget = QDockWidget("Navigation", self)
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(hGroupBox)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

    def __next__(self):
        pass
        # self.wf_index = self.wf_index + 1
        # self._redraw(self.pw1)
        # self._redraw(self.pw2)
        # self._redraw(self.pw3)
        # self._redraw(self.pw4)

    def __prev__(self):
        pass
        # self.wf_index = max(0, self.wf_index - 1)
        # self._redraw(self.pw1)
        # self._redraw(self.pw2)
        # self._redraw(self.pw3)
        # elf._redraw(self.pw4)
