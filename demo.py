import numpy as np
import matplotlib.pyplot as plt
import cmath

class polynomial:
    def __init__(self):
        print('init polynomial')

    def hello(self, name):
        print('hello world, %s' % (name))

class mathDraw:
    def __init__(self, f):
        self.f = f
    
    def draw_linspace(self, start, end, num):
        x = np.linspace(start, end, num)
        ex = []
        ey = []        
        for v in x:
            y = self.f(v) 
            if y != None:
                ex.append(v)
                ey.append(y)
        plt.plot(ex, ey)
        plt.show()

    def draw_eclipse(self, start, end, num):
        x = np.linspace(start, end, num)
        ex = []
        ey = []
        ey_rv = []  
        for v in x:
            y = self.f(v) 
            if y != None:
                ex.append(v)
                ey.append(y)
                ey_rv.append(-y)
        line = plt.plot(ex, ey)[0]
        line.set(color = 'r')
        line = plt.plot(ex, ey_rv)[0]
        line.set(color = 'r')
        plt.show()

    def draw_points(self, x, y):
        plt.plot(x, y)
        plt.show()

class umath:
    def __init(self):
        print('init umath')

    def countPrimes(self, n):
        if n <= 2:
            return 0
        else:
            res = []
        for i in range(2, n):
            flag = 0
            for j in res:
                if i % j == 0:
                    flag = 1
            if flag == 0:
                res.append(i)
        return len(res), res

# f(x) = x^3 - 5x^2 + 9
def func(x):
    return x**3 - 5*x**2 + 9

def func_ecc(x):
    value = x**3 - 2*x + 4
    if value >= 0:
        return cmath.sqrt(value)
    else:
        return None

# exp(x)=ex
def exp(x):
    return np.e**x

obj = polynomial()
obj.hello('yd')


m = umath()
da, res = m.countPrimes(20)
print(res, ', primes: %d' % da)

poly = mathDraw(func_ecc)
poly.draw_eclipse(-5, 5, 5000)

exit

# expDraw = mathDraw(exp)
# expDraw.draw_linspace(-5, 5, num = 100)

# poly = mathDraw(func)
# poly.draw_linspace(-5, 5, 100)
