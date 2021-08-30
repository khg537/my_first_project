import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import re
import pandas as pd

#form의 주소 [0]은 첫번째것만 가져온 것 
form_class = uic.loadUiType("test.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mystr = []

    def slot_textChanged(self):
        print("textChanged")

        self.mystr.append(self.textEdit.toPlainText())

    def slot_print(self):
        mystr2 = self.textEdit.toPlainText()
        mystr2 = re.split(r'\s|\n', mystr2)
        mylist = pd.unique(mystr2).tolist()
        mylist = [ x for x in mylist if not x=='']

        print(mystr2, type(mylist),mylist, sep='\n')

    def slot_clear(self):
        self.textEdit.clear()
        
       

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()

