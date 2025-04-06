import sys
from PyQt5 import QtWidgets
from form_data import Ui_Dialog

class FormData(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormData()
    window.show()
    sys.exit(app.exec_())
