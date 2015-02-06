import time

def dead_loop():
    a = time.time()
    print a
    while True:
        b=time.time()
        if b - a > 10:
            break
        pass
if __name__ == '__main__':
    dead_loop()
