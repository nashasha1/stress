import time

def dead_loop():
    a = time.time()
    print a
    count = 0
    while True:
        b=time.time()
        if b - a > 10:
            print 'sleep 1s'
            print a,'---',count
            count = 0
#            time.sleep(0.1)
            a=time.time()
        count += 1
if __name__ == '__main__':
    dead_loop()
    print time.time()
