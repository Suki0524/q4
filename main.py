time = int(input('Please set your timer in minutes: ') * 60
b = time.CLOCK_REALTIME
while time.CLOCK_REALTIME - b < time:
 pass
print('Time's up!')
 
