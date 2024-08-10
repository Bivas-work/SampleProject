import time
import threading

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(func.__name__ +" took "+ str((time.time()- start)* 1000) + " mil seconds ")
        return result
    return wrapper
@time_it
def calc_square(number):
    time.sleep(0.2)
    for num in number:
        print("square", num * num)

@time_it
def calc_qube(number):
    time.sleep(0.2)
    for num in number:
        print("qube", num * num * num)

start = time.time()
arrayVal = [2,3,4,5]
t1 =  threading.Thread(target=calc_square, args=(arrayVal,))
t2 =  threading.Thread(target=calc_qube, args=(arrayVal,))
t1.start()
t2.start()
t1.join()
t2.join()

print("program took: ", (time.time()-start)*1000, " mil seconds")