# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EVALUATETeam.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from player_data import player_data

class Ui_EVALUATETeam(object):
    def setupUi(self, EVALUATETeam):
        EVALUATETeam.setObjectName("EVALUATETeam")
        EVALUATETeam.resize(524, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(EVALUATETeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(EVALUATETeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_2 = QtWidgets.QComboBox(EVALUATETeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setIconSize(QtCore.QSize(25, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)

        player_data.cur.execute("select distinct name from teams;")
        for temp in tuple(player_data.cur.fetchall()):
            self.comboBox_2.addItem(str(temp[0]))

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(EVALUATETeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(60, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(EVALUATETeam)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(EVALUATETeam)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(EVALUATETeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(EVALUATETeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(EVALUATETeam)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.listWidget = QtWidgets.QListWidget(EVALUATETeam)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(EVALUATETeam)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(EVALUATETeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(EVALUATETeam)
        QtCore.QMetaObject.connectSlotsByName(EVALUATETeam)

    def retranslateUi(self, EVALUATETeam):
        _translate = QtCore.QCoreApplication.translate
        EVALUATETeam.setWindowTitle(_translate("EVALUATETeam", "EVALUATETeam"))
        self.label_3.setText(_translate("EVALUATETeam", "                   Evaluate the Performance of your Fantacy Team"))
        self.comboBox_2.setItemText(0, _translate("EVALUATETeam", "Select Team"))
        self.comboBox.setItemText(0, _translate("EVALUATETeam", "Select Match"))
        self.comboBox.setItemText(1, _translate("EVALUATETeam", "Match1"))
        self.comboBox.setItemText(2, _translate("EVALUATETeam", "Match2"))
        self.comboBox.setItemText(3, _translate("EVALUATETeam", "Match3"))
        self.comboBox.setItemText(4, _translate("EVALUATETeam", "Match4"))
        self.label.setText(_translate("EVALUATETeam", "     Players"))
        self.label_2.setText(_translate("EVALUATETeam", "               Player\'s Point"))
        self.label_5.setText(_translate("EVALUATETeam", " ##"))
        self.pushButton.setText(_translate("EVALUATETeam", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EVALUATETeam = QtWidgets.QWidget()
    ui = Ui_EVALUATETeam()
    ui.setupUi(EVALUATETeam)
    EVALUATETeam.show()
    sys.exit(app.exec_())

