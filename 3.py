import serial           # import the module
import wake_word
ComPort = serial.Serial('/dev/rfcomm5') # open COM24
ComPort.baudrate = 9600 # set Baud rate to 9600
ComPort.bytesize = 8    # Number of data bits = 8
ComPort.parity   = 'N'  # No parity
ComPort.stopbits = 1    # Number of Stop bits = 1
# Write character 'A' to serial port
n=0 
wordig=["forward","left","right","stop","backward"]
while n==0:
    print("new")
    out=0
    paths = ['./triggers/goahead_linux.ppn','./triggers/go_left_linux.ppn','./triggers/go_right_linux.ppn', './triggers/stop_bot_linux.ppn','./triggers/go_back_linux.ppn']
    out = wake_word.trigger_detect(paths)
    text=wordig[out]
    print(text)
    data = bytearray(text, 'utf-8')
    ComPort.write(data)
    #name=input()
    if text=="s":
        n=1

ComPort.close()    
