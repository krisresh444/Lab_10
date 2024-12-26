def f(n):
    def chisla(x):
        for i in range(2, int(x**0.5)+3):
            if x % i == 0: 
                return False 
        return True
    for i in range(2, n+1):
        if chisla(i):
            yield i 