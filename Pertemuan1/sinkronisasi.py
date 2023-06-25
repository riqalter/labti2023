import threading

class DataProcessor:
    def __init__(self):
        self.lock = threading.Lock()

    def process_data(self):
        with self.lock:
            print("data diproses")

def run_thread(data_processor):
    for _ in range(10):
        data_processor.process_data()

data_processor = DataProcessor()

thread1 = threading.Thread(target=run_thread, args=(data_processor,))
thread2 = threading.Thread(target=run_thread, args=(data_processor,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("proses selesai")



