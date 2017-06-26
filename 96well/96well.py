import serial
import time
import os
import datetime

Ycordinates = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}

def GetDate():
        today = datetime.datetime.now()
        strtoday = str(today)
        newstring = strtoday.replace(" ","_")
        newstring = newstring.replace(":","_")
        newstring = newstring.replace("-","_")
        newstring = newstring.replace(".","_")
        return newstring


def MoveDown(n):
	ser = serial.Serial('/dev/ttyACM0', 38400, timeout=4)
	for a in range(n):
		ser.write('MV - Y,CCW,30500')	
		time.sleep(65)

def MoveUp(n):
        ser = serial.Serial('/dev/ttyACM0', 38400, timeout=4)
        for a in range(n):
                ser.write('MV - Y,CW,30500')
                time.sleep(65)

def MoveRight(n):
        ser = serial.Serial('/dev/ttyACM0', 38400, timeout=4)
        for a in range(n):
                ser.write('MV - X,CW,30500')
                time.sleep(44)

def MoveLeft(n):
        ser = serial.Serial('/dev/ttyACM0', 38400, timeout=4)
        for a in range(n):
                ser.write('MV - X,CCW,30500')
                time.sleep(44)

def ColDown(exp,col,strt,num):
	try:
		os.stat(exp)
	except:
		os.mkdir(exp)
	end = strt + (num - 1)
	i = strt
	rowname = Ycordinates[i]
	well = exp+'/'+rowname+str(col)
	try:
		os.stat(well)
	except:
		os.mkdir(well)
	
	
	file = well+'/'+str(GetDate())+'_pic.jpg'
	os.system('raspistill -awb sun -t 2000 -o '+file)
	for a in range(strt,end,1):
		i = i - 1
		rowname = Ycordinates[i] 
		well = exp+'/'+rowname+str(col)
		file = well+"/"+str(GetDate())
		file = file+'_pic.jpg'
		try:
			os.stat(well)
		except:
			os.mkdir(well)
	        MoveDown(1)	
		os.system('raspistill -awb sun -t 2000 -o '+file)



def ColUp(exp,col,strt,num):
        try:
                os.stat(exp)
        except:
                os.mkdir(exp)
        end = strt + (num - 1)
        i = strt
        rowname = Ycordinates[i]
        well = exp+'/'+rowname+str(col)
        try:
                os.stat(well)
        except:
                os.mkdir(well)
        file = well+'/'+str(GetDate())+'_pic.jpg'
        os.system('raspistill -awb sun -t 2000 -o '+file)
        for a in range(strt,end,1):
                i = i + 1
                rowname = Ycordinates[i]
                well = exp+'/'+rowname+str(col)
                file = well+"/"+str(GetDate())
		file = file+'_pic.jpg'
                try:
                        os.stat(well)
                except:
                        os.mkdir(well)
                MoveUp(1)
                os.system('raspistill -awb sun -t 2000 -o '+file)


def pixarray(exp,col,strt,num):
	
	upstrt = strt - 3
	for a in range(num):
		ColDown(exp,col,strt,4)
		MoveRight(1)
		col = col + 1
		ColUp(exp,col,upstrt,4)
	        if (a < num):
			MoveRight(1)	
			col = col + 1

def Cross():
	
	ser.write('MV - X,CW,5000')
        os.system('raspistill -awb sun -t 8000 -o pica.jpg')
	time.sleep(8)
	
	ser.write('MV - X,CCW,10000')
	os.system('raspistill -awb sun -t 16000 -o picb.jpg')
	time.sleep(16)

	ser.write('MV - X,CW,5000')
        time.sleep(8)

	ser.write('MV - Y,CW,5000')
        os.system('raspistill -awb sun -t 11000 -o picc.jpg')
        time.sleep(11)

	ser.write('MV - Y,CCW,10000')
        os.system('raspistill -awb sun -t 22000 -o picd.jpg')
        time.sleep(22)

	ser.write('MV - Y,CW,5000')
        time.sleep(11)
#global ser

ser = serial.Serial('/dev/ttyACM0', 38400, timeout=4)
time.sleep(3)
ser.write('color - 255,0,0')
time.sleep(5)
#pixarray("testexp4",4,6,2)
#MV = Moves,  "Y" Stands for the Y Axis, CW = ClockWise, "17000" = number of steps
ser.write('MV - Y,CW,17000')


os.system('raspistill -awb sun -t 40000 -o testpic.jpg')



