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
        AboutDialog.resize(460, 220)
        font = QFont()
        font.setPointSize(9)
        AboutDialog.setFont(font)
        self.gridLayout = QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.lbContact = QLabel(AboutDialog)
        self.lbContact.setObjectName(u"lbContact")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbContact.sizePolicy().hasHeightForWidth())
        self.lbContact.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        self.lbContact.setFont(font1)
        self.lbContact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbContact.setOpenExternalLinks(True)
        self.lbContact.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lbContact, 3, 1, 1, 1)

        self.label_3 = QLabel(AboutDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lbCode = QLabel(AboutDialog)
        self.lbCode.setObjectName(u"lbCode")
        sizePolicy.setHeightForWidth(self.lbCode.sizePolicy().hasHeightForWidth())
        self.lbCode.setSizePolicy(sizePolicy)
        self.lbCode.setFont(font1)
        self.lbCode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbCode.setOpenExternalLinks(True)
        self.lbCode.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lbCode, 1, 1, 1, 1)

        self.lbAuthor = QLabel(AboutDialog)
        self.lbAuthor.setObjectName(u"lbAuthor")
        sizePolicy.setHeightForWidth(self.lbAuthor.sizePolicy().hasHeightForWidth())
        self.lbAuthor.setSizePolicy(sizePolicy)
        self.lbAuthor.setFont(font1)
        self.lbAuthor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbAuthor.setOpenExternalLinks(True)
        self.lbAuthor.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lbAuthor, 2, 1, 1, 1)

        self.label = QLabel(AboutDialog)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(AboutDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lbVersion = QLabel(AboutDialog)
        self.lbVersion.setObjectName(u"lbVersion")
        sizePolicy.setHeightForWidth(self.lbVersion.sizePolicy().hasHeightForWidth())
        self.lbVersion.setSizePolicy(sizePolicy)
        self.lbVersion.setFont(font1)
        self.lbVersion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbVersion.setOpenExternalLinks(True)
        self.lbVersion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lbVersion, 0, 1, 1, 1)

        self.label_4 = QLabel(AboutDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

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
        self.lbContact.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p>kamzar24@gmail.com</p><p><a href=\"https://github.com/Kamzarr\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Kamzarr<br/></span></a></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AboutDialog", u"Autor:", None))
        self.lbCode.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p><a href=\"https://github.com/Kamzarr/asc_konwerter\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Kamzarr/asc_konwerter</span></a></p></body></html>", None))
        self.lbAuthor.setText(QCoreApplication.translate("AboutDialog", u"Kamil Zarzyczny", None))
        self.label.setText(QCoreApplication.translate("AboutDialog", u"Wersja:", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Kod \u017br\u00f3d\u0142owy:", None))
        self.lbVersion.setText(QCoreApplication.translate("AboutDialog", u"v", None))
        self.label_4.setText(QCoreApplication.translate("AboutDialog", u"Kontakt:", None))
        self.label_9.setText(QCoreApplication.translate("AboutDialog", u"2024", None))
    # retranslateUi

