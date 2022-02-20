import multiprocessing as mp
import os


def fun(a):
    print("Fun Parent  pid  - ",os.getppid())
    print("Fun  pid  - ",os.getpid())


if "__main__" == __name__:
    print("Script Main pid  - ", os.getpid())
    p = mp.Process(target=fun,args=('bob',))
    p1 = mp.Process(target=fun,args=('bob',))
    p.start()
    p1.start()




a = [1,2,4]

list()
dict()


from django.db.models import  Model