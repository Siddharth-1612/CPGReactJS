import threading
import time
def single_task():
    print("task is started")
    time.sleep(2)
    print("task is completed")
threader=threading.Thread(target=single_task)
threader.start()
threader.join()
print("main thread is completed")