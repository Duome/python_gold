# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 初始化Thread对象，将函数（及其参数）传进去
"""
# import threading
# from time import sleep, ctime
#
# loops = [4, 2]
#
# def loop(nloop, nsec):
#     print 'start loop', nloop, 'at:', ctime()
#     sleep(nsec)
#     print 'loop', nloop, 'done at:', ctime()
#
# def main():
#     print 'starting at:', ctime()
#     threads = []
#     nloops = range(len(loops))
#
#     for i in nloops:
#         t = threading.Thread(target=loop, args=(i, loops[i]))   # 传入循环号码和睡眠时间
#         threads.append(t)
#
#     for i in nloops:    # start threads
#         threads[i].start()
#
#     for i in nloops:    # wait for all
#         threads[i].join()   # threads to finish
#
#     print 'all DONE at:', ctime()
#
# if __name__ == '__main__':
#     main()





import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nesc):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nesc)
    print 'loop', nloop, 'done at:',ctime()

def main():
    print 'stating at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()






















