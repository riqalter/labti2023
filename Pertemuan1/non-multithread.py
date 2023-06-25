import time

class olahData:
    def __init__(self, rentang):
        self.rentang = rentang

    def readData(self):
        print(f"[1] Read data ke : {self.rentang}")
        time.sleep(2)

    def sortData(self):
        print(f"[2] Sort data ke : {self.rentang}")
        time.sleep(1)

    def exportData(self):
        print(f"[3] Export data ke : {self.rentang}")
        time.sleep(1)

    def run(self):
        self.readData()
        self.sortData()
        self.exportData()
    
if __name__ == "__main__":
    start = time.perf_counter()
    rentangs = {
        "1-100000",
        "100001-200000",
        "200001-300000",
        "300001-400000",
        "400001-500000",
        "500001-600000",
        "600001-700000",
        "700001-800000",
        "800001-900000",
        "900001-1000000",
    }

    for rentang in rentangs:
        olahData(rentang).run()

    finish = time.perf_counter()

    print(f"waktu total : {round(finish-start, 2)}")