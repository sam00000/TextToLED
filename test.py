import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
for i in range(18, 26):
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

dict = {
    'A': [8, 16, 24, 48, 64, 88, 96, 104, 128, 144, 168, 184],
    'B': [0, 8, 16, 40, 56, 80, 88, 96, 120, 136, 160, 168, 176],
    'C': [0, 8, 16, 24, 32, 40, 80, 120, 160, 168, 176, 184, 192],
    'D': [0, 8, 16, 24, 40, 72, 80, 112, 120, 152, 160, 168, 176, 184],
    'E': [0, 8, 16, 24, 40, 80, 88, 96, 104, 120, 160, 168, 176, 184],
    'F': [0, 8, 16, 24, 40, 80, 88, 96, 104, 120, 160],
    'G': [0, 8, 16, 24, 32, 40, 80, 104, 112, 120, 152, 160, 168, 176, 184, 192],
    'H': [0, 32, 40, 72, 80, 88, 96, 104, 112, 120, 152, 160, 192],
    'I': [0, 8, 16, 24, 32, 56, 96, 136, 160, 168, 176, 184, 192],
    'J': [0, 8, 16, 24, 32, 56, 96, 136, 160, 168, 176],
    'K': [0, 24, 40, 56, 80, 88, 120, 136, 160, 184],
    'L': [0, 40, 80, 120, 160, 168, 176, 184, 192],
    'M': [0, 8, 16, 24, 32, 40, 56, 72, 80, 96, 112, 120, 136, 152, 160, 192],
    'N': [0, 8, 16, 24, 32, 40, 72, 80, 112, 120, 152, 160, 192],
    'O': [0, 8, 16, 24, 32, 40, 72, 80, 112, 120, 152, 160, 168, 176, 184, 192],
    'P': [0, 8, 16, 24, 32, 40, 72, 80, 88, 96, 104, 112, 120, 160],
    'Q': [0, 8, 16, 24, 32, 40, 72, 80, 112, 120, 128, 136, 144, 152, 176],
    'R': [0, 8, 16, 24, 32, 40, 72, 80, 88, 96, 104, 112, 120, 128, 160, 176],
    'S': [0, 8, 16, 24, 32, 40, 80, 88, 96, 104, 112, 152, 160, 168, 176, 184, 192],
    'T': [0, 8, 16, 24, 32, 56, 96, 136, 176],
    'U': [0, 32, 40, 72, 80, 112, 120, 152, 160, 168, 176, 184, 192],
    'V': [0, 32, 40, 72, 88, 104, 128, 144, 176],
    'W': [0, 32, 40, 72, 80, 96, 112, 128, 144, 168, 184],
    'X': [0, 32, 48, 64, 96, 128, 144, 160, 192],
    'Y': [0, 32, 48, 64, 96, 136, 176],
    'Z': [0, 8, 16, 24, 32, 64, 96, 128, 160, 168, 176, 184, 192]
}
def findletter(ch, dict):
    for i in dict:
        gay = dict[ch]
        if(ch in dict.keys()):
            gay = dict[ch]
            print gay
            for i in range(0,3):
                for j in range(1, len(dict[ch])):
                    gay.append(i + dict[ch][j])

printit = str(raw_input("What do you want to type")).upper()
for ch in printit:
    print ch
    for n in range(0, 1):
        print findletter(ch, dict)
        for i in findletter(ch, dict):
            bitstr=str("{0:08b}".format(i))
            print bitstr
            for j in range(7,-1,-1):
       	        if int(bitstr[j]) == 0:
		    GPIO.output(j+18, 0)
	        elif int(bitstr[j]) == 1:
		    GPIO.output(j+18, 1)
            time.sleep(0.05)
'''
for i in range(0, 128):
    bitstr=str('0.08b'.format(i))
    for i in range(0, 8):
        GPIO.output(i+18, bit(bitstr[i]))

        GPIO.output(i+18, int(bitstr[i]))
    #waits 1 second before moving to the next LED
    time.sleep(1)
    for i in range(0, 8):
        GPIO.output(i+18, 0)
'''
'''
for i in range(0, 8):
    GPIO.output(i+18, 1)
    time.sleep(2)
    GPIO.output(i+18, 0)
'''
