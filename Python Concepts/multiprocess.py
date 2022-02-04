from multiprocessing import Process
import os

def fun(a):
    print("in PFun")
    print(os.getppid())
    print(os.getpid())

if "__main__" == __name__:

    p = Process(target=fun,args=('bob',))
    p.start()