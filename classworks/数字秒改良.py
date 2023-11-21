import time
import turtle

#initialization
t=turtle.Pen()
t.ht()
seconds_first_place = 0
seconds_tenth_place = 0
min_first_place = 0
min_tenth_place = 0
hour_first_place = 0
hour_tenth_place = 0


for a in range(24): #hour number control loop
    for b in range (60): #min number control loop
        for c in range (60): #sec number control loop
            #initializing clock display
            t.write("{}{}:{}{}:{}{}".format(hour_tenth_place, hour_first_place, min_tenth_place,min_first_place,seconds_tenth_place,seconds_first_place),font=("Arial",100,"bold"))#str(min_tenth_place)+str(min_first_place)+":"+str(seconds_tenth_place)+str(seconds_first_place),font=("Arial",100,"bold"))
            #control sec first place number
            #time.sleep(1)
            seconds_first_place = seconds_first_place+1
            t.clear()
            #control sec tenth place number
            if seconds_first_place>9:
                seconds_tenth_place = seconds_tenth_place+1
                seconds_first_place = 0
                seconds = str(seconds_tenth_place)+str(seconds_first_place)
                #print(type(seconds),seconds)
        # determin is it time to move to min
        if str(seconds_tenth_place)+str(seconds_first_place)=="60":
            #clear number of sec
            seconds_first_place = 0
            seconds_tenth_place = 0
            #control min first place number
            min_first_place = min_first_place+1
            #control min second place number
            if min_first_place>9:
                min_first_place = 0
                min_tenth_place = min_tenth_place+1
    # determin is it time to move to hour
    if str(min_tenth_place)+str(min_first_place)=="60":
        #clear number of min
        min_first_place = 0
        min_tenth_place = 0
        #control hour first place
        hour_first_place = hour_first_place+1
        #control hour tenth place
        if hour_first_place>9:
            hour_first_place = 0
            hour_tenth_place = hour_tenth_place+1    

