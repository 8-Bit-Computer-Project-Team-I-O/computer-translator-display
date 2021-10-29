# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from random import random

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import socket
import interpreter
from EmulatorGUI import GPIO



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 800)
        Form.setMinimumSize(QtCore.QSize(900, 800))
        Form.setMaximumSize(QtCore.QSize(900, 800))

        #Background
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(-30, 0, 981, 831))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet("background-color: rgb(10, 10, 25);")
        self.graphicsView.setObjectName("graphicsView")


        #Bus
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(330, 50, 211, 101))
        self.textBrowser.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser.setObjectName("textBrowser")

        #Bus LCD
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(350, 100, 171, 41))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_3.setDigitCount(8)



        #Ram
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 310, 211, 101))
        self.textBrowser_2.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_2.setObjectName("textBrowser_2")



        #Clock
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 170, 211, 91))
        self.textBrowser_3.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_3.setObjectName("textBrowser_3")



        #Program Counter
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(600, 160, 221, 101))
        self.textBrowser_5.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_5.setObjectName("textBrowser_5")

        #Program Counter LCD
        self.lcdNumber_5 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_5.setGeometry(QtCore.QRect(640, 210, 131, 41))
        self.lcdNumber_5.setObjectName("lcdNumber_5")



        #Memory
        self.textBrowser_7 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_7.setGeometry(QtCore.QRect(60, 460, 211, 101))
        self.textBrowser_7.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_7.setObjectName("textBrowser_7")




        #Cancel button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 171, 71))
        self.pushButton.setStyleSheet(" QPushButton#pushButton {\n"
        "     background-color: rgba(30, 30, 30, 250);\n"
        "     \n"
        " }\n"
        " QPushButton#pushButton:pressed {\n"
        "     background-color: rgb(224, 0, 0);     \n"
        " }\n"
        " QPushButton#pushButton:hover {\n"
        "     \n"
        "    font: 12pt \"MS Shell Dlg 2\";\n"
        "    background-color: rgb(156, 0, 0);\n"
        "    \n"
        " }\n"
        "\n"
        "")
        self.pushButton.setObjectName("pushButton")


        #Text Display
        self.textBrowser_9 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_9.setGeometry(QtCore.QRect(290, 600, 431, 131))
        self.textBrowser_9.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.textBrowser_9.setObjectName("textBrowser_9")


        #Instruction Register
        self.textBrowser_10 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_10.setGeometry(QtCore.QRect(60, 610, 211, 101))
        self.textBrowser_10.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_10.setObjectName("textBrowser_10")


        #Flag register
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(730, 610, 151, 91))
        self.textEdit.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textEdit.setObjectName("textEdit")

        #Flag check boxes
        self.Carry_Flag = QtWidgets.QCheckBox(Form)
        self.Carry_Flag.setEnabled(True)
        self.Carry_Flag.setGeometry(QtCore.QRect(800, 640, 81, 20))
        self.Carry_Flag.setText("")
        self.Carry_Flag.setChecked(False)
        self.Carry_Flag.setObjectName("Carry_Flag")
        self.Zero_Flag = QtWidgets.QCheckBox(Form)
        self.Zero_Flag.setGeometry(QtCore.QRect(800, 660, 81, 20))
        self.Zero_Flag.setText("")
        self.Zero_Flag.setChecked(False)
        self.Zero_Flag.setObjectName("Zero_Flag")



        #ALU Frame
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(410, 270, 481, 301))
        self.groupBox.setStyleSheet("background-color: rgba(107, 135, 85, 100);")
        self.groupBox.setObjectName("groupBox")


        #Register A
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_4.setGeometry(QtCore.QRect(260, 30, 211, 111))
        self.textBrowser_4.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_4.setObjectName("textBrowser_4")

        #Register A LCD
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_4.setGeometry(QtCore.QRect(280, 90, 171, 41))
        self.lcdNumber_4.setObjectName("lcdNumber_4")



        #Register B
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_6.setGeometry(QtCore.QRect(260, 170, 211, 111))
        self.textBrowser_6.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_6.setObjectName("textBrowser_6")

        #Register B LCD
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_2.setGeometry(QtCore.QRect(280, 230, 171, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setDigitCount(8)



        #Output Register
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_8.setGeometry(QtCore.QRect(20, 100, 201, 111))
        self.textBrowser_8.setStyleSheet("background-color: rgba(107, 107, 107, 150);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)


        #Output Register LCD
        self.lcdNumber.setGeometry(QtCore.QRect(40, 160, 161, 41))
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setObjectName("lcdNumber")




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

       #Bus
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Bus</span></p></body></html>"))

       #RAM
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">RAM</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600; color:#ffffff;\"><br /></p></body></html>"))

       #Clock
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Clock</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">No Power</span></p></body></html>"))

       #Program Counter
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff; vertical-align:super;\">Program Counter</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

       #Memory
        self.textBrowser_7.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Memory</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        #Cancel button
        self.pushButton.setText(_translate("Form", "Cancel"))


        #Text Display
        self.textBrowser_9.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Text Displays here.</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

        #Instruction Register
        self.textBrowser_10.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Instruction Register</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        #Flag Register
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Flag Register</span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\"> Carry:</span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">  Zero:</span></p></body></html>"))

        #Group box
        self.groupBox.setTitle(_translate("Form", "Arithmetic Logic Unit"))
        #Attempt to change title font color -   self.groupBox.setStyleSheet('QgroupBox:title {color: green;}')


        #Register B
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Register B</span></p>\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        #Register A
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Register A</span></p>\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        #Output
        self.textBrowser_8.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Output</span></p></body></html>"))


def set_up_connection(source, ui):
    # establish the base variables
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 9999))
    s.listen(1)
    # if BE architecture, we're going to get stuff from the GPIO pins, then do the interpretation in a forever loop. Add some sort of exception later
    if (source == "True"):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.IN)
        GPIO.setup(16, GPIO.IN)
        GPIO.setup(12, GPIO.IN)
        GPIO.setup(4, GPIO.IN)
        GPIO.setup(7, GPIO.IN)
        GPIO.setup(8, GPIO.IN)
        GPIO.setup(25, GPIO.IN)
        GPIO.setup(23, GPIO.IN)
        GPIO.setup(10,GPIO.IN)
        while True:
            bus_Val=str(int(GPIO.input(23)))+str(int(GPIO.input(25)))+str(int(GPIO.input(8)))+str(int(GPIO.input(7)))+str(int(GPIO.input(4)))+str(int(GPIO.input(12)))+str(int(GPIO.input(16)))+str(int(GPIO.input(20)))
            clock_Val=GPIO.input(10)
            mcVal="0000000000000000"
            valsArr=[clock_Val,bus_Val,mcVal]
            ui.lcdNumber_3.display(valsArr[1])
            QtCore.QCoreApplication.processEvents()
    # same as BE architecture except we're getting the connection from a Java program
    else:
        sock = socket.create_connection(("", 9999))
        conn, addr = s.accept()
        conn, addr = s.accept()
        while True:
            data = conn.recv(4096)
            allValues = data.decode('utf-8').split('#')




            #Constants
            #Bus
            ui.lcdNumber_3.display(allValues[1])

            #Clock
            ui.textBrowser_3.setHtml(QtCore.QCoreApplication.translate("Form",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Clock</span></p>\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Low Epoch</span></p></body></html>"))
            if allValues[0] == "1":
                ui.textBrowser_3.setStyleSheet(
                    QtCore.QCoreApplication.translate("form", "background-color: rgb(255, 255, 204);"))
                ui.textBrowser_3.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">Clock</span></p>\n"
                                                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">High Epoch</span></p></body></html>"))
            else:
                ui.textBrowser_3.setStyleSheet(QtCore.QCoreApplication.translate("form","background-color: rgba(107, 107, 107, 150);"))




            #Switch statement begins









            #memory
       #    ui.textBrowser_7.setHtml(QtCore.QCoreApplication.translate("Form",
        #                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
         #                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
          #                                        "p, li { white-space: pre-wrap; }\n"
           #                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            #                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
             #                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Memory</span></p>\n"
              #                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">"+allValues[2]+"</span></p></body></html>"))












            QtCore.QCoreApplication.processEvents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    # make a file reader
    f = open('data.json', )
    # load the json values into a variable
    json_vals = json.load(f)
    set_up_connection(json_vals["BE Architecture"], ui)
    sys.exit(app.exec_())