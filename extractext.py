import io
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image
from pytesseract import image_to_string
import subprocess

# apps class
class App(QWidget):

    def __init__(self):
        # design about graphics and defining names etc.
        super().__init__()
        self.setWindowTitle("ExtracText")

        self.resize(809, 500)
        self.setMinimumSize(809, 500)
        self.setMaximumSize(809, 500)
        icon = QIcon()
        icon.addPixmap(QPixmap("D:/laravel&extractext/extractext/[Mahir Can Yüksel].15541040/logox.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap("D:/laravel&extractext/extractext/[Mahir Can Yüksel].15541040/logox.png"), QIcon.Normal, QIcon.On)
        self.setWindowIcon(icon)
        self.setWindowOpacity(1.0)
        self.setAutoFillBackground(False)
        self.setStyleSheet("alternate-background-color: rgb(243, 244, 255);")

        self.browseButton = QPushButton(self)
        self.browseButton.setGeometry(75, 300, 250, 30)
        self.browseButton.setStyleSheet("font: 87 10pt \"Segoe UI\";\n")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setText("Dosyayı seçin ve başlatın")
        self.label = QLabel(self)
        self.label.setStyleSheet("font: 27 12pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.label.setGeometry(75, 375, 400, 30)
        self.label.setText("")


        self.saveButton = QPushButton(self)
        self.saveButton.setStyleSheet("font: 87 11pt \"Segoe UI\";\n")
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setGeometry(75, 410, 250, 30)
        self.saveButton.setText("Kaydetmek için tıklayın")
        self.description = QLabel(self)
        self.description.setGeometry(30, 110, 411, 111)
        self.description.setStyleSheet("font: 87 10pt \"Segoe UI\";")
        self.description.setObjectName("description")
        self.description.setText("ExtracText sayesinde gömülü yazılarınızı text formatına dönüştürün.")
        self.explain = QLabel(self)
        self.explain.setGeometry(75, 185, 411, 111)
        self.explain.setStyleSheet("font: 87 11pt \"Segoe UI\";")
        self.explain.setObjectName("explain")
        self.explain.setText("Dönüştürmek istediğiniz dosyanın türünü seçiniz:")
        self.jpgType = QCheckBox(self)
        self.jpgType.setStyleSheet("font: 87 9pt \"Segoe UI\";\n")
        self.jpgType.setCheckable(True)
        self.jpgType.setObjectName("jpgType")
        self.jpgType.setGeometry(80, 250, 250, 30)
        self.jpgType.setText("Resim dosyası")
        self.pdfType = QCheckBox(self)
        self.pdfType.setStyleSheet("font: 87 9pt \"Segoe UI\";\n")
        self.pdfType.setObjectName("pdfType")
        self.pdfType.setCheckable(True)
        self.pdfType.setGeometry(80, 270, 250, 30)
        self.pdfType.setText("PDF dosyası")
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(485, 20, 260, 420)
        self.plainTextEdit.setStyleSheet("background-color: rgb(249, 248, 255);")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.logo = QLabel(self)
        self.logo.setGeometry(75, 5, 303, 111)
        self.logo.setText("")
        self.logo.setPixmap(QPixmap("D:/laravel&extractext/extractext/[Mahir Can Yüksel].15541040/logox.png"))
        self.logo.setObjectName("logo")


        self.initUI()

    def initUI(self):
        # initializing

        self.browseButton.clicked.connect(self.extracting)





    def extracting(self):
        if(self.pdfType.isChecked()):
            self.pdf()
            self.jpg()
        if(self.jpgType.isChecked()):
            self.jpg()
            self.label.setText("Kaydetme işlemi başarıyla gerçekleştirildi.")




    def pdf(self):
        # define master function: openfile and extracting process
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"ExtracText", "","Tüm dosyalar (*)", options=options)
        PDFTOPPMPATH = r"C:/Program Files (x86)/poppler/bin/pdftoppm.exe"
        PDFFILE = ""+fileName+""
        subprocess.Popen('"%s" -png "%s" ExtracText' % (PDFTOPPMPATH, PDFFILE))


    def jpg(self):
        self.label.setText("İşleminiz gerçekleştiriliyor. Lütfen bekleyiniz...")
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"ExtracText", "","Tüm dosyalar (*)", options=options)
        img= Image.open(fileName)
        text= image_to_string(img,lang='tur')
        self.label.setText("Dönüştürme işlemi başarıyla tamamlanmıştır.")
        self.plainTextEdit.setPlainText(text)
        file = open(fileName+".txt","w")
        file.write(text)
        file.close()
        self.label.setText("Kaydetme işlemi gerçekleştiriliyor.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
