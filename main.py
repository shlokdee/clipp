import sys
import os
import time
os.environ["QT_QPA_PLATFORM"] = "xcb"
from PySide6.QtGui import QGuiApplication

app=QGuiApplication(sys.argv)
app.processEvents()
clipboard=app.clipboard()

clip=["sample"]
def clipchanged():
    if clip[-1] != clipboard.text():
        clip.append(clipboard.text())
        print(clip)


clipboard.dataChanged.connect(clipchanged)



sys.exit(app.exec())