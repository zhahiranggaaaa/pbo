import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QLabel, QPushButton, QLineEdit, QTabWidget, QVBoxLayout, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Pemesanan Tiket Pesawat")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QTabWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.tab_flight = QWidget()
        self.central_widget.addTab(self.tab_flight, "Pesan Tiket")

        self.label_from = QLabel("Dari ✈︎   :", self.tab_flight)
        self.label_from.move(50, 25)

        self.line_edit_from = QLineEdit(self.tab_flight)
        self.line_edit_from.setGeometry(50, 45, 200, 20)

        self.label_to = QLabel("Ke   ✈︎   :", self.tab_flight)
        self.label_to.move(50, 67)

        self.line_edit_to = QLineEdit(self.tab_flight)
        self.line_edit_to.setGeometry(50, 85, 200, 20)

        self.label_date = QLabel("Tanggal :", self.tab_flight)
        self.label_date.move(50, 107)

        self.line_edit_date = QLineEdit(self.tab_flight)
        self.line_edit_date.setGeometry(50, 125, 200, 20)
        

        self.label_name = QLabel("Nama Pemesan:", self.tab_flight)
        self.label_name.move(50, 150)

        self.line_edit_name = QLineEdit(self.tab_flight)
        self.line_edit_name.setGeometry(50, 170, 200, 20)



        self.button_search = QPushButton("Cari Penerbangan", self.tab_flight)
        self.button_search.setGeometry(100, 200, 100, 30)
        self.button_search.clicked.connect(self.open_dialog)

        self.tab_booking = QWidget()
        self.central_widget.addTab(self.tab_booking, "Data Pemesanan")

        self.layout = QVBoxLayout(self.tab_booking)
        self.text_edit = QLabel()
        self.text_edit.move(0,0)
        self.layout.addWidget(self.text_edit)


    def open_dialog(self):
        dialog = FlightDialog(self)
        if dialog.exec_():
            passenger_name = self.line_edit_name.text()
            ticket_info = dialog.ticket_info
            price = dialog.price
            date = self.line_edit_date.text()
            self.text_edit.setText(f"Nama Pemesan        : {passenger_name}\nKarcis Pemesanan    : {ticket_info}\nHarga                       : Rp {price}\nTanggal                    : {date}")


class FlightDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Daftar Penerbangan")
        self.setGeometry(200, 200, 400, 300)

        self.label_flight = QLabel("Pilih Pesawat:", self)
        self.label_flight.move(50, 50)

        self.button_flight1 = QPushButton("GARUDA INDONESIA\n(Rp 10.000.000)", self)
        self.button_flight1.setGeometry(50, 80, 200, 50)
        self.button_flight1.clicked.connect(self.select_flight1)

        self.button_flight2 = QPushButton("BATIK AIR\n(Rp 8.000.000 )", self)
        self.button_flight2.setGeometry(50, 150, 200, 50)
        self.button_flight2.clicked.connect(self.select_flight2)

        self.button_flight3 = QPushButton("CITILINK\n(Rp 5.000.000 )", self)
        self.button_flight3.setGeometry(50, 220, 200, 50)
        self.button_flight3.clicked.connect(self.select_flight3)

        self.button_flight4 = QPushButton("SRIWIJAYA AIR\n(Rp 3.500.000 )", self)
        self.button_flight4.setGeometry(250, 80, 200, 50)
        self.button_flight4.clicked.connect(self.select_flight4)

        self.button_flight5 = QPushButton("LION AIR\n(Rp 2.500.000)", self)
        self.button_flight5.setGeometry(250, 150, 200, 50)
        self.button_flight5.clicked.connect(self.select_flight5)

        self.button_flight5 = QPushButton("AIR ASIA\n(Rp 1.500.000)", self)
        self.button_flight5.setGeometry(250, 220, 200, 50)
        self.button_flight5.clicked.connect(self.select_flight5)


        self.passenger_name = ""
        self.ticket_info = ""
        self.price = ""


    def select_flight1(self):
        self.passenger_name = self.parent().line_edit_name.text()
        self.ticket_info = "GARUDA INDONESIA"
        self.price = "10.000.000"
        self.accept()

    def select_flight2(self):
        self.passenger_name = self.parent().line_edit_name.text()
        self.ticket_info = "BATIK AIR"
        self.price = "8.000.000"
        self.accept()

    def select_flight3(self):
        self.passenger_name = self.parent().line_edit_name.text()
        self.ticket_info = "CITILINK"
        self.price = "5.000.000"
        self.accept()

    def select_flight4(self):
        self.passenger_name = self.parent().line_edit_name.text()
        self.ticket_info = "SRIWIJAYA AIR"
        self.price = "3.500.000"
        self.accept()

    def select_flight5(self):
        self.passenger_name = self.parent().line_edit_name.text()
        self.ticket_info = "LION AIR"
        self.price = "2.500.000"
        self.accept()
    
    def select_flight5(self):
        self.passenger_name = self.parent().line_edit_name.text()
        self.ticket_info = "AIR ASIA"
        self.price = "1.500.000"
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
