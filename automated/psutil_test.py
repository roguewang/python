#!/usr/bin/env python
# Author:rogue
import psutil,time,datetime

# cpu相关
print(psutil.cpu_times())

print(psutil.cpu_times(percpu=True))

print(psutil.cpu_times().user)  # 获取单项数据信息,如用户 user的cpu时间比

print(psutil.cpu_count())   # 获取cpu的逻辑个数,默认logical=True,即:是否是逻辑的logical

print(psutil.cpu_count(logical=False))  # 获取cpu的物理个数,即:是否是逻辑的logical

# 获取内存信息

print(psutil.virtual_memory().total / 1024 / 1024)  # 获取内存总量,然后换算成M

mem = psutil.virtual_memory()   # 将内存信息赋值给mem
print(mem)

print(mem.total)    # 获取内存总数

print(mem.free)     # 获取空闲内存数

# swap分区
swap = psutil.swap_memory()     # 将swap分区信息赋值给swap
print(swap)

print(swap.used)    # 获取已使用的swap分区空间

# 磁盘
print(psutil.disk_partitions())     # 打印完整的磁盘信息赋值给disk
print(psutil.disk_usage("/"))   # 查看该分区"/"的使用情况

print(psutil.disk_io_counters())    # 获取磁盘总的io个数,读写信息

print(psutil.disk_io_counters(perdisk=True))    # 通过perdisk参数来获取单个分区的io个数和读写信息

print("分隔".center(30,'='))


# 网络信息
print(psutil.net_io_counters())    # 获取网络总的,默认pernic=False

print(psutil.net_io_counters(pernic=True))  # 获取每个网络接口的IO信息

print("分隔".center(30,'='))

# 其他系统信息
print(psutil.users())   #得到当前登录的用户信息

# 把started转换为人看的格式
user = psutil.users()       # 把当前用户信息赋值给user
started = user[0].started       # 获取user[0]的started数据
t = time.localtime(started)     # 用time.localtime方法把started转换成能看懂的格式

started2 = psutil.boot_time()       # 获取开机时间,以linux时间戳的形式返回
t2 = time.localtime(started2)

print("用户登录时间:",datetime.datetime.fromtimestamp(started).strftime("%Y-%m-%d %H:%M:%S"))     #通过datetime的format方法来格式化时间
print("开机时间:",datetime.datetime.fromtimestamp(started2).strftime("%Y-%m-%d %H:%M:%S"))


print(psutil.pids())
