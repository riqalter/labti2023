import sys
from PyQt5 import QtWidgets, uic
import conndb

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = conndb.conndb()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Data MAHASISWA")
        self.pushButtonMemuat.clicked.connect(self.loadData)
        self.pushButtonSimpan.clicked.connect(self.createData)
        self.pushButtonUpdate.clicked.connect(self.updateData)
        self.pushButtonDelete.clicked.connect(self.deleteData)
        self.tableWidget.clicked.connect(self.getData)
        self.tableWidget.setColumnWidth(0, 220)
        self.tableWidget.setColumnWidth(3, 220)

    def getData(self):
        row = self.tableWidget.currentRow()
        rowItemNama = self.tableWidget.item(row, 0).text()
        rowItemNpm = self.tableWidget.item(row, 1).text()
        rowItemKelas = self.tableWidget.item(row, 2).text()
        rowItemMatprak = self.tableWidget.item(row, 3).text()

        self.lineEditNama.setText(rowItemNama)
        self.lineEditNpm.setText(rowItemNpm)
        self.lineEditKelas.setText(rowItemKelas)
        self.lineEditMatprak.setText(rowItemMatprak)

    def createData(self):
        nama = self.lineEditNama.text()
        npm = self.lineEditNpm.text()
        kelas = self.lineEditKelas.text()
        mata_praktikum = self.lineEditMatprak.text()
        strsql = f"INSERT INTO mahasiswa (nama, npm, kelas, mata_praktikum) VALUES ('{nama}', '{npm}', '{kelas}', '{mata_praktikum}')"
        self.conn.queryExecute(strsql)
        self.loadData()

    def updateData(self):
        nama = self.lineEditNama.text()
        npm = self.lineEditNpm.text()
        kelas = self.lineEditKelas.text()
        mata_praktikum = self.lineEditMatprak.text()
        strsql = f"UPDATE mahasiswa SET nama ='{nama}', kelas='{kelas}', mata_praktikum='{mata_praktikum}' WHERE npm='{npm}'"

        self.conn.queryExecute(strsql)
        self.loadData()

    def loadData(self):
        strsql = "SELECT * FROM mahasiswa"
        result = self.conn.queryResult(strsql)
        print(result)
        row=0
        self.tableWidget.setRowCount(len(result))
        for user in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(user[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[3]))
            row = row+1

    def deleteData(self):
        npm = self.lineEditNpm.text()
        strsql = f"DELETE FROM mahasiswa WHERE npm='{npm}'"
        self.conn.queryExecute(strsql)
        self.loadData()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
