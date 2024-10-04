from machine import Pin, ADC, PWM
import time

Pin9 = PWM(Pin(1),freq=1000000)
Pin2 = Pin(2, Pin.OUT)
Pin7 = Pin(3, Pin.OUT)

while 1:
    time.sleep(5)           #cw
    Pin9.duty_u16(32768)    #50% duty cw
    Pin2.on()
    Pin7.off()
    
    time.sleep(5)
    Pin9.duty_u16(65535)    #100% duty cw
    Pin2.on()
    Pin7.off()

    time.sleep(5)
    Pin9.duty_u16(32768)    #50% duty cw
    Pin2.on()
    Pin7.off()

    time.sleep(5)
    Pin9.duty_u16(0)

    Pin2.off()   
    Pin7.off()   
    time.sleep(5)
############################################################ 
    Pin9.duty_u16(32768) #50% duty ccw
    Pin2.off()
    Pin7.on()
    
    time.sleep(5)
    Pin9.duty_u16(65535) #100% duty ccw
    Pin2.off()
    Pin7.on()

    time.sleep(5)
    Pin9.duty_u16(32768) #50% duty ccw
    Pin2.off()
    Pin7.on()

    time.sleep(5)
    Pin9.duty_u16(0)
    Pin2.off()
    Pin7.off()