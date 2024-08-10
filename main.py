import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(func.__name__ +" took "+ str((time.time()- start)* 1000) + " mil seconds ")
        return result
    return wrapper
@time_it
def calc_square(number):
    result =[]
    for num in number:
        result.append(num*num)
    return result

arrayVal = range(1,10000000)
out_sq = calc_square(arrayVal)