#!/usr/bin/env python3

from multiprocessing import Pipe, Process


conn1, conn2 = Pipe()

def f1():
    conn1.send('hello')


def f2():
    data = conn2.recv()
    print(data)


def main():
#    Process(target=f1).start()
#    Process(target=f2).start()
    f1()
    f2()

if __name__ == '__main__':
    main()


