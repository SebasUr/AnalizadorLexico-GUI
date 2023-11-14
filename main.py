# This Python file uses the following encoding: utf-8
import sys
import sys
from ui_form import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Funcs import *
import re

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btnPwd.clicked.connect(self.validarPassword)
        self.set_background_image("background2.png")
        
    def set_background_image(self, image_path):
        background = QPixmap(image_path)
        background_label = QLabel(self)
        background_label.setPixmap(background)
        background_label.setGeometry(0, 0, background.width(), background.height())
        background_label.lower()

    def validarPassword(self):
        texto = self.ui.TXTpWD.text()
        if(texto==""):
            self.ui.lblSalida.setText("Introduce una entrada válida")
        elif(len(texto)>58):
            self.ui.lblSalida.setText("Introduce una entrada más corta")
        else:
            self.ui.lblSalida.setText(convertirAEmoji(texto)[0])
            self.ui.lblSalida_2.setText(f"Num Emojis: {convertirAEmoji(texto)[1]} NumPalabras {convertirAEmoji(texto)[2]} ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())