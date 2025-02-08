# Smart-Car-Accident-Detection-System-IOT

An IoT-based vehicle safety solution that leverages ultrasonic sensors (HCSR04), GPS tracking (ublox neo6m), and motion detection (MPU6050) to provide real-time accident monitoring and alerts. The system runs on an ESP32 microcontroller using MicroPython and features a companion Android app for location tracking and instant notifications. All data is securely managed through Firebase backend services.

## **Objectives**
**Primary objectives:**
* Create an IoT-based smart car accident detection and safety system
* Provide real-time accident detection and notification
* Enable GPS tracking and location monitoring
* Implement parking assistance features
* Automate airbag deployment in case of accidents

**Secondary objectives:**
* Establish wireless communication using ESP32 and Wi-Fi
* Create a user-friendly mobile application interface
* Enable data storage and retrieval through Firebase
* Integrate multiple sensors for comprehensive safety monitoring

---

## **Setup and Execution Codes**
**Hardware Components Required:**

* ESP32 microcontroller
* HCSR04 Ultrasonic sensor
* Ublox neo6m GPS module
* MPU6050 Gyroscope sensor
* SG90 Servo Motor
* Buzzer and LED indicators
* Jumper wires
* 5V DC power supply

**Software Requirements:**

* Thonny IDE with MicroPython v1.22.1
* Firebase for backend
* Android Studio for mobile app development

## **Key Implementation Steps:**
**Basic System Setup**
```
  import con
  import test
  import ufirebase as firebase
  from machine import I2C, Pin
  import mpu6050
  import gps_sat
  from time import sleep
  from hcsr04 import HCSR04
  from servo import Servo
```
**Sensor Configuration:**
```
# Ultrasonic sensor setup
  sensor = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=1000000)

# I2C communication setup
  i2c = I2C(scl=Pin(22), sda=Pin(21))

# Servo motor initialization
  motor = Servo(pin=13)
  motor.move(0)
```
## **Main Control Loop:**
* Monitors accelerometer values for accident detection
* Tracks GPS location continuously
* Measures distance for parking assistance
* Sends data to Firebase in real-time
* Controls airbag deployment via servo motor

---
## **Test Results Summary**
**System Performance:**
* Successfully detects accidents based on accelerometer thresholds
* Provides accurate GPS tracking with latitude and longitude
* Implements parking assistance with distance measurements
* Achieves real-time data transmission to Firebase
* Demonstrates proper airbag deployment mechanism

**Safety Features:**
* Triggers warning signals when obstacles are detected within 7cm
* Activates multiple warning indicators (LED, buzzer) in case of accidents
* Deploys airbag system when acceleration exceeds safety thresholds
* Maintains continuous GPS tracking for location monitoring
---

## **Testimonial images :**
** IOT DEVICE
![image](https://github.com/AvilashBhowmick12/Smart-Car-Accident-Detection-System-IOT/blob/main/Project%20Images/WhatsApp%20Image%202024-01-19%20at%205.48.55%20PM.jpeg)

