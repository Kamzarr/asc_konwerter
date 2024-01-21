from PySide2.QtWidgets import QListWidget
from PySide2.QtCore import Signal, Qt
import os

class DragDropListWidget(QListWidget):
    itemsCountChanged = Signal(int)  # Custom signal to emit item count changes

    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setAcceptDrops(True)
        self.acceptedFileDragExt = ['.txt']
        self.acceptedDirDragExt = ['.txt']

    def addAcceptedFileDragExt(self, ext):
        self.acceptedFileDragExt.append(ext)

    def clearAcceptedFileDragExt(self):
        self.acceptedFileDragExt = []

    def addAcceptedDirDragExt(self, ext):
        self.acceptedDirDragExt.append(ext)

    def clearAcceptedDirDragExt(self):
        self.acceptedDirDragExt = []

    def checkIfFileAllowed(self, file_path, accepted_ext):
        if '.*' in accepted_ext or '*' in accepted_ext:
            return True
        elif file_path.lower().endswith(tuple(ext.lower() for ext in accepted_ext)):
            return True
        else:
            return False

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            url_paths = event.mimeData().urls()
            for l_path in url_paths:
                loc_path = os.path.normpath(l_path.toLocalFile())
                if os.path.isfile(loc_path):
                    if self.checkIfFileAllowed(loc_path, self.acceptedFileDragExt):
                        event.accept()
                        break
                    else:
                        event.ignore()
                elif os.path.isdir(loc_path):
                    event.accept()
                else:
                    event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            url_paths = event.mimeData().urls()
            for l_path in url_paths:
                loc_path = os.path.normpath(l_path.toLocalFile())
                if os.path.isfile(loc_path):
                    if self.checkIfFileAllowed(loc_path, self.acceptedFileDragExt):
                        event.accept()
                        break
                    else:
                        event.ignore()
                elif os.path.isdir(loc_path):
                    event.accept()
                else:
                    event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url_paths = event.mimeData().urls()
            for l_path in url_paths:
                loc_path = os.path.normpath(l_path.toLocalFile())
                if os.path.isfile(loc_path):
                    if self.checkIfFileAllowed(loc_path, self.acceptedFileDragExt):
                        self.addItem(loc_path)
                elif os.path.isdir(loc_path):
                    all_contents = os.listdir(loc_path)
                    # Filter out only the files (not directories)
                    files_only = [os.path.join(loc_path, file) for file in all_contents if os.path.isfile(os.path.join(loc_path, file))]
                    for loc_file in files_only:
                        if self.checkIfFileAllowed(loc_file, self.acceptedDirDragExt):
                            self.addItem(loc_file)

        '''if event.mimeData().hasUrls():
            file_paths = event.mimeData().urls()
            for f_path in file_paths:
                file_path = f_path.toLocalFile()
                if self.checkIfFileAllowed(file_path, self.acceptedFileDragExt):
                    self.addItem(file_path)'''

    def deleteSelectedItems(self):
        selected_items = self.selectedItems()
        for item in selected_items:
            row = self.row(item)
            self.takeItem(row)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Delete:
            self.deleteSelectedItems()

    def addItem(self, item):
        super().addItem(item)
        self.itemsCountChanged.emit(self.count())  # Emit the signal with the new item count

    def takeItem(self, item):
        super().takeItem(item)
        self.itemsCountChanged.emit(self.count())  # Emit the signal with the new item count

    def clear(self):
        super().clear()
        self.itemsCountChanged.emit(self.count())  # Emit the signal with the new item count

