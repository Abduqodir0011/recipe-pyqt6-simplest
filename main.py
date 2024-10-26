import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from pages.categories import CategoriesPage
from widgets.bottom_navigation import BottomNavigationBar
from widgets.top_navigation import TopNavigationBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipes")
        self.setFixedSize(430, 930)
        self.main_layout = QVBoxLayout()
        self.__set_up_layout()
        self.setStyleSheet("background-color: #1C0F0D;")

    def __set_up_layout(self) -> None:
        top_navigation_bar = TopNavigationBar()
        page = CategoriesPage()
        bottom_navigation_bar = BottomNavigationBar()
        bottom_navigation_bar.raise_()
        self.main_layout.addWidget(top_navigation_bar, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(page, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(bottom_navigation_bar, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.main_layout)


app = QApplication(sys.argv)
app.setStyleSheet("padding: 0; margin: 0;")
window = MainWindow()
window.show()

sys.exit(app.exec())
