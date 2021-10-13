__author__ = 'Taha yusuf'

#this is for python 3, for python 2: change input to raw_input
import serial

#Working Current Turns IP routing on,the setup management loopback interface,
#

#serial is the main module used and needs to be installed

import time

'''
start
'''

#creating your serial object
ser = serial.Serial(
    port = 'COM6', #COM is on windows, linux is different
    baudrate=9600, #many different baudrates are available
    parity='N',    #no idea
    stopbits=1,
    bytesize=8,
    timeout=8      #8 seconds seems to be a good timeout, may need to be increased
    )

#open your serial object
ser.isOpen()

#in this case it returns str COM3
print(ser.name)

command = 'no\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()


command = 'enable\n'

#convert str to binary (commands sent to switch must be binary)
command = str.encode(command)

#send the command to the switch
ser.write(command)

#wait a sec
time.sleep(0.5)
ser.inWaiting()

print('entering enable mode')

print('entering config mode.......')
#Enter Config mode
command = 'Config T\n'
Strcommand = str.encode(command)
ser.write(Strcommand)
print('inside Config mode!')


time.sleep(0.5)
ser.inWaiting()

#Enable dual stacking ipV4 & ipV6
#command = 'sdm prefer dual-ipv4-and-ipv6 default\n'
#Strcommand = str.encode(command)
#ser.write(Strcommand)
##
#time.sleep(0.5)
#ser.inWaiting()
#print('enabled dual stacking ipv4 & ipv6 NOTE: this is only required for 3750 & 3560X models')

#######Create loopback interface for management
command = 'Int lo1\n'
command = str.encode(command)
ser.write(command)
time.sleep(0.5)
ser.inWaiting()



command = 'description Management Loopback spine1 \n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()


command = 'IP address 192.168.1.1 255.255.255.255\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()


#Enable IP routing on layer 3 switch
command = 'IP routing\n' 
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()



#Enable OSPF 
command = 'ROUTER OSPF 1 \n' 
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()


#advertisement of all networks/interfaces on the layer 3 spine/leaf switch can be reached from anywhere on the network fabric
command = 'network 0.0.0.0 255.255.255.255 area 0\n' 
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()


#setup virtual terminal

command = 'line vty 0 4\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()



command = 'transport input ssh\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()



command = 'login local\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()





command = 'password 7\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()






command = 'line console 0\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()




command = 'logging synchronous\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()   




command = ' login local\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()



command = 'exit\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()




command = ' enable secret tame2011\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()





command = 'username tamedcobra password tanyatamirtame\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()



command = 'hostname spine1\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()



command = 'ip domain-name tamedcobra.local\n'
command = str.encode(command)
ser.write(command)
time.sleep(0.5)
ser.inWaiting()



command = 'crypto key generate rsa\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.9)
ser.inWaiting()



command = '2048\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.9)
ser.inWaiting()

command = 'ip ssh version 2\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.9)
ser.inWaiting()

command = 'do wr\n'
command = str.encode(command)
ser.write(command)

time.sleep(2.0)
ser.inWaiting()


command = 'exit\n'
command = str.encode(command)

ser.write(command)
time.sleep(0.5)
ser.inWaiting()

command = 'exit\n'
command = str.encode(command)
ser.write(command)

time.sleep(0.5)
ser.inWaiting()




#get the response from the switch
input_data = ser.read(8000) #(how many bytes to limit to read)

#convert binary to str
input_data = input_data.decode("utf-8", "ignore")

#print response
print(input_data)
