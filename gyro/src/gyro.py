#!/usr/bin/python3
import smbus
from time import sleep
import rospy
from std_msgs.msg import String


class Mpu6050():
	
    def __init__(self):

        # MPU6050 Registers addresses
        self.PWR_MGMT_1   = 0x6B
        self.SMPLRT_DIV   = 0x19
        self.CONFIG       = 0x1A
        self.GYRO_CONFIG  = 0x1B
        self.INT_ENABLE   = 0x38
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_ZOUT_H = 0x3F
        self.GYRO_XOUT_H  = 0x43
        self.GYRO_YOUT_H  = 0x45
        self.GYRO_ZOUT_H  = 0x47
	
	self.bus = smbus.SMBus(1)
        self.Device_Address = 0x68   # MPU6050 device address

	
	# Init MPU
        bus.write_byte_data(self.Device_Address, SMPLRT_DIV, 7)
        bus.write_byte_data(self.Device_Address, PWR_MGMT_1, 1)
        bus.write_byte_data(self.Device_Address, CONFIG, 0)
        bus.write_byte_data(self.Device_Address, GYRO_CONFIG, 24)
        bus.write_byte_data(self.Device_Address, INT_ENABLE, 1)
	
	
    def readData(self, addr):
        #Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(self.Device_Address, addr)
        low = self.bus.read_byte_data(self.Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
            value = value - 65536

        return value


    def mesure(self):
	    
	#Read Accelerometer raw value
        acc_x = self.readData(self.ACCEL_XOUT_H)
        acc_y = self.readData(self.ACCEL_YOUT_H)
        acc_z = self.readData(self.ACCEL_ZOUT_H)
	
        #Read Gyroscope raw value
        gyro_x = self.readData(self.GYRO_XOUT_H)
        gyro_y = self.readData(self.GYRO_YOUT_H)
        gyro_z = self.readData(self.GYRO_ZOUT_H)
	
        #Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0
	
        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0
	
	return {'Gx': Gx, 'Gy': Gy, 'Gz': Gz, 'Ax': Ax, 'Ay': Ay, 'Az': Az}
	



while True:
	
    sleep(1)
