from machine import Pin
import stepper2003 

m = stepper2003.FullStepMotor.frompins(1,2,3,4)

while 1:
    user = input("How many steps:")
    int_value = int(user)
    m.step(int_value)
        