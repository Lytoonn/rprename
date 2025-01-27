# # -*- coding: utf-8 -*-
# rprename.py/__init__.py

"""This module provides the rprename package."""

from collections import deque
from pathlib import Path

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QFileDialog, QWidget

from .ui.window import Ui_Window

class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self._setupUi()
        
    def _setupUi(self):
        self.setupUi(self)