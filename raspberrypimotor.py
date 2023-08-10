import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


left_motor_pin = 17
right_motor_pin = 18
piker_pin1=23
piker_pin2=24



GPIO.setup(left_motor_pin, GPIO.OUT)
GPIO.setup(right_motor_pin, GPIO.OUT)
GPIO.setup(piker_pin1, GPIO.OUT)
GPIO.setup(piker_pin2, GPIO.OUT)

left_motor_pwm = GPIO.PWM(left_motor_pin, 100)
right_motor_pwm = GPIO.PWM(right_motor_pin, 100)
piker_pin1_pwm = GPIO.PWM(piker_pin1, 100)
piker_pin2_pwm = GPIO.PWM(piker_pin2, 100)


left_motor_pwm.start(0)
right_motor_pwm.start(0)
piker_pin1_pwm.start(0)
piker_pin2_pwm.start(0)

def set_speed(left_speed, right_speed):
    left_motor_pwm.ChangeDutyCycle(left_speed)
    right_motor_pwm.ChangeDutyCycle(right_speed)
def move_piker(sss):
    piker_pin1_pwm.ChangeDutyCycle(sss)
    piker_pin2_pwm.ChangeDutyCycle(sss)

def stop_motors():
    set_speed(0, 0)

def move_forward(speed):
    set_speed(speed, speed)


def turn_left(speed):
    set_speed(0, speed)

def turn_right(speed):
    set_speed(speed, 0)
speed=60

try:
    while True:
        command = input("Enter command (f=forward,p=picker,sp=stop picker, l=left, r=right, s=stop): ")

        if command == "f":
    
            move_forward(speed)

        elif command == "p":
          
            move_piker(90)
        elif command == "sp":
       
            move_piker(0)

        elif command == "l":
     
            turn_left(speed)

        elif command == "r":
         
            turn_right(speed)

        elif command == "s":
            stop_motors()

except KeyboardInterrupt:

    stop_motors()
    left_motor_pwm.stop()
    right_motor_pwm.stop()
    GPIO.cleanup()

