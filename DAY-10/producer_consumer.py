import queue
import threading
import time

def producer(q):
    l1=['apples','oranges','banana','pear','guava']
    for i in l1:
        q.put(i)
        print(f"{i} is produced")
        time.sleep(2)
def consumer(q):
    while True:
        item=q.get()
        if(item is None):
            break
        print(f"{item} is consumed")
        time.sleep(2)
q=queue.Queue()
producer=threading.Thread(target=producer,args=(q,))
consumer=threading.Thread(target=consumer,args=(q,))
producer.start()
consumer.start()
producer.join()
q.put(None)
consumer.join()
print("the task is completed")

