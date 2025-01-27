# -*- coding: utf-8 -*-

# rprename/rename.py


"""This module provides the Renamer class to rename multiple files."""

import time

from pathlib import Path

from PySide6.QtCore import QObject, Signal

class Renamer(QObject):

    # Define custom signals
    progressed = Signal(int)
    renamedFile = Signal(Path)
    finished = Signal()


    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix


    def renameFiles(self):
        for fileNumber, file in enumerate(self._files, 1):
            newFile = file.parent.joinpath(
                f"{self._prefix}{str(fileNumber)}{file.suffix}"
            )
            file.rename(newFile)
            time.sleep(0.1)
            self.progressed.emit(fileNumber)
            self.renamedFile.emit(newFile)

        self.progressed.emit(0)
        self.finished.emit()