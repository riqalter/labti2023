import threading

def my_function():
    print("Hello Mahasiswa Gunadarma\n")

# membuat beberapa objek thread
threads =[]
for i in range(5):
    t = threading.Thread(target=my_function)
    threads.append(t)

# menjalankan thread
for t in threads:
    t.start()

# menunggu thread selesai
for t in threads:
    t.join()
