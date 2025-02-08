import con #connectivity
import test
import ufirebase as firebase #firebase connection
from machine import I2C, Pin
import mpu6050 # accident detection
import gps_sat # gps value
from time import sleep
from hcsr04 import HCSR04 # parking 
from servo import Servo # airbag 

test.res()

con.connection()

URL='test2-48b95-default-rtdb.firebaseio.com/SmartCar'

#Ultrasonic 
sensor = HCSR04(trigger_pin=18,echo_pin=5,echo_timeout_us=1000000)

#ESP8266
# i2c = I2C(scl=Pin(5), sda=Pin(4))

#ESP32
i2c = I2C(scl=Pin(22), sda=Pin(21))

#Servo Motor

motor=Servo(pin=13)
motor.move(0)
accelerometer = mpu6050.accel(i2c)
Data={}
while True:
    val = accelerometer.get_values()
    gps_data = gps_sat.val2()
    
    parking_distance = sensor.distance_cm()
    if parking_distance <=7:
        Pin(12,Pin.OUT).value(1)
        Pin(14,Pin.OUT).value(1)
        Pin(27,Pin.OUT).value(1)
        print("Caution!!!! Obstacle is close")
    else:
        test.res()
    '''if (parking_distance >5 and parking_distance <=10):
        test.res()
        Pin(12,Pin.OUT).value(1)
        Pin(14,Pin.OUT).value(1)
    if (parking_distance >10 and parking_distance <=15):
        test.res()
        Pin(12,Pin.OUT).value(1)'''
    
    '''
    GyZ = val['GyZ']
    GyY = val['GyY']
    GyX = val['GyX']
    '''
    
    GyZ = val['AcZ']
    GyY = val['AcY']
    GyX = val['AcX']
    
    if(GyX <= -7500 or GyX >= 8500 or GyY <= -7500 or GyY >= 8500 or GyZ >=0):
        Pin(12,Pin.OUT).value(1)
        Pin(14,Pin.OUT).value(1)
        Pin(27,Pin.OUT).value(1)
        # Open Servo Motor
        motor.move(180)
        
        print("Accident Occured")
        print()
        print('X-axix',GyX)
        print('Y-axix',GyY)
        print('Z-axix',GyZ)
        # print("Gps data: ",lat,long)
        
        break
    else:
        motor.move(0)
    #Sending Accelerometer Data
    
    Data['X'] = GyX
    Data['Y'] = GyY
    Data['Z'] = GyZ
    
    lat = gps_data["Latitude"]
    long = gps_data["Longitude"]
    
    #Sending Lat , Lang Data
    
    Data['Lat'] = lat
    Data['Long'] = long
    
    Data['Dist'] = parking_distance
    
    #trying to send data
    while True:
        try:
            # print(Data)
            firebase.put(URL,Data) # Realtime
            #print('Received Data: ',firebase.get(URL))
            print('Recieved Data')
            print()
            break 
        except:
            print('Reconnecting')
            print()
        
    print('X-axix',GyX)
    print('Y-axix',GyY)
    print('Z-axix',GyZ)
    
        
    print("Gps data: ",lat,long)
    print("Distance: ",parking_distance)
    
    
     
    sleep(0.5)

    

