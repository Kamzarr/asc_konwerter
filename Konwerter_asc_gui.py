import datetime
import os
import shutil
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QDialog, QStyledItemDelegate, \
    QHeaderView, QTableWidgetItem, QLabel, QMenu, QMenuBar
from PySide2.QtCore import Qt, QObject, Signal, Slot, QThread, QTimer, QUrl


from ui.main_window import Ui_MainWindow
from ui.convert_result_output import Ui_ResultDialog
from ui.about import Ui_AboutDialog

from asc_converter import AscConverter

class ResultOutputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ResultDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.setWindowModality(Qt.ApplicationModal)
        self.adjustSize()
        self.show()

    @Slot()
    def on_pbOk_clicked(self):
        self.accept()

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)


class ConwerterWorker(QObject):
    # finished = Signal(dict, str)
    finished = Signal(list, list)
    progress_update = Signal(str)

    def __init__(self):
        super().__init__()
        self.files_list = []

    @Slot()
    def setFilesList(self, files_list):
        self.files_list = files_list

    @Slot()
    def runConversion(self):
        if len(self.files_list) > 0:
            try:
                self.progressMessage('rozpoczęcie konwersji plików')
                asc_converter = AscConverter()
                asc_converter.progress_update.connect(self.progressMessage)
                asc_converter.ListAscToXyz(self.files_list)

                self.finished.emit(['ok'], ['ok'])
            except Exception as err:
                self.finished.emit(None, [str(err)])

        else:
            self.finished.emit(None, ['Nie wybrano żadnego pliku'])

    def progressMessage(self, pr_message):
        self.progress_update.emit(pr_message)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lwFilesList.addAcceptedFileDragExt('.asc')
        self.ui.lwFilesList.addAcceptedDirDragExt('.asc')
        self.handleEnableRemoveButton()

        self.files_list = []
        self.converter_thread = QThread()
        self.converter_worker = ConwerterWorker()
        self.converter_worker = ConwerterWorker()
        self.converter_worker.moveToThread(self.converter_thread)
        self.converter_worker.finished.connect(self.onConversionFinished)
        self.converter_worker.progress_update.connect(self.onConversionProgressUpdate)
        self.converter_thread.started.connect(self.converter_worker.runConversion)



        self.timer = QTimer(self)
        self.stopProgressBar()
        self.timer.timeout.connect(self.updateProgressBar)
        self.value = 0
        self.sign = 1


        self.adjustSize()

    def handleEnableRemoveButton(self):
        if len(self.ui.lwFilesList.selectedItems()) > 0:
            self.ui.pbRemovePath.setEnabled(True)
        else:
            self.ui.pbRemovePath.setEnabled(False)
    def read_list_widget_items(self, list_widget):
        items = []
        for index in range(list_widget.count()):
            item = list_widget.item(index)
            items.append(item.text())
        return items

    def updateProgressBar(self):
        self.ui.progressBar.setValue(self.value)
        if self.sign == -1:
            self.ui.progressBar.setInvertedAppearance(True)
        else:
            self.ui.progressBar.setInvertedAppearance(False)

        if self.value == 99:
            self.sign = -1
        elif self.value == 0:
            self.sign = 1

        self.value += self.sign * 1

    def startProgressBar(self):
        self.ui.progressBar.setValue(self.value)
        self.ui.frameMain.setEnabled(False)
        self.ui.progressBar.setVisible(True)
        self.timer.start(50)  # Update every 1000 milliseconds (1 second)

    def stopProgressBar(self):
        self.ui.frameMain.setEnabled(True)
        self.ui.progressBar.setVisible(False)
        self.timer.stop()


    ### SIGNALS:
    ## sygnaly walidatora:
    @Slot()
    def onConversionFinished(self, summary_result, more_info):
        self.ui.lbWhatInProgress.setText('')
        self.stopProgressBar()

        self.converter_thread.quit()
        self.converter_thread.wait()

        def show_error_message(r_info):
            m_info = 'Nie udało się wykonać konwersji'
            res_wind.ui.lbMainInfo.setText(m_info)
            res_wind.ui.lbResult.setText(r_info)

        res_wind = ResultOutputDialog()
        if not summary_result:
            result_info = f'<font color="#FF0000">Błąd</font>: {more_info[0]}'
            show_error_message(result_info)
        elif summary_result:
            main_info = 'konwersja zakończona'
            res_wind.ui.lbMainInfo.setText(main_info)
        else:
            result_info = '?'
            show_error_message(result_info)

        #res_wind.adjustSize()
        result = res_wind.exec_()

        if result == QDialog.Accepted:
            pass
        else:
            pass

    @Slot(str)
    def onConversionProgressUpdate(self, progress_message):
        """ Update your GUI to show the progress message, e.g., in a label or status bar."""
        '''# jesli byly jakies pliki xsd zrobione na lokalne to odswiezana jest sciezka
        # (bo moglo go w ogole nie byc wczesniej, i byla wtedy zla sciezka w pliku ustawien)
        if progress_message == 'files_made_local':
            self.setXsdForBase(self.ui.cmbBase.currentText())
            self.saveFormSettings()'''
        self.ui.lbWhatInProgress.setText(progress_message)

    ## sygnaly okna:
    @Slot()
    def on_lwFilesList_itemSelectionChanged(self):
        self.handleEnableRemoveButton()

    @Slot()
    def on_pbRunCoversions_clicked(self):
        self.value = 0
        self.ui.lbWhatInProgress.setText('')
        self.startProgressBar()

        self.files_list = self.read_list_widget_items(self.ui.lwFilesList)

        self.converter_worker.setFilesList(self.files_list)
        self.converter_thread.start()

        '''sheets = {'RaportKonkluzja': False,
                  'NazwaPliku': False,
                  'ZawartoscPliku': True,
                  'WalidacjaXSD': True,
                  'Ograniczenia': True}'''

    @Slot()
    def on_pbAddPath_clicked(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(self, 'Wybierz pliki asc',
                                                     '',  # Empty string for default directory
                                                     'asc (*.asc);;Wszystkie pliki (*)',
                                                     options=options)
        if file_paths:
            self.ui.lwFilesList.addItems(file_paths)

    @Slot()
    def on_pbRemovePath_clicked(self):
        self.ui.lwFilesList.deleteSelectedItems()

    @Slot()
    def on_pbClearAllPaths_clicked(self):
        self.ui.lwFilesList.clear()

    @Slot()
    def on_actionAbout_triggered(self):
        about = AboutDialog()
        about.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    '''widget_login = LogInWidget()
    widget_login.show()'''
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
