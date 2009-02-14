#!/usr/bin/python

print "meamm v0.0.1 alpha\n"

from qt4 import *
from gui_form import *
import sys
if __name__ == "__main__":
	app = QApplication(sys.argv)
	f = gui_form()
	f.show()
	app.setMainWidget(f)
	app.exec_loop()

