# # -*- coding: utf-8 -*-
# rprename.py/__init__.py

"""
This module provides the RP Renamer Application
"""
import sys

from PySide6.QtWidgets import QApplication

from .views import Window

def main():
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
    sys.exit(app.exec())
    #return app.exec()