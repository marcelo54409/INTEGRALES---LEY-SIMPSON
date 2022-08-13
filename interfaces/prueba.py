#import matplotlib as plot
import numpy as np
import re

fcn = ""


def graphic(a, b):
    global fcn
    x = np.linspace(a, b, 100)
    y = eval(fcn)

    #fig = plot.figure()
    #ax = fig.add_subplot(1, 1, 1)
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    return x, y
    #plt.plot(x, y, 'r')
    # fig.savefig("figure.png")
    # plt.close(fig)


def f(x0):
    x = x0
    return eval(fcn)


def simpson(a, b, n) -> int:
    dif = (b-a)/n
    i = 0
    sum = 0
    while (i < n-1):
        x1 = a + i*dif
        x2 = x1 + dif
        x3 = x2 + dif
        sum += f(x1) + 4*f(x2) + f(x3)
        i = i + 2
    res = dif*sum/3
    return res


def formating(f):
    if "^" in f:
        f = re.sub(r'\^', '**', f)
    if "sin" in f:
        f = re.sub(r'sin', 'np.sin', f)
    if "arcnp.sin" in f:
        f = re.sub(r'arcnp.sin', 'np.arcsin', f)
    if "cos" in f:
        f = re.sub(r'cos', 'np.cos', f)
        if "arcnp.cos" in f:
            f = re.sub(r'arcnp.cos', 'np.arccos', f)
    if "tan" in f:
        f = re.sub(r'tan', 'np.tan', f)
        if "arcnp.tan" in f:
            f = re.sub(r'arcnp.tan', 'np.arctan', f)
    if "ctg" in f:
        f = re.sub(r'ctg', '1/np.tan', f)
        if "arc1/np.tan" in f:
            f = re.sub(r'arc1/np.tan\(', 'np.arctan(1/', f)
    if "sec" in f:
        f = re.sub(r'sec', '1/np.cos', f)
        if "arc1/np.cos" in f:
            f = re.sub(r'arc1/np.cos\(', 'np.arccos(1/', f)
    if "csc" in f:
        f = re.sub(r'csc', '1/np.sen', f)
        if "arc1/np.sen" in f:
            f = re.sub(r'arc1/np.sen\(', 'np.arcsen(1/', f)
    if "sqrt" in f:
        f = re.sub(r'sqrt', 'np.sqrt', f)
    if "ln" in f:
        f = re.sub(r'ln', 'np.log', f)
    return f

# 1


def setFunction(funcion):
    global fcn
    fcn = formating(funcion)
