import threading
import time
def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time .sleep(2)
        print(f"{threading.current_thread().name} has released the lock")
        
lock=threading.Lock()
threads=[threading.Thread(target=task,args=(lock,)) for _ in range(5)]
for thread in threads:
    thread.start() 

for thread in threads:
    thread.join() 
print("task is completed")

