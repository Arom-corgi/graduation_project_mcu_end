import _thread, time
from machine import Timer
from multithreading import Task
import heart_rate, SpO2_tmp, multithreading


# 声明变量
heart_rates = 0
SpO2 = 0
tmp = 0
counter = 0
timer = None
# 控制线程标志
stop_event = False

def display_info():
    # 声明全局变量用于赋值
    global heart_rates, SpO2, tmp, counter, stop_event
    while counter < 30 and not stop_event:
        heart_rates = heart_rate.read_rate()
        SpO2, tmp = SpO2_tmp.read_SpO2()
        print('心率: ', heart_rates, '血氧: ', SpO2, '温度: ', tmp)
        counter += 1
        time.sleep(1)
    
if __name__ == '__main__':
#     # 创建定时器
#     timer = Timer(1)
#     # 设置定时器的回调函数，每1秒钟调用1次display_info函数（用来显示数据）
#     timer.init(period=1000, mode=Timer.PERIODIC, callback=display_info)
    # 回调函数均存在死循环，开多线程调用主程序，用来检测数据
    # 创建并启动健康指标输出线程
    _thread.start_new_thread(display_info, ())
    # 创建并启动心率检测线程
    _thread.start_new_thread(heart_rate.main, ())
    # 创建并启动血氧温度检测线程
    _thread.start_new_thread(SpO2_tmp.main, ())
    # 延时15秒钟
    time.sleep(30)
    stop_event = True  # 设置标志，通知线程停止执行
#     # 结束线程的执行
#     _thread.exit()

    
    

