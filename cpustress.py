import time

def dead_loop():
    a = time.time()
    print a
    while True:
        b=time.time()
        if b - a > 10:
            print 'sleep 1s'
            time.sleep(1)
            a=time.time()
            print a
        pass
if __name__ == '__main__':
    dead_loop()
    print time.time()
