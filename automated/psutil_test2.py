#!/usr/bin/env python
# Author:rogue
# 系统进程管理方法
import psutil,time,datetime

#pids = psutil.pids()        # 把所有的PID赋值给pids

#for i in pids:          # 循环获取PID
    # p = psutil.Process(i)    # 获取PID对应的进程名
    # print(p.name())     # 进程名
    # p.exe()       # 进程bin路径
    # p.cwd()       # 工作目录绝对路径
    # p.status()    # 进程状态
    # p.create_time()   # 创建时间,以时间戳的形式
    # p.uids()      # 进程uid
    # p.gids()      # 进程gid
    # p.cpu_times() # 进程cpu时间,包括user system
    # p.cpu_affinity()  # cpu亲和度
    # p.memory_full_info()  # 内存利用率
    # p.memory_info()   # 进程内存的rss,vms信息
    # p.io_counters()   # 进程io信息,包括读写io数及字节数
    # p.connections()   # 返回打开进程socket的namedutples列表,fs,family,laddr 等信息
    # p.num_threads()   # 进程开启的线程数

# popen类:获取用户 启动的应用程序进程信息,以便跟踪程序进程的运行状态.

from subprocess import PIPE
# 通过psutil的popen方法启动应用程序,可以跟踪程序运行的所有相关信息
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
print(p.name())
print(p.username())
print(p.cpu_times())    # 得到进程运行的CPU时间