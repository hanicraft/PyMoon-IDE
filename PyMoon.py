
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import os
import subprocess
import webbrowser

class LuaSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.highlightRules = []

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordPatterns = [
            "\\band\\b", "\\bbreak\\b", "\\bdo\\b", "\\belse\\b",
            "\\belseif\\b", "\\bend\\b", "\\bfalse\\b", "\\bfor\\b",
            "\\bfunction\\b", "\\bif\\b", "\\bin\\b", "\\blocal\\b",
            "\\bnil\\b", "\\bnot\\b", "\\bor\\b", "\\brepeat\\b",
            "\\breturn\\b", "\\bthen\\b", "\\btrue\\b", "\\buntil\\b",
            "\\bwhile\\b"
        ]
        for pattern in keywordPatterns:
            rule = QRegularExpression("\\b" + pattern + "\\b")
            self.highlightRules.append((rule, keywordFormat))

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightRules.append((QRegularExpression("\".*\""), quotationFormat))
        self.highlightRules.append((QRegularExpression("'.*'"), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setForeground(Qt.darkCyan)
        self.highlightRules.append((QRegularExpression("\\b[A-Za-z0-9_]+(?=\\()"), functionFormat))

        self.text1Format = QTextCharFormat()
        self.text1Format.setFontPointSize(24)
        self.text1Format.setForeground(Qt.red)

    def highlightBlock(self, text):
        for rule, format in self.highlightRules:
            iterator = rule.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

        index = text.indexOf("text1")
        while index >= 0:
            self.setFormat(index, 5, self.text1Format)
            index = text.indexOf("text1", index + 1)


class Widget1(QWidget):
    def __init__(self, parent=None):
        super(Widget1, self).__init__(parent)
        self.gui()
        self.highlighter = LuaSyntaxHighlighter(self.text1.document())

    def gui(self):
        self.w1 = self
        self.w1.setAutoFillBackground(True)
        self.w1.setWindowTitle("PyMoon IDE Version 1.0 by Mohamad Hani Janaty")
        self.w1.resize(650, 600)
        palette = self.w1.palette()
        palette.setColor(self.w1.backgroundRole(), QColor(44, 44, 44, 255))
        self.w1.setPalette(palette)
        self.w1.setCursor(Qt.ArrowCursor)
        self.w1.setToolTip("")
        self.text1 = QPlainTextEdit(self.w1)
        self.text1.setPlainText("")
        self.text1.move(10, 120)
        self.text1.resize(510, 370)
        self.text1.setStyleSheet("background-color: #414141; color: #c0c0c0;")
        self.text1.setCursor(Qt.ArrowCursor)
        self.text1.setToolTip("")
        self.group1 = QGroupBox(self.w1)
        self.group1.setAutoFillBackground(True)
        self.group1.setTitle("Visual Lua Component")
        self.group1.move(520, 120)
        self.group1.resize(130, 170)
        palette = self.group1.palette()
        palette.setColor(self.group1.backgroundRole(), QColor(129, 129, 129, 255))
        self.group1.setPalette(palette)
        self.group1.setCursor(Qt.ArrowCursor)
        self.group1.setToolTip("")
        self.button7 = QToolButton(self.group1)
        self.button7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button7.setText("Function")
        self.button7.move(0, 20)
        self.button7.resize(60, 22)
        self.button7.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button7.setCursor(Qt.ArrowCursor)
        self.button7.setToolTip("")
        self.button7.clicked.connect(self.addfunc)
        self.button8 = QToolButton(self.group1)
        self.button8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button8.setText("If Else")
        self.button8.move(70, 20)
        self.button8.resize(60, 22)
        self.button8.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button8.setCursor(Qt.ArrowCursor)
        self.button8.setToolTip("")
        self.button8.clicked.connect(self.addifelse)
        self.button9 = QToolButton(self.group1)
        self.button9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button9.setText("Local")
        self.button9.move(0, 60)
        self.button9.resize(60, 22)
        self.button9.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button9.setCursor(Qt.ArrowCursor)
        self.button9.setToolTip("")
        self.button9.clicked.connect(self.addlocal)
        self.button10 = QToolButton(self.group1)
        self.button10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button10.setText("Table")
        self.button10.move(70, 60)
        self.button10.resize(60, 22)
        self.button10.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button10.setCursor(Qt.ArrowCursor)
        self.button10.setToolTip("")
        self.button10.clicked.connect(self.addtable)
        self.button11 = QToolButton(self.group1)
        self.button11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button11.setText("Print")
        self.button11.move(0, 100)
        self.button11.resize(60, 22)
        self.button11.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button11.setCursor(Qt.ArrowCursor)
        self.button11.setToolTip("")
        self.button11.clicked.connect(self.addprint)
        self.button14 = QToolButton(self.group1)
        self.button14.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button14.setText("Require")
        self.button14.move(70, 100)
        self.button14.resize(60, 22)
        self.button14.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button14.setCursor(Qt.ArrowCursor)
        self.button14.setToolTip("")
        self.button14.clicked.connect(self.addrequire)
        self.tab1 = QTabWidget(self.w1)
        self.tab1.move(10, 0)
        self.tab1.resize(480, 120)
        self.tab1.setTabPosition(QTabWidget.North)
        palette = self.tab1.palette()
        palette.setColor(self.tab1.backgroundRole(), QColor(80, 80, 80, 255))
        self.tab1.setPalette(palette)
        self.tab1.setCursor(Qt.ArrowCursor)
        self.tab1.setToolTip("")
        self.ta1 = QWidget(self.tab1)
        self.ta1.setAutoFillBackground(True)
        self.ta1.setWindowTitle("")
        self.ta1.move(0, 0)
        self.ta1.resize(476, 93)
        palette = self.ta1.palette()
        palette.setColor(self.ta1.backgroundRole(), QColor(80, 80, 80, 255))
        self.ta1.setPalette(palette)
        self.ta1.setCursor(Qt.ArrowCursor)
        self.ta1.setToolTip("")
        self.openbtn = QToolButton(self.ta1)
        self.openbtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.openbtn.setText("")
        openbtn_pixmap = QPixmap("Oxygen-Icons.org-Oxygen-Places-folder-blue.256.png")
        self.openbtn.setAutoRaise(True)
        self.openbtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.openbtn.setIconSize(openbtn_pixmap.size())
        self.openbtn.setIcon(QIcon(openbtn_pixmap))
        self.openbtn.move(8, 6)
        self.openbtn.resize(90, 52)
        self.openbtn.setCursor(Qt.ArrowCursor)
        self.openbtn.setToolTip("")
        self.openbtn.clicked.connect(self.openfile)
        self.button5 = QToolButton(self.ta1)
        self.button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button5.setText("Save")
        button5_pixmap = QPixmap("Iconmoon-Web-Application-Load.48.png")
        self.button5.setAutoRaise(True)
        self.button5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button5.setIconSize(button5_pixmap.size())
        self.button5.setIcon(QIcon(button5_pixmap))
        self.button5.move(98, 6)
        self.button5.resize(90, 72)
        self.button5.setCursor(Qt.ArrowCursor)
        self.button5.setToolTip("")
        self.button5.clicked.connect(self.save)
        self.label2 = QLabel(self.ta1)
        self.label2.setText("Save As")
        self.label2.move(208, 56)
        self.label2.resize(80, 22)
        self.label2.setCursor(Qt.ArrowCursor)
        self.label2.setToolTip("")
        self.label3 = QLabel(self.ta1)
        self.label3.setText("Open")
        self.label3.move(38, 56)
        self.label3.resize(50, 22)
        self.label3.setCursor(Qt.ArrowCursor)
        self.label3.setToolTip("")
        self.button6 = QToolButton(self.ta1)
        self.button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button6.setText("")
        button6_pixmap = QPixmap("Umut-Pulat-Tulliana-2-3floppy-mount.128.png")
        self.button6.setAutoRaise(True)
        self.button6.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button6.setIconSize(button6_pixmap.size())
        self.button6.setIcon(QIcon(button6_pixmap))
        self.button6.move(198, 6)
        self.button6.resize(60, 52)
        self.button6.setCursor(Qt.ArrowCursor)
        self.button6.setToolTip("")
        self.button6.clicked.connect(self.savenrun)
        self.tab1.addTab(self.ta1, "File")
        self.ta2 = QWidget(self.tab1)
        self.ta2.setAutoFillBackground(True)
        self.ta2.setWindowTitle("")
        self.ta2.move(0, 0)
        self.ta2.resize(476, 93)
        palette = self.ta2.palette()
        palette.setColor(self.ta2.backgroundRole(), QColor(80, 80, 80, 255))
        self.ta2.setPalette(palette)
        self.ta2.setCursor(Qt.ArrowCursor)
        self.ta2.setToolTip("")
        self.spin1 = QSpinBox(self.ta2)
        self.spin1.setMinimum(0)
        self.spin1.setMaximum(64)
        self.spin1.setSingleStep(1)
        self.spin1.setValue(20)
        self.spin1.move(58, 6)
        self.spin1.resize(40, 22)
        self.spin1.setCursor(Qt.ArrowCursor)
        self.spin1.setToolTip("")
        self.spin1.valueChanged.connect(self.setfont1)
        self.label1 = QLabel(self.ta2)
        self.label1.setText("Font Size")
        self.label1.move(8, 6)
        self.label1.resize(50, 22)
        self.label1.setCursor(Qt.ArrowCursor)
        self.label1.setToolTip("")
        self.label4 = QLabel(self.ta2)
        self.label4.setText("Compiler")
        self.label4.move(108, 6)
        self.label4.resize(50, 22)
        self.label4.setCursor(Qt.ArrowCursor)
        self.label4.setToolTip("")
        self.radio1 = QRadioButton("Lua", self.ta2)
        self.radio1.setChecked(1)
        self.radio1.move(158, 6)
        self.radio1.resize(90, 22)
        self.radio1.setCursor(Qt.ArrowCursor)
        self.radio1.setToolTip("")
        self.radio3 = QRadioButton("Love", self.ta2)
        self.radio3.setChecked(0)
        self.radio3.move(158, 26)
        self.radio3.resize(90, 22)
        self.radio3.setCursor(Qt.ArrowCursor)
        self.radio3.setToolTip("")
        self.tab1.addTab(self.ta2, "Settings")
        self.ta3 = QWidget(self.tab1)
        self.ta3.setAutoFillBackground(True)
        self.ta3.setWindowTitle("")
        self.ta3.move(0, 0)
        self.ta3.resize(476, 93)
        self.ta3.setCursor(Qt.ArrowCursor)
        self.ta3.setToolTip("")
        self.button20 = QToolButton(self.ta3)
        self.button20.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button20.setText("")
        button20_pixmap = QPixmap("love2d.png")
        self.button20.setAutoRaise(True)
        self.button20.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button20.setIconSize(button20_pixmap.size())
        self.button20.setIcon(QIcon(button20_pixmap))
        self.button20.move(8, 6)
        self.button20.resize(80, 62)
        self.button20.setCursor(Qt.ArrowCursor)
        self.button20.setToolTip("")
        self.button20.clicked.connect(self.lovecompile)
        self.label7 = QLabel(self.ta3)
        self.label7.setText("Compile Love")
        self.label7.move(18, 66)
        self.label7.resize(70, 22)
        self.label7.setCursor(Qt.ArrowCursor)
        self.label7.setToolTip("")
        self.tab1.addTab(self.ta3, "Tools")
        self.ta4 = QWidget(self.tab1)
        self.ta4.setAutoFillBackground(True)
        self.ta4.setWindowTitle("")
        self.ta4.move(0, 0)
        self.ta4.resize(476, 93)
        self.ta4.setCursor(Qt.ArrowCursor)
        self.ta4.setToolTip("")
        self.button18 = QToolButton(self.ta4)
        self.button18.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button18.setText("")
        button18_pixmap = QPixmap("Oxygen-Icons.org-Oxygen-Actions-help-about.256.png")
        self.button18.setAutoRaise(True)
        self.button18.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button18.setIconSize(button18_pixmap.size())
        self.button18.setIcon(QIcon(button18_pixmap))
        self.button18.move(108, 6)
        self.button18.resize(80, 62)
        self.button18.setCursor(Qt.ArrowCursor)
        self.button18.setToolTip("")
        self.button18.clicked.connect(self.info)
        self.button19 = QToolButton(self.ta4)
        self.button19.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button19.setText("")
        button19_pixmap = QPixmap("Uriy1966-Steel-System-Library-Windows.512.png")
        self.button19.setAutoRaise(True)
        self.button19.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button19.setIconSize(button19_pixmap.size())
        self.button19.setIcon(QIcon(button19_pixmap))
        self.button19.move(8, 6)
        self.button19.resize(80, 62)
        self.button19.setCursor(Qt.ArrowCursor)
        self.button19.setToolTip("")
        self.button19.clicked.connect(self.freeresources)
        self.label5 = QLabel(self.ta4)
        self.label5.setText("  Free Resources")
        self.label5.move(8, 66)
        self.label5.resize(80, 22)
        self.label5.setCursor(Qt.ArrowCursor)
        self.label5.setToolTip("")
        self.label6 = QLabel(self.ta4)
        self.label6.setText("Info")
        self.label6.move(138, 66)
        self.label6.resize(40, 22)
        self.label6.setCursor(Qt.ArrowCursor)
        self.label6.setToolTip("")
        self.tab1.addTab(self.ta4, "Help")
        self.button1_copy = QToolButton(self.w1)
        self.button1_copy.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button1_copy.setText("")
        button1_copy_pixmap = QPixmap("Actions-system-run-icon.png")
        self.button1_copy.setAutoRaise(True)
        self.button1_copy.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button1_copy.setIconSize(button1_copy_pixmap.size())
        self.button1_copy.setIcon(QIcon(button1_copy_pixmap))
        self.button1_copy.move(500, 20)
        self.button1_copy.resize(140, 82)
        self.button1_copy.setCursor(Qt.ArrowCursor)
        self.button1_copy.setToolTip("")
        self.button1_copy.clicked.connect(self.runcode)
        self.results = QPlainTextEdit(self.w1)
        self.results.setPlainText("")
        self.results.move(10, 490)
        self.results.resize(640, 100)
        self.results.setStyleSheet("background-color: #414141; color: #c0c0c0;")
        self.results.setCursor(Qt.ArrowCursor)
        self.results.setToolTip("")
        self.results.setEnabled(False)
        self.group2 = QGroupBox(self.w1)
        self.group2.setAutoFillBackground(True)
        self.group2.setTitle("Love Components")
        self.group2.move(520, 290)
        self.group2.resize(130, 200)
        palette = self.group2.palette()
        palette.setColor(self.group2.backgroundRole(), QColor(129, 129, 129, 255))
        self.group2.setPalette(palette)
        self.group2.setCursor(Qt.ArrowCursor)
        self.group2.setToolTip("")
        self.button17 = QToolButton(self.group2)
        self.button17.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button17.setText("Starter Template")
        self.button17.move(10, 20)
        self.button17.resize(110, 22)
        self.button17.setStyleSheet("background-color: #565656; border-style: none; border-width: 2px; border-radius: 5px; ")
        self.button17.setCursor(Qt.ArrowCursor)
        self.button17.setToolTip("")
        self.button17.clicked.connect(self.addstarter)
        return self.w1

    def openfile(self):
        self.openfiledialog = QFileDialog()
        file_path, _ = self.openfiledialog.getOpenFileName(
            self, 'Select Lua File', '', 'Lua Files (*.lua)'
        )
        if file_path:
            with open(file_path, 'r') as file:
                self.text1.setPlainText(file.read())

    def setfont1(self):
        self.font1 = QFont("Arial", self.spin1.value())
        self.text1.setFont(self.font1)
        self.font2 = QFont("Arial", 16)
        self.results.setFont(self.font2)

    def savenrun(self):
        file_dialog = QFileDialog(self)
        file_dialog.setDefaultSuffix('.lua')
        file_path, _ = file_dialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.lua)')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text1.toPlainText())

    def save(self):
        with open("tempfiles/main.lua", "w") as file:
            file.write(self.text1.toPlainText())

    def runcode(self):
        if self.radio1.isChecked():
            with open("tempfiles/main.lua", "w") as file:
                file.write(self.text1.toPlainText())
            command = "lua54 tempfiles/main.lua"
        elif self.radio3.isChecked():
            with open("tempfiles/main.lua", "w") as file:
                file.write(self.text1.toPlainText())
            command = "love tempfiles/"
        else:
            return
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode().strip()
        error = error.decode().strip()
        if output:
            self.results.setPlainText(output)
        elif error:
            self.results.setPlainText(error)
        else:
            self.results.setPlainText("No output")

    def addfunc(self): 
        self.text1.appendPlainText("function name() \n//code here \nend")

    def addtable(self):
        self.text1.appendPlainText("table = {}")

    def addifelse(self):
        self.text1.appendPlainText("if state then  \n//code here\nend")

    def addlocal(self):
        self.text1.appendPlainText("local variable = //value here")

    def addprint(self):
        self.text1.appendPlainText("print(text here);")

    def addrequire(self):
        self.text1.appendPlainText("require //package name here")

    def addstarter(self):
        self.text1.appendPlainText("function love.load() \n//on game load \nend\nfunction love.update(dt)\n//updates every frame\nend\nfunction love.draw()\n//draws on screen\nend")

    def info(self):
        self.message = QMessageBox()
        self.message.setText("Created By Mohamad Hani Janaty \nPyMoon is a OpenSource Lua IDE focused on simplicity \nand ease of use")    
        self.message.exec_()    

    def freeresources(self):
        webbrowser.open("http://soundimage.org/")

    def lovecompile(self):
        os.system("pip install lovepacker")
        command = "python -m lovepacker tempfiles/main.lua"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode().strip()
        error = error.decode().strip()
        if output:
            self.results.setPlainText(output)
        elif error:
            self.results.setPlainText(error)
        else:
            self.results.setPlainText("No output")



                        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = Widget1()
    a.show()
    sys.exit(app.exec_())