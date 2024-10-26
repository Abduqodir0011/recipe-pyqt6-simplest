from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

from utils.file import create_image_label


class CategoryItem(QWidget):
    def __init__(self, title: str, photo: str, photo_width: float, photo_height: float, reverse_title_and_photo: bool = False):
        super().__init__()
        self.layout = QVBoxLayout()
        self.title_label = self.__create_title_label(title)
        self.title_label.setFixedHeight(20)
        self.image_label = create_image_label(photo, photo_width, photo_height)
        self.setFixedHeight(200)
        self.__set_up_layout(reverse_title_and_photo)

    def __create_title_label(self, title: str) -> QLabel:
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        return title_label

    def __set_up_layout(self, reverse_title_and_photo: bool):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if reverse_title_and_photo:
            self.layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
            self.layout.addWidget(self.image_label)
        else:
            self.layout.addWidget(self.image_label)
            self.layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.setLayout(self.layout)
