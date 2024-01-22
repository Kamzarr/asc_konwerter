# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .DragDropListWidget import DragDropListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(432, 347)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.actionInstrukcja_u_ytkownika = QAction(MainWindow)
        self.actionInstrukcja_u_ytkownika.setObjectName(u"actionInstrukcja_u_ytkownika")
        self.actionO_programie = QAction(MainWindow)
        self.actionO_programie.setObjectName(u"actionO_programie")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.actAbout = QAction(MainWindow)
        self.actAbout.setObjectName(u"actAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(5, 0, 5, 8)
        self.frameMain = QFrame(self.centralwidget)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frameMain)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(8)
        self.gridLayout_5.setVerticalSpacing(11)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frameFiles = QFrame(self.frameMain)
        self.frameFiles.setObjectName(u"frameFiles")
        self.frameFiles.setFrameShape(QFrame.StyledPanel)
        self.frameFiles.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameFiles)
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lwFilesList = DragDropListWidget(self.frameFiles)
        self.lwFilesList.setObjectName(u"lwFilesList")
        self.lwFilesList.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.lwFilesList.setTabKeyNavigation(False)
        self.lwFilesList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout_2.addWidget(self.lwFilesList, 2, 0, 1, 8)

        self.pbAddPath = QPushButton(self.frameFiles)
        self.pbAddPath.setObjectName(u"pbAddPath")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbAddPath.sizePolicy().hasHeightForWidth())
        self.pbAddPath.setSizePolicy(sizePolicy1)
        self.pbAddPath.setMinimumSize(QSize(32, 32))
        self.pbAddPath.setMaximumSize(QSize(32, 32))
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        self.pbAddPath.setPalette(palette)
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pbAddPath.setFont(font)

        self.gridLayout_2.addWidget(self.pbAddPath, 1, 7, 1, 1)

        self.label = QLabel(self.frameFiles)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 5)

        self.pbClearAllPaths = QPushButton(self.frameFiles)
        self.pbClearAllPaths.setObjectName(u"pbClearAllPaths")
        sizePolicy1.setHeightForWidth(self.pbClearAllPaths.sizePolicy().hasHeightForWidth())
        self.pbClearAllPaths.setSizePolicy(sizePolicy1)
        self.pbClearAllPaths.setMinimumSize(QSize(32, 32))
        self.pbClearAllPaths.setMaximumSize(QSize(32, 32))
        palette1 = QPalette()
        brush2 = QBrush(QColor(222, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        self.pbClearAllPaths.setPalette(palette1)
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.pbClearAllPaths.setFont(font2)

        self.gridLayout_2.addWidget(self.pbClearAllPaths, 1, 5, 1, 1)

        self.pbRemovePath = QPushButton(self.frameFiles)
        self.pbRemovePath.setObjectName(u"pbRemovePath")
        sizePolicy1.setHeightForWidth(self.pbRemovePath.sizePolicy().hasHeightForWidth())
        self.pbRemovePath.setSizePolicy(sizePolicy1)
        self.pbRemovePath.setMinimumSize(QSize(32, 32))
        self.pbRemovePath.setMaximumSize(QSize(32, 32))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        self.pbRemovePath.setPalette(palette2)
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setKerning(True)
        self.pbRemovePath.setFont(font3)

        self.gridLayout_2.addWidget(self.pbRemovePath, 1, 6, 1, 1)


        self.gridLayout_5.addWidget(self.frameFiles, 0, 0, 1, 1)

        self.pbRunCoversions = QPushButton(self.frameMain)
        self.pbRunCoversions.setObjectName(u"pbRunCoversions")
        font4 = QFont()
        font4.setPointSize(9)
        self.pbRunCoversions.setFont(font4)

        self.gridLayout_5.addWidget(self.pbRunCoversions, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frameMain, 0, 0, 1, 2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 12))
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)

        self.lbWhatInProgress = QLabel(self.centralwidget)
        self.lbWhatInProgress.setObjectName(u"lbWhatInProgress")
        self.lbWhatInProgress.setMinimumSize(QSize(0, 20))
        self.lbWhatInProgress.setMaximumSize(QSize(16777215, 20))
        self.lbWhatInProgress.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbWhatInProgress, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 432, 26))
        self.menuO_programie = QMenu(self.menubar)
        self.menuO_programie.setObjectName(u"menuO_programie")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuO_programie.menuAction())
        self.menuO_programie.addAction(self.actAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Konwerter plik\u00f3w asc na xyz", None))
        self.actionInstrukcja_u_ytkownika.setText(QCoreApplication.translate("MainWindow", u"Instrukcja u\u017cytkownika", None))
        self.actionO_programie.setText(QCoreApplication.translate("MainWindow", u"O programie", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"O programie", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"O programie", None))
        self.actAbout.setText(QCoreApplication.translate("MainWindow", u"O programie", None))
#if QT_CONFIG(tooltip)
        self.pbAddPath.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj", None))
#endif // QT_CONFIG(tooltip)
        self.pbAddPath.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wybierz pliki asc do konwersji:", None))
#if QT_CONFIG(tooltip)
        self.pbClearAllPaths.setToolTip(QCoreApplication.translate("MainWindow", u"Usu\u0144 wszystkie", None))
#endif // QT_CONFIG(tooltip)
        self.pbClearAllPaths.setText(QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(tooltip)
        self.pbRemovePath.setToolTip(QCoreApplication.translate("MainWindow", u"Usu\u0144 wybrane", None))
#endif // QT_CONFIG(tooltip)
        self.pbRemovePath.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pbRunCoversions.setText(QCoreApplication.translate("MainWindow", u"konwertuj", None))
        self.progressBar.setFormat("")
        self.lbWhatInProgress.setText("")
        self.menuO_programie.setTitle(QCoreApplication.translate("MainWindow", u"O programie", None))
    # retranslateUi

