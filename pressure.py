from machine import Pin, ADC
import time

def get_adc_value(adc):
    # 在MicroPython中，直接读取ADC对象的值即可
    return adc.read()

def get_adc_average(adc, times):
    temp_val = 0
    for _ in range(times):
        temp_val += get_adc_value(adc)
        time.sleep_ms(2)  # 等待2毫秒，模仿C语言中的延时
    return temp_val // times

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)  # 配置ADC以读取最大3.3V

def main():
    while True:
        # 初始化ADC，这里以GPIO36为例，对应于ESP32的VP引脚
        # 读取ADC值并计算平均值，这里假设我们想要读取50次以获得平均值
        average_value = get_adc_average(adc, 50)
        

        # 根据需要转换平均ADC值到电压值
        voltage = average_value * 3.0 / 4095
        
        
        # 根据电气曲线得到压力通道电压
        v_pressure = voltage / 1.242
        
        
        # 计算压力
        pressure = 0.48471 * v_pressure + 4.4168
        print('Voltage: {:.2f}V, Pressure: {:.2f}Kpa'.format(v_pressure, pressure))
        
        # 延时
        time.sleep(2)  # 等待2秒再次读取
if __name__ == '__main__':
    main()


