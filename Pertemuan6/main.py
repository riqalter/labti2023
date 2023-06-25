from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def main():
    global app, window, textbox_nama, textbox_npm, textbox_kelas

    app = QApplication([])

    window = QWidget()
    window.setGeometry(400, 200, 400, 100)
    window.setWindowTitle("Pertemuan 6 - 50422881")

    label_judul = QLabel("Masukkan Data Diri Anda")
    label_nama = QLabel("Nama")
    label_npm = QLabel("NPM")
    label_kelas = QLabel("Kelas")

    textbox_nama = QLineEdit()
    textbox_npm = QLineEdit()
    textbox_kelas = QLineEdit()

    textbox_nama.setPlaceholderText("Masukkan Nama Anda")
    textbox_npm.setPlaceholderText("Masukkan NPM Anda")
    textbox_kelas.setPlaceholderText("Masukkan Kelas Anda")

    button_submit = QPushButton("Input Data")
    button_submit.clicked.connect(on_clicked)

    layout = QVBoxLayout()

    layout.addWidget(label_judul, alignment=Qt.AlignCenter)
    layout.addWidget(label_nama)
    layout.addWidget(textbox_nama)
    layout.addWidget(label_npm)
    layout.addWidget(textbox_npm)
    layout.addWidget(label_kelas)
    layout.addWidget(textbox_kelas)
    layout.addWidget(button_submit)

    window.setLayout(layout)
    window.show()

    app.exec_()

def on_clicked():	
    if textbox_nama.text() == "" or textbox_npm.text() == "" or textbox_kelas.text() == "":	
        message = QMessageBox()	
        message.critical(	
            window,	
            "Error",	
            "Mohon isi semua kolom form",	
        ) 	
        return
        
    message = QMessageBox()
    message.information(
        window,
        "Data diri anda",
        (
            f"Nama: {textbox_nama.text()} \nNPM: {textbox_npm.text()} \nKelas: {textbox_kelas.text()}"
        ),
    )

    textbox_nama.setText("")
    textbox_npm.setText("")
    textbox_kelas.setText("")

if __name__ == "__main__":
    main()


