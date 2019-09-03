import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = Messenger(name = 'My name is X\n')
y = Messenger(name = 'My name is Y\n')
x.start()
y.start()
