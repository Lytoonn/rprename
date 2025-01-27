# # -*- coding: utf-8 -*-
# rprename.py/__init__.py

"""This module provides the rprename package."""

from collections import deque
from pathlib import Path

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox

from .ui.window import Ui_Window
from .rename import Renamer

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
    )
)

class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self._setupUi()
        self._connectSignalSlot()
        self._updateStateWhenNoFiles()

    def _updateStateWhenNoFiles(self):
        self._files = deque()
        self._filesCount = 0
        
    def _setupUi(self):
        self.setupUi(self)

    def _connectSignalSlot(self):
        self.loadFilesButton.clicked.connect(self.loadFiles())
        self.renameFilesButton.clicked.connect(self.renameFiles())

    def loadFiles(self):
        self.dstFileList.clear()
        init_dir = self.dirEdit.text() if self.dirEdit.text() else str(Path.home) 
        files, filter_ = QFileDialog.getOpenFileNames(
            self, "Choose Files to Rename", init_dir, filter=FILTERS
        )

        if len(files) > 0:
            file_extension = filter_[filter_.index('*') : -1]
            self.extensionLabel.setText(file_extension)
            src_dir_name = str(Path(files[0]).parent)
            self.dirEdit.setText(src_dir_name)
            for file in files:
                file_path = Path(file)
                if file_path not in self._files:   # let's avoid duplicate files
                    self._files.append(file_path)
                    self.srcFileList.addItem(file)
            self._files_count = len(self._files)

            # self._update_state_when_files_loaded()

    def renameFiles(self):
        self._runRenamerThread()

    def _runRenamerThread(self):
        prefix = self.prefixEdit.text()
        self.renamer = Renamer(
            files = self._files,
            prefix = prefix,
        )

        self._renamer.renamedFile.connect(self._updateStateWhenFileRenamed)

    def _updateStateWhenFileRenamed(self, newFile: Path):
        self._files.popleft()
        self.srcFileList.takeItem(0)
        self.dstFileList.addItem(str(newFile))