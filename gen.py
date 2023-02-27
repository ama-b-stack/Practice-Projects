def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step
        # generator = gen_range(10)
        # next(generator)
        # will "iterate" through

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
        # python -i gen.py
        # fib = gen_fib()
        # next(fib)
        # this will return forever
        
        # [next(fib) for _ in range(50)][-1]
        # this will return the 50th number in fib sequence quickly
