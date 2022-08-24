from time import time

def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time() # start timer
    result = fn(*args, **kwargs)
    t2 = time() # stop timer
    
    print(f'it took {t2 - t1} s')
    return result
  return wrapper


@performance
def long_time():
  for i in range(100000):
    i * 5

long_time()