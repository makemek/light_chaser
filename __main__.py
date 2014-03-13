from lightChaser import LightChaser
from PySide.QtGui import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    prog = LightChaser()
    prog.setWindowTitle("Light Chaser")
    prog.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())