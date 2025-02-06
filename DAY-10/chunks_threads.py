import threading
results=[]
def calc_sum(chunk):
    result=sum(chunk)
    results.append(result)

chunks=[
    list(range(10000000)),
    list(range(10000000,20000000)),
    list(range(20000000,30000001)),
]
threads=[]
for chunk in chunks:
    thread=threading.Thread(target=calc_sum,args=(chunk,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(sum(results))
    
