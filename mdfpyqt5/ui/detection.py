# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1600, 900)
        widget.setMinimumSize(QtCore.QSize(1600, 900))
        widget.setMaximumSize(QtCore.QSize(1600, 900))
        font = QtGui.QFont()
        font.setFamily("楷体")
        widget.setFont(font)
        icon = QtGui.QIcon.fromTheme("123213")
        widget.setWindowIcon(icon)
        widget.setStyleSheet("QWidget#Form{\n"
"border-image:url(:/detection/162247.jpg)\n"
"    }")
        self.tabWidget = QtWidgets.QTabWidget(widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1601, 901))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget_4 = QtWidgets.QWidget(self.tab)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 131, 851))
        self.widget_4.setStyleSheet("background-color:rgb(230,230,230);")
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 102, 791))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.xiangji = QtWidgets.QPushButton(self.layoutWidget)
        self.xiangji.setMinimumSize(QtCore.QSize(100, 50))
        self.xiangji.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.xiangji.setFont(font)
        self.xiangji.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.xiangji.setObjectName("xiangji")
        self.verticalLayout_2.addWidget(self.xiangji)
        self.path_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.path_2.setMinimumSize(QtCore.QSize(100, 50))
        self.path_2.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.path_2.setFont(font)
        self.path_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.path_2.setObjectName("path_2")
        self.verticalLayout_2.addWidget(self.path_2)
        self.moxing = QtWidgets.QPushButton(self.layoutWidget)
        self.moxing.setMinimumSize(QtCore.QSize(100, 50))
        self.moxing.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.moxing.setFont(font)
        self.moxing.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.moxing.setObjectName("moxing")
        self.verticalLayout_2.addWidget(self.moxing)
        self.kaishi = QtWidgets.QPushButton(self.layoutWidget)
        self.kaishi.setMinimumSize(QtCore.QSize(100, 50))
        self.kaishi.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.kaishi.setFont(font)
        self.kaishi.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }\n"
"QPushButton:checked\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(221, 0, 0);\n"
"}")
        self.kaishi.setCheckable(True)
        self.kaishi.setObjectName("kaishi")
        self.verticalLayout_2.addWidget(self.kaishi)
        self.suspend = QtWidgets.QPushButton(self.layoutWidget)
        self.suspend.setMinimumSize(QtCore.QSize(100, 50))
        self.suspend.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.suspend.setFont(font)
        self.suspend.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(240, 160, 40);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(250, 170, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0)\n"
"    }\n"
"QPushButton:checked{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0)\n"
"    }")
        self.suspend.setCheckable(True)
        self.suspend.setObjectName("suspend")
        self.verticalLayout_2.addWidget(self.suspend)
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setGeometry(QtCore.QRect(130, 0, 1471, 851))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setGeometry(QtCore.QRect(-41, 0, 51, 741))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_11 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 0, 621, 531))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.list = QtWidgets.QTableView(self.groupBox_11)
        self.list.setGeometry(QtCore.QRect(10, 20, 600, 500))
        self.list.setMinimumSize(QtCore.QSize(206, 200))
        self.list.setMaximumSize(QtCore.QSize(10000, 10000))
        self.list.setAlternatingRowColors(True)
        self.list.setShowGrid(True)
        self.list.setGridStyle(QtCore.Qt.DotLine)
        self.list.setSortingEnabled(True)
        self.list.setWordWrap(True)
        self.list.setCornerButtonEnabled(True)
        self.list.setObjectName("list")
        self.list.horizontalHeader().setCascadingSectionResizes(True)
        self.list.verticalHeader().setCascadingSectionResizes(False)
        self.groupBox_12 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 530, 621, 311))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.detail = QtWidgets.QTableView(self.groupBox_12)
        self.detail.setGeometry(QtCore.QRect(10, 20, 600, 240))
        self.detail.setMinimumSize(QtCore.QSize(206, 100))
        self.detail.setMaximumSize(QtCore.QSize(10000, 10000))
        self.detail.setAlternatingRowColors(True)
        self.detail.setShowGrid(True)
        self.detail.setGridStyle(QtCore.Qt.DotLine)
        self.detail.setSortingEnabled(True)
        self.detail.setWordWrap(True)
        self.detail.setCornerButtonEnabled(True)
        self.detail.setObjectName("detail")
        self.detail.horizontalHeader().setCascadingSectionResizes(True)
        self.detail.verticalHeader().setCascadingSectionResizes(False)
        self.label_2 = QtWidgets.QLabel(self.groupBox_12)
        self.label_2.setGeometry(QtCore.QRect(130, 270, 72, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_12)
        self.textBrowser.setGeometry(QtCore.QRect(190, 270, 270, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_8.setGeometry(QtCore.QRect(640, 0, 821, 841))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.tuxiang = QtWidgets.QGraphicsView(self.groupBox_8)
        self.tuxiang.setGeometry(QtCore.QRect(10, 20, 800, 400))
        self.tuxiang.setMinimumSize(QtCore.QSize(800, 400))
        self.tuxiang.setMaximumSize(QtCore.QSize(800, 700))
        self.tuxiang.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang.setObjectName("tuxiang")
        self.tuxiang_5 = QtWidgets.QGraphicsView(self.groupBox_8)
        self.tuxiang_5.setGeometry(QtCore.QRect(10, 430, 800, 400))
        self.tuxiang_5.setMinimumSize(QtCore.QSize(800, 400))
        self.tuxiang_5.setMaximumSize(QtCore.QSize(800, 700))
        self.tuxiang_5.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang_5.setObjectName("tuxiang_5")
        self.line_2 = QtWidgets.QFrame(self.groupBox_8)
        self.line_2.setGeometry(QtCore.QRect(0, 415, 821, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_9 = QtWidgets.QWidget(self.tab_3)
        self.widget_9.setGeometry(QtCore.QRect(130, 0, 1461, 861))
        self.widget_9.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.groupBox_13 = QtWidgets.QGroupBox(self.widget_9)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 0, 621, 531))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.list_2 = QtWidgets.QTableView(self.groupBox_13)
        self.list_2.setGeometry(QtCore.QRect(10, 20, 600, 500))
        self.list_2.setMinimumSize(QtCore.QSize(206, 200))
        self.list_2.setMaximumSize(QtCore.QSize(10000, 10000))
        self.list_2.setAlternatingRowColors(True)
        self.list_2.setShowGrid(True)
        self.list_2.setGridStyle(QtCore.Qt.DotLine)
        self.list_2.setSortingEnabled(True)
        self.list_2.setWordWrap(True)
        self.list_2.setCornerButtonEnabled(True)
        self.list_2.setObjectName("list_2")
        self.list_2.horizontalHeader().setCascadingSectionResizes(True)
        self.list_2.verticalHeader().setCascadingSectionResizes(False)
        self.groupBox_14 = QtWidgets.QGroupBox(self.widget_9)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 530, 621, 311))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setObjectName("groupBox_14")
        self.detail_2 = QtWidgets.QTableView(self.groupBox_14)
        self.detail_2.setGeometry(QtCore.QRect(10, 20, 600, 240))
        self.detail_2.setMinimumSize(QtCore.QSize(206, 200))
        self.detail_2.setMaximumSize(QtCore.QSize(10000, 10000))
        self.detail_2.setAlternatingRowColors(True)
        self.detail_2.setShowGrid(True)
        self.detail_2.setGridStyle(QtCore.Qt.DotLine)
        self.detail_2.setSortingEnabled(True)
        self.detail_2.setWordWrap(True)
        self.detail_2.setCornerButtonEnabled(True)
        self.detail_2.setObjectName("detail_2")
        self.detail_2.horizontalHeader().setCascadingSectionResizes(True)
        self.detail_2.verticalHeader().setCascadingSectionResizes(False)
        self.label_3 = QtWidgets.QLabel(self.groupBox_14)
        self.label_3.setGeometry(QtCore.QRect(130, 275, 60, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_14)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 270, 270, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget_9)
        self.groupBox_7.setGeometry(QtCore.QRect(640, 0, 821, 841))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.tuxiang_2 = QtWidgets.QGraphicsView(self.groupBox_7)
        self.tuxiang_2.setGeometry(QtCore.QRect(10, 20, 800, 400))
        self.tuxiang_2.setMinimumSize(QtCore.QSize(800, 400))
        self.tuxiang_2.setMaximumSize(QtCore.QSize(800, 700))
        self.tuxiang_2.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang_2.setObjectName("tuxiang_2")
        self.tuxiang_6 = QtWidgets.QGraphicsView(self.groupBox_7)
        self.tuxiang_6.setGeometry(QtCore.QRect(10, 430, 800, 400))
        self.tuxiang_6.setMinimumSize(QtCore.QSize(800, 400))
        self.tuxiang_6.setMaximumSize(QtCore.QSize(800, 700))
        self.tuxiang_6.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang_6.setObjectName("tuxiang_6")
        self.line_3 = QtWidgets.QFrame(self.groupBox_7)
        self.line_3.setGeometry(QtCore.QRect(0, 410, 821, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.groupBox_14.raise_()
        self.groupBox_7.raise_()
        self.groupBox_13.raise_()
        self.widget_10 = QtWidgets.QWidget(self.tab_3)
        self.widget_10.setGeometry(QtCore.QRect(0, 0, 131, 851))
        self.widget_10.setMaximumSize(QtCore.QSize(131, 851))
        self.widget_10.setStyleSheet("background-color:rgb(230,230, 230);")
        self.widget_10.setObjectName("widget_10")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_10)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 102, 781))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file = QtWidgets.QPushButton(self.layoutWidget1)
        self.file.setMinimumSize(QtCore.QSize(100, 50))
        self.file.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.file.setFont(font)
        self.file.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.file.setObjectName("file")
        self.verticalLayout.addWidget(self.file)
        self.moxing_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.moxing_2.setMinimumSize(QtCore.QSize(100, 50))
        self.moxing_2.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.moxing_2.setFont(font)
        self.moxing_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.moxing_2.setObjectName("moxing_2")
        self.verticalLayout.addWidget(self.moxing_2)
        self.kaishi_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.kaishi_2.setMinimumSize(QtCore.QSize(100, 50))
        self.kaishi_2.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.kaishi_2.setFont(font)
        self.kaishi_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }\n"
"QPushButton:checked\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(221, 0, 0);\n"
"}")
        self.kaishi_2.setCheckable(True)
        self.kaishi_2.setObjectName("kaishi_2")
        self.verticalLayout.addWidget(self.kaishi_2)
        self.suspend_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.suspend_2.setMinimumSize(QtCore.QSize(100, 50))
        self.suspend_2.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.suspend_2.setFont(font)
        self.suspend_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(240, 160, 40);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(250, 170, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0)\n"
"    }\n"
"QPushButton:checked{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0)\n"
"    }")
        self.suspend_2.setCheckable(True)
        self.suspend_2.setObjectName("suspend_2")
        self.verticalLayout.addWidget(self.suspend_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_5 = QtWidgets.QWidget(self.tab_4)
        self.widget_5.setGeometry(QtCore.QRect(130, 0, 1461, 851))
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_5)
        self.groupBox_4.setGeometry(QtCore.QRect(640, 0, 821, 841))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tuxiang_3 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.tuxiang_3.setGeometry(QtCore.QRect(10, 20, 800, 810))
        self.tuxiang_3.setMinimumSize(QtCore.QSize(800, 800))
        self.tuxiang_3.setMaximumSize(QtCore.QSize(800, 850))
        self.tuxiang_3.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang_3.setObjectName("tuxiang_3")
        self.groupBox_15 = QtWidgets.QGroupBox(self.widget_5)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 0, 621, 681))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.list_3 = QtWidgets.QTableView(self.groupBox_15)
        self.list_3.setGeometry(QtCore.QRect(10, 20, 600, 651))
        self.list_3.setMinimumSize(QtCore.QSize(206, 200))
        self.list_3.setMaximumSize(QtCore.QSize(10000, 10000))
        self.list_3.setAlternatingRowColors(True)
        self.list_3.setShowGrid(True)
        self.list_3.setGridStyle(QtCore.Qt.DotLine)
        self.list_3.setSortingEnabled(True)
        self.list_3.setWordWrap(True)
        self.list_3.setCornerButtonEnabled(True)
        self.list_3.setObjectName("list_3")
        self.list_3.horizontalHeader().setCascadingSectionResizes(True)
        self.list_3.verticalHeader().setCascadingSectionResizes(False)
        self.groupBox_16 = QtWidgets.QGroupBox(self.widget_5)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 680, 621, 161))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.detail_3 = QtWidgets.QTableView(self.groupBox_16)
        self.detail_3.setGeometry(QtCore.QRect(9, 20, 601, 91))
        self.detail_3.setMinimumSize(QtCore.QSize(206, 20))
        self.detail_3.setMaximumSize(QtCore.QSize(10000, 10000))
        self.detail_3.setAlternatingRowColors(True)
        self.detail_3.setShowGrid(True)
        self.detail_3.setGridStyle(QtCore.Qt.DotLine)
        self.detail_3.setSortingEnabled(True)
        self.detail_3.setWordWrap(True)
        self.detail_3.setCornerButtonEnabled(True)
        self.detail_3.setObjectName("detail_3")
        self.detail_3.horizontalHeader().setCascadingSectionResizes(True)
        self.detail_3.verticalHeader().setCascadingSectionResizes(False)
        self.label_6 = QtWidgets.QLabel(self.groupBox_16)
        self.label_6.setGeometry(QtCore.QRect(130, 120, 72, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_16)
        self.textBrowser_3.setGeometry(QtCore.QRect(190, 120, 270, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.widget_8 = QtWidgets.QWidget(self.tab_4)
        self.widget_8.setGeometry(QtCore.QRect(0, 0, 131, 851))
        self.widget_8.setStyleSheet("background-color:rgb(230, 230, 230);")
        self.widget_8.setObjectName("widget_8")
        self.layoutWidget2 = QtWidgets.QWidget(self.widget_8)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 102, 781))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.xiangji_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.xiangji_3.setMinimumSize(QtCore.QSize(100, 50))
        self.xiangji_3.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.xiangji_3.setFont(font)
        self.xiangji_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.xiangji_3.setObjectName("xiangji_3")
        self.verticalLayout_3.addWidget(self.xiangji_3)
        self.path = QtWidgets.QPushButton(self.layoutWidget2)
        self.path.setMinimumSize(QtCore.QSize(100, 50))
        self.path.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.path.setFont(font)
        self.path.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }")
        self.path.setObjectName("path")
        self.verticalLayout_3.addWidget(self.path)
        self.kaishi_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.kaishi_3.setMinimumSize(QtCore.QSize(100, 50))
        self.kaishi_3.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.kaishi_3.setFont(font)
        self.kaishi_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(85, 200, 0)\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 0, 0)\n"
"    }\n"
"QPushButton:checked\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(221, 0, 0);\n"
"}")
        self.kaishi_3.setCheckable(True)
        self.kaishi_3.setObjectName("kaishi_3")
        self.verticalLayout_3.addWidget(self.kaishi_3)
        self.suspend_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.suspend_3.setMinimumSize(QtCore.QSize(100, 50))
        self.suspend_3.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.suspend_3.setFont(font)
        self.suspend_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(240, 160, 40);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(250, 170, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0)\n"
"    }\n"
"QPushButton:checked{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 0)\n"
"    }")
        self.suspend_3.setCheckable(True)
        self.suspend_3.setObjectName("suspend_3")
        self.verticalLayout_3.addWidget(self.suspend_3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_6 = QtWidgets.QWidget(self.tab_2)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 181, 851))
        self.widget_6.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.widget_6.setObjectName("widget_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit.setGeometry(QtCore.QRect(10, 400, 160, 40))
        self.lineEdit.setMinimumSize(QtCore.QSize(160, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 90, 30))
        self.label_4.setMinimumSize(QtCore.QSize(90, 30))
        self.label_4.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.find = QtWidgets.QPushButton(self.widget_6)
        self.find.setGeometry(QtCore.QRect(40, 570, 80, 40))
        self.find.setMinimumSize(QtCore.QSize(80, 40))
        self.find.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.find.setFont(font)
        self.find.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(200, 200, 200);\n"
"    border-radius:10px\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgb(225, 225, 225);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgb(225, 225, 225);\n"
"    }")
        self.find.setObjectName("find")
        self.label = QtWidgets.QLabel(self.widget_6)
        self.label.setGeometry(QtCore.QRect(10, 190, 90, 30))
        self.label.setMinimumSize(QtCore.QSize(90, 30))
        self.label.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setGeometry(QtCore.QRect(10, 280, 90, 30))
        self.label_8.setMinimumSize(QtCore.QSize(90, 30))
        self.label_8.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget_6)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 220, 160, 40))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 11), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.widget_6)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(10, 310, 160, 40))
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 11), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 490, 160, 40))
        self.comboBox_2.setMinimumSize(QtCore.QSize(160, 40))
        self.comboBox_2.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        self.label_9.setGeometry(QtCore.QRect(10, 460, 90, 30))
        self.label_9.setMinimumSize(QtCore.QSize(90, 30))
        self.label_9.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.widget_7 = QtWidgets.QWidget(self.tab_2)
        self.widget_7.setGeometry(QtCore.QRect(180, 0, 1411, 851))
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_7)
        self.groupBox_3.setGeometry(QtCore.QRect(630, 0, 781, 841))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tuxiang_4 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.tuxiang_4.setGeometry(QtCore.QRect(10, 20, 760, 400))
        self.tuxiang_4.setMinimumSize(QtCore.QSize(500, 400))
        self.tuxiang_4.setMaximumSize(QtCore.QSize(8000, 400))
        self.tuxiang_4.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang_4.setObjectName("tuxiang_4")
        self.tuxiang_7 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.tuxiang_7.setGeometry(QtCore.QRect(10, 430, 760, 400))
        self.tuxiang_7.setMinimumSize(QtCore.QSize(760, 400))
        self.tuxiang_7.setMaximumSize(QtCore.QSize(800, 400))
        self.tuxiang_7.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tuxiang_7.setObjectName("tuxiang_7")
        self.line_4 = QtWidgets.QFrame(self.groupBox_3)
        self.line_4.setGeometry(QtCore.QRect(0, 410, 821, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.groupBox_17 = QtWidgets.QGroupBox(self.widget_7)
        self.groupBox_17.setGeometry(QtCore.QRect(0, 0, 621, 531))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setObjectName("groupBox_17")
        self.list_4 = QtWidgets.QTableView(self.groupBox_17)
        self.list_4.setGeometry(QtCore.QRect(10, 20, 600, 500))
        self.list_4.setMinimumSize(QtCore.QSize(206, 200))
        self.list_4.setMaximumSize(QtCore.QSize(10000, 10000))
        self.list_4.setAlternatingRowColors(True)
        self.list_4.setShowGrid(True)
        self.list_4.setGridStyle(QtCore.Qt.DotLine)
        self.list_4.setSortingEnabled(True)
        self.list_4.setWordWrap(True)
        self.list_4.setCornerButtonEnabled(True)
        self.list_4.setObjectName("list_4")
        self.list_4.horizontalHeader().setCascadingSectionResizes(True)
        self.list_4.verticalHeader().setCascadingSectionResizes(False)
        self.groupBox_18 = QtWidgets.QGroupBox(self.widget_7)
        self.groupBox_18.setGeometry(QtCore.QRect(0, 530, 621, 311))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.detail_4 = QtWidgets.QTableView(self.groupBox_18)
        self.detail_4.setGeometry(QtCore.QRect(10, 20, 600, 240))
        self.detail_4.setMinimumSize(QtCore.QSize(0, 0))
        self.detail_4.setMaximumSize(QtCore.QSize(10000, 10000))
        self.detail_4.setAlternatingRowColors(True)
        self.detail_4.setShowGrid(True)
        self.detail_4.setGridStyle(QtCore.Qt.DotLine)
        self.detail_4.setSortingEnabled(True)
        self.detail_4.setWordWrap(True)
        self.detail_4.setCornerButtonEnabled(True)
        self.detail_4.setObjectName("detail_4")
        self.detail_4.horizontalHeader().setCascadingSectionResizes(True)
        self.detail_4.verticalHeader().setCascadingSectionResizes(False)
        self.label_7 = QtWidgets.QLabel(self.groupBox_18)
        self.label_7.setGeometry(QtCore.QRect(130, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_18)
        self.textBrowser_4.setGeometry(QtCore.QRect(190, 270, 270, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(8)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_17 = QtWidgets.QLabel(widget)
        self.label_17.setGeometry(QtCore.QRect(1310, 0, 291, 51))
        self.label_17.setMinimumSize(QtCore.QSize(120, 30))
        self.label_17.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.retranslateUi(widget)
        self.tabWidget.setCurrentIndex(0)
        self.xiangji.clicked['bool'].connect(widget.camera_clicked)
        self.path_2.clicked['bool'].connect(widget.save_clicked)
        self.moxing.clicked['bool'].connect(widget.model_clicked)
        self.kaishi.clicked['bool'].connect(widget.detect_start_clicked)
        self.suspend.clicked['bool'].connect(widget.suspend_clicked)
        self.file.clicked['bool'].connect(widget.file_clicked)
        self.moxing_2.clicked['bool'].connect(widget.model_clicked)
        self.kaishi_2.clicked['bool'].connect(widget.local_start_clicked)
        self.suspend_2.clicked['bool'].connect(widget.suspend2_clicked)
        self.xiangji_3.clicked['bool'].connect(widget.camera_clicked)
        self.path.clicked['bool'].connect(widget.save_clicked)
        self.kaishi_3.clicked['bool'].connect(widget.collect_start_clicked)
        self.suspend_3.clicked['bool'].connect(widget.suspend3_clicked)
        self.find.clicked['bool'].connect(widget.find_clicked)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "中密度纤维板表面缺陷检测软件"))
        self.xiangji.setText(_translate("widget", "参数设置"))
        self.path_2.setText(_translate("widget", "保存路径"))
        self.moxing.setText(_translate("widget", "模型选择"))
        self.kaishi.setText(_translate("widget", "开始/结束"))
        self.suspend.setText(_translate("widget", "暂停/继续"))
        self.groupBox_11.setTitle(_translate("widget", "已检列表"))
        self.groupBox_12.setTitle(_translate("widget", "检测详情"))
        self.label_2.setText(_translate("widget", "文件名称"))
        self.groupBox_8.setTitle(_translate("widget", "检测结果预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("widget", "实时检测"))
        self.groupBox_13.setTitle(_translate("widget", "已检列表"))
        self.groupBox_14.setTitle(_translate("widget", "检测详情"))
        self.label_3.setText(_translate("widget", "文件名称"))
        self.groupBox_7.setTitle(_translate("widget", "检测结果预览"))
        self.file.setText(_translate("widget", "文件选择"))
        self.moxing_2.setText(_translate("widget", "模型选择"))
        self.kaishi_2.setText(_translate("widget", "开始/结束"))
        self.suspend_2.setText(_translate("widget", "暂停/继续"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("widget", "本地检测"))
        self.groupBox_4.setTitle(_translate("widget", "图像采集预览"))
        self.groupBox_15.setTitle(_translate("widget", "已采列表"))
        self.groupBox_16.setTitle(_translate("widget", "图片详情"))
        self.label_6.setText(_translate("widget", "文件名称"))
        self.xiangji_3.setText(_translate("widget", "参数设置"))
        self.path.setText(_translate("widget", "保存路径"))
        self.kaishi_3.setText(_translate("widget", "开始/结束"))
        self.suspend_3.setText(_translate("widget", "暂停/继续"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("widget", "图像采集"))
        self.label_4.setText(_translate("widget", "图片名称"))
        self.find.setText(_translate("widget", "查询"))
        self.label.setText(_translate("widget", "<html><head/><body><p>起始日期<span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.label_8.setText(_translate("widget", "<html><head/><body><p>结束日期<span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.comboBox_2.setItemText(1, _translate("widget", "实时检测"))
        self.comboBox_2.setItemText(2, _translate("widget", "本地检测"))
        self.label_9.setText(_translate("widget", "<html><head/><body><p>工作模式</p></body></html>"))
        self.groupBox_3.setTitle(_translate("widget", "检测结果预览"))
        self.groupBox_17.setTitle(_translate("widget", "已检列表"))
        self.groupBox_18.setTitle(_translate("widget", "检测详情"))
        self.label_7.setText(_translate("widget", "文件名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("widget", "历史查询"))
        self.label_17.setText(_translate("widget", "机器视觉与人工智能实验室\n"
"Machine Vision and Aitificial Intelligence Laboratory\n"
"                                              北京林业大学----工学院"))
import images_rc
