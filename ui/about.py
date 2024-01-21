# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(328, 172)
        font = QFont()
        font.setPointSize(9)
        AboutDialog.setFont(font)
        self.gridLayout = QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.label_8 = QLabel(AboutDialog)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.label_3 = QLabel(AboutDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(AboutDialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_7 = QLabel(AboutDialog)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label = QLabel(AboutDialog)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(AboutDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(AboutDialog)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_4 = QLabel(AboutDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_9 = QLabel(AboutDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 2)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("AboutDialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("AboutDialog", u"Autor:", None))
        self.label_6.setText(QCoreApplication.translate("AboutDialog", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("AboutDialog", u"Kamil Zarzyczny", None))
        self.label.setText(QCoreApplication.translate("AboutDialog", u"Wersja:", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Kod \u017br\u00f3d\u0142owy:", None))
        self.label_5.setText(QCoreApplication.translate("AboutDialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("AboutDialog", u"Kontakt:", None))
        self.label_9.setText(QCoreApplication.translate("AboutDialog", u"2024", None))
    # retranslateUi

