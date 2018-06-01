from sense_hat import SenseHat
import os

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
cpu_temp = os.popen('/opt/vc/bin/vdgencmd measure_temp')
print(str(cpu_temp))
cputemp = cpu_temp.read()
cputemp = cputemp.replace('temp=','')
cputemp = cputemp.replace('\'C\n','')
cputemp = float(cputemp)
newtemp = temp - ((cputemp -temp) /2)

print(newtemp)
