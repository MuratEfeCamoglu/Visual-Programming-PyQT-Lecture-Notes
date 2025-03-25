from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_topla.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Toplam':
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender == 'Cikarma':
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender == 'Carpma':
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender == 'Bolme':
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())

        self.ui.lbl_sonuc.setText('sonuç: '+ str(result))


def app():
    app = QtWidgets.QApplication(sys.argv) 
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()


