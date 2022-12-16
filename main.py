import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()

menubar = win.menuBar()
file_menu = menubar.addMenu("File")
file_menu.addAction(QAction("New", win))
file_menu.addAction(QAction("Open", win))
file_menu.addAction(QAction("Quit", win))
edit_menu = menubar.addMenu("Edit")
edit_menu.addAction(QAction("Copy", win))
edit_menu.addAction(QAction("Paste", win))
edit_menu.addAction(QAction("Cut", win))
view_menu = menubar.addMenu("View")
view_menu.addAction(QAction("Zoom in", win))
view_menu.addAction(QAction("Zoom out", win))
view_menu.addAction(QAction("Reset", win))
help_menu = menubar.addMenu("Help")
help_menu.addAction(QAction("Show help", win))

label = QLabel("Test HiDPI scaling")
label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

win.setCentralWidget(label)
win.show()

sys.exit(app.exec())
