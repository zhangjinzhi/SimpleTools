from multiprocess import Process, Queue

def f(q):
    q.put('hello world')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=[q])
    p.start()
    print (q.get())
    p.join()