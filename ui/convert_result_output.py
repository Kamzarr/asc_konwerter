# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_result_output.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ResultDialog(object):
    def setupUi(self, ResultDialog):
        if not ResultDialog.objectName():
            ResultDialog.setObjectName(u"ResultDialog")
        ResultDialog.resize(404, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResultDialog.sizePolicy().hasHeightForWidth())
        ResultDialog.setSizePolicy(sizePolicy)
        ResultDialog.setMinimumSize(QSize(400, 150))
        self.gridLayout = QGridLayout(ResultDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.lbMainInfo = QLabel(ResultDialog)
        self.lbMainInfo.setObjectName(u"lbMainInfo")
        font = QFont()
        font.setPointSize(9)
        self.lbMainInfo.setFont(font)
        self.lbMainInfo.setAlignment(Qt.AlignCenter)
        self.lbMainInfo.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lbMainInfo, 0, 0, 1, 3)

        self.pbOk = QPushButton(ResultDialog)
        self.pbOk.setObjectName(u"pbOk")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbOk.sizePolicy().hasHeightForWidth())
        self.pbOk.setSizePolicy(sizePolicy1)
        self.pbOk.setMinimumSize(QSize(120, 0))
        self.pbOk.setFont(font)
        self.pbOk.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.pbOk, 2, 1, 1, 1)

        self.lbResult = QLabel(ResultDialog)
        self.lbResult.setObjectName(u"lbResult")
        self.lbResult.setFont(font)
        self.lbResult.setAlignment(Qt.AlignCenter)
        self.lbResult.setWordWrap(True)
        self.lbResult.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lbResult, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.retranslateUi(ResultDialog)

        QMetaObject.connectSlotsByName(ResultDialog)
    # setupUi

    def retranslateUi(self, ResultDialog):
        ResultDialog.setWindowTitle(QCoreApplication.translate("ResultDialog", u"Wynik kontroli", None))
        self.lbMainInfo.setText("")
        self.pbOk.setText(QCoreApplication.translate("ResultDialog", u"Ok", None))
        self.lbResult.setText("")
    # retranslateUi

