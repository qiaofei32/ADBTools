#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Joe
# datetime:2018/11/11 11:52
# software: ADBTool-Capture
import re
import os
import sys
import Image
from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)


HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head>
			<meta name="qrichtext" content="1" />
			<style type="text/css">
				p, li { white-space: pre-wrap; }
			</style>
		</head>
		<body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;"><p><img src="screenshot.png" width="%d" height="%d" /></p></body>
	</html>
	"""

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(455, 860)
		MainWindow.setMinimumSize(QtCore.QSize(455, 860))
		MainWindow.setMaximumSize(QtCore.QSize(455, 860))
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
		self.textBrowser.setEnabled(False)
		self.textBrowser.setGeometry(QtCore.QRect(0, 50, 450, 810))
		self.textBrowser.setMinimumSize(QtCore.QSize(378, 790))
		self.textBrowser.setMaximumSize(QtCore.QSize(480, 820))
		self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
		self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
		self.textBrowser.setLineWidth(0)
		self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(110, 4, 65, 38))
		self.pushButton.setMinimumSize(QtCore.QSize(59, 38))
		self.pushButton.setMaximumSize(QtCore.QSize(120, 38))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton.setFont(font)
		self.pushButton.setStyleSheet(_fromUtf8(""))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.lineEdit = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(369, 5, 80, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lineEdit.setFont(font)
		self.lineEdit.setText(_fromUtf8(""))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(325, 10, 46, 25))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(240, 5, 80, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(180, 10, 62, 25))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.checkBox = QtGui.QCheckBox(self.centralwidget)
		self.checkBox.setGeometry(QtCore.QRect(10, 10, 90, 28))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.checkBox.setFont(font)
		self.checkBox.setObjectName(_fromUtf8("checkBox"))
		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(0, 40, 451, 20))
		self.label_3.setObjectName(_fromUtf8("label_3"))

		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(0, 50, 450, 810))
		self.label_4.setObjectName(_fromUtf8(""))

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.textBrowser.setHtml(_translate("MainWindow",
											"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
											"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
											"p, li { white-space: pre-wrap; }\n"
											"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
											"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"screenshot.png\" width=\"450\" height=\"800\" /></p></body></html>",
											None))
		self.pushButton.setText(_translate("MainWindow", "截屏", None))
		self.label.setText(_translate("MainWindow", "坐标：", None))
		self.lineEdit_2.setText(_translate("MainWindow", "1920*1080", None))
		self.label_2.setText(_translate("MainWindow", "分辨率：", None))
		self.checkBox.setText(_translate("MainWindow", "横屏模式", None))
		self.label_3.setText(_translate("MainWindow", "-----------------------------------------------------------------------------", None))

		self.rotation = False
		self.ratio = 450.0 / 1080
		im = Image.open("screenshot.png")
		self.width, self.height = im.size

		self.pushButton.clicked.connect(self.screenshot)
		self.checkBox.stateChanged.connect(self.rotate)

	def mousePressEvent(self, QMouseEvent):
		pos = QMouseEvent.pos()
		x, y = pos.x(), pos.y()-49

		if not self.rotation:
			x1, y1 = int(x / self.ratio), int(y / self.ratio)
		else:
			x1 = self.height - int(y / self.ratio)
			y1 = int(x / self.ratio)

		x1 = x1 if x1 > 0 else 0
		y1 = y1 if y1 > 0 else 0

		# print "{} {} ---> {} {}".format(x, y, x1, y1)

		self.lineEdit.setText(_translate("MainWindow", "{},{}".format(x1, y1), None))

	def rotate(self, *args):
		self.rotation = self.checkBox.isChecked()
		im = Image.open("screenshot.png")
		self.width, self.height = im.size

	def screenshot(self):
		# print "screenshot"

		if self.rotation:
			im = Image.open("screenshot.png")
			im_rotate = im.rotate(90)
			im_rotate.save("screenshot.png")

		im = Image.open("screenshot.png")
		width, height = im.size
		self.width = width
		self.height = height

		self.lineEdit_2.setText(_translate("MainWindow", "{}*{}".format(height, width), None))

		self.ratio = 450.0 / width
		width_show, height_show = 450, int(self.ratio * height)

		# print width_show, height_show
		html = HTML % (width_show, height_show)
		html = re.sub("\s+", " ", html)
		self.textBrowser.setHtml(_translate("MainWindow", html, None))

class ADBCaptute(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

app = QtGui.QApplication(sys.argv)
win = ADBCaptute()
win.show()
sys.exit(app.exec_())
