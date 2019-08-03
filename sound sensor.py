import RPi.GPIO as IO
#import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input

while True:

    if(IO.input(14)==True): #object is far away
        IO.output(3,False) # Green led OFF
        print("No sound")
    
    if(IO.input(14)==False): #object is near
        IO.output(3,True) #Green led ON
        print("sound")
        
