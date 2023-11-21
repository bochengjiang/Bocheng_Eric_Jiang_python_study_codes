import time
import turtle

t=turtle.Pen()
t.ht()
seconds_first_place = 0
seconds_tenth_place = 0
min_first_place = 0
min_tenth_place = 0

for i in range (60):
    for i in range (60):
        t.write("0"+"0"+":"+str(seconds_tenth_place)+str(seconds_first_place),font=("Arial",100,"bold"))
        #time.sleep(1)
        seconds_first_place = seconds_first_place+1
        t.clear()
        if seconds_first_place>9:
            seconds_tenth_place = seconds_tenth_place+1
            seconds_first_place = 0
            seconds = str(seconds_tenth_place)+str(seconds_first_place)
            #print(type(seconds),seconds)
    for i in range(60):
        if str(seconds_tenth_place)+str(seconds_first_place)=="59":
            seconds_first_place = 0
            seconds_tenth_place = 0
            t.write(str(min_tenth_place)+str(min_first_place)+":"+str(seconds_tenth_place)+str(seconds_first_place),font=("Arial",100,"bold"))
            min_first_place = min_first_place+1
            time.sleep(1)
            t.clear()
            print ("min_first_place = "+str(min_first_place))
            if min_first_place>9:
                min_first_place = 0
                min_tenth_place = min_tenth_place+1

