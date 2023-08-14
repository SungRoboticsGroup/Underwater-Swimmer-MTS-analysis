# libraies to include
import matplotlib.pyplot as plt 
import os
import numpy as np
#import pandas as pd 
import scipy.io
import csv
#from pattern_utils import *

DEBUG = True
if DEBUG:
    import pdb

# plot setting parameters
font_type = 'Times New Roman'
font_size = '24'

plt.rcParams['font.family'] = font_type
plt.rcParams['font.size'] = font_size

# file path
mts_data_path = 'valve_characterization'

# this helper function reads in a csv file, and returns the x,f, and t values, 
# where x is the vertical displacement array, f is the force array, and t is the time array
def parse_mts_data_csv(data_path):
    with open(data_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        arr_to_return=np.zeros((830,3))
        for i in range(8):
            test=csv_reader.next()
        for i in range(830):
            test=csv_reader.next()
            arr_to_return[i][0]=float(test[0])
            arr_to_return[i][1]=float(test[1])
            arr_to_return[i][2]=float(test[2])
        x=arr_to_return[0:,0]
        f=arr_to_return[0:,1]
        t=arr_to_return[0:,2]
    return x,f,t
# If we are subtracting a control experiment, this function identifies the correct control based on the key
def get_thing_to_subtract(str,key,speed):
    if str=='aperture':
        if(speed=="8m"):
            speed="8"
        if('300' in key):
                thing_to_subtract=speed+"ms_empty_300mm2"
        if('500' in key):
                thing_to_subtract=speed+"ms_empty_500mm2"
        if('800' in key):
                thing_to_subtract=speed+"ms_empty_800mm2"
    return thing_to_subtract
# This creates 3 kinds of plots to show the effects of varying thickness. It plots the raw data, the mean with standard deviation, 
# and one which normalizes by subtracting the control
def plot_thickness(xdictraw,fdictraw,std,keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets):
    speeds=[keys_of_70ms,keys_of_20ms,keys_of_8ms]
    orientations=[keys_of_outlets,keys_of_inlets]
    count=0
    for speed in speeds:
        count=count+1
        if(count==1):
                title_speed="70ms"
        if(count==2):
                title_speed="20ms"
        if(count==3):
                title_speed="8ms"
        county=0
        for orientation in orientations:
            county=county+1
            if(county==1):
                title_or="outlet"
            if(county==2):
                title_or="inlet"
           
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 outlets  at 300,500,800
            for key in orientation:
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_500.count(key)!=0):
                            line, =plt.plot(xdict[key],fdict[key], label=key) 
                            c=line.get_color()
                            test=fdict[key]-std[key]
                            testy=fdict[key]+std[key]
                            plt.fill_between(xdict[key], test, testy,color=c, alpha=.5)          
            leg = plt.legend(loc='lower right')
            #leg = plt.legend(bbox_to_anchor=(1.05, 1.05))
            plt.title(title_speed+", 8leaf, 500mm2, .001vs.002vs.003"+title_or)
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.xlim(0, 80)
            plt.show()

            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 outlets  at 300,500,800
            for key in orientation:
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_500.count(key)!=0):
                            for count in range(5):
                                line, =plt.plot(xdictraw[key][count],fdictraw[key][count], label=key+" trial # "+ str(count+1) )  
                                               
            leg = plt.legend(loc='lower right', fontsize='xx-small', ncol=3)
            #leg = plt.legend(bbox_to_anchor=(1.05, 1.05))
            plt.title(title_speed+", 8leaf, 500mm2, .001vs.002vs.003 "+title_or + " raw data")

            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.xlim(0, 80)
            plt.show()
            for key in orientation:
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 oulets subtracted by no leaf at 300,500,800
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_500.count(key)!=0):
                            thing_to_subtract=get_thing_to_subtract("aperture",'500',title_speed[0:2])
                            line=plt.plot(xdict[key],fdict[key]-fdict[thing_to_subtract], label=key)           
            leg = plt.legend(loc='lower right')
            plt.title(title_speed+", 8leaf, 500mm2, .001vs.002vs.003"+title_or +"subtracted by 70ms no leaf at 500")
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.xlim(0, 80)
            plt.show()
# This creates 3 kinds of plots to show the effects of varying number of leaflets. It plots the raw data, the mean with standard deviation, 
# and one which normalizes by subtracting the control
def plot_num_leaflets(xdictraw,fdictraw,std,keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets):
    speeds=[keys_of_70ms,keys_of_20ms,keys_of_8ms]
    orientations=[keys_of_outlets,keys_of_inlets]
    count=0
    for speed in speeds:
        count=count+1
        if(count==1):
                title_speed="70ms"
        if(count==2):
                title_speed="20ms"
        if(count==3):
                title_speed="8ms"
        county=0
        for orientation in orientations:
            county=county+1
            if(county==1):
                title_or="outlet"
            if(county==2):
                title_or="inlet"
           
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 outlets  at 300,500,800
            for key in orientation:
                if(keys_of_500.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            line, =plt.plot(xdict[key],fdict[key], label=key)   
                            c=line.get_color()
                            test=fdict[key]-std[key]
                            testy=fdict[key]+std[key]
                            plt.fill_between(xdict[key], test, testy,color=c, alpha=.5)                  
            leg = plt.legend(loc='lower right')
            #leg = plt.legend(bbox_to_anchor=(1.05, 1.05))
            plt.title(title_speed+", 500mm2, .002in, 4 vs 8 vs 10"+title_or )
            plt.xlim(0, 80)
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.show()
            #plot raw 70m/s, 8leaf, .002in, 300vs.500vs.800 outlets  at 300,500,800
            for key in orientation:
                if(keys_of_500.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            for count in range(5):
                                line, =plt.plot(xdictraw[key][count],fdictraw[key][count], label=key+" trial # "+ str(count+1) )  
                                c=line.get_color()                 
            leg = plt.legend(loc='lower right', fontsize='xx-small', ncol=3)
            #leg = plt.legend(bbox_to_anchor=(1.05, 1.05))
            plt.title(title_speed+", 500mm2, .002in, 4 vs 8 vs 10 "+title_or + " raw data")
            plt.xlim(0, 80)
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.show()
            for key in orientation:
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 oulets subtracted by no leaf at 300,500,800
                if(keys_of_500.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            thing_to_subtract=get_thing_to_subtract("aperture","500",title_speed[0:2])
                            line=plt.plot(xdict[key],fdict[key]-fdict[thing_to_subtract], label=key)           
            leg = plt.legend(loc='lower right')
            plt.title(title_speed+", 500mm2, .002in, 4 vs 8 vs 10"+title_or +"subtracting no leaf at 500")
            plt.xlim(0, 80)
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.show()
# This creates 3 kinds of plots to show the effects of varying aperture size. It plots the raw data, the mean with standard deviation, 
# and one which normalizes by subtracting the control
def plot_apertures(xdictraw, fdictraw, std,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets):
    speeds=[keys_of_70ms,keys_of_20ms,keys_of_8ms]
    orientations=[keys_of_outlets,keys_of_inlets]
    count=0
    for speed in speeds:
        count=count+1
        if(count==1):
                title_speed="70ms"
        if(count==2):
                title_speed="20ms"
        if(count==3):
                title_speed="8ms"
        county=0
        for orientation in orientations:
            county=county+1
            if(county==1):
                title_or="outlet"
            if(county==2):
                title_or="inlet"
           
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 outlets  at 300,500,800
            for key in orientation:
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            line, =plt.plot(xdict[key],fdict[key], label=key)  
                            c=line.get_color()
                            test=fdict[key]-std[key]
                            testy=fdict[key]+std[key]
                            plt.fill_between(xdict[key], test, testy,color=c, alpha=.5)        
            leg = plt.legend(loc='lower right', fontsize='xx-small')
            plt.xlim(0, 80)
            #plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0)
            plt.title(title_speed+", 8leaf, .002in, 300vs.500vs.800"+title_or +" at 300,500,800")
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.show()
            #plot raw data
            for key in orientation:
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            for count in range(5):
                                line =plt.plot(xdictraw[key][count],fdictraw[key][count], label=key+" trial # "+ str(count+1) )  
            
            leg = plt.legend(loc='lower right', fontsize='xx-small', ncol=3)
            plt.xlim(0, 80)
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            #plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0)
            plt.title(title_speed+", 8leaf, .002in, 300vs.500vs.800 "+title_or +" at 300,500,800 " + " raw data")
            plt.show()
            
            for key in orientation:
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 oulets subtracted by no leaf at 300,500,800
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            thing_to_subtract=get_thing_to_subtract("aperture",key,title_speed[0:2])
                            line=plt.plot(xdict[key],fdict[key]-fdict[thing_to_subtract], label=key)           
            leg = plt.legend(loc='lower right', fontsize='xx-small')
            plt.title(title_speed+", 8leaf, .002in, 300vs.500vs.800"+title_or +"subtracted by no leaf at 300,500,800")
            plt.xlabel("displacement (MM)")
            plt.ylabel("Force (N)")
            plt.xlim(0, 80)
            plt.show()
            


def main():
    path_of_control='valve_characterization/20ms_novalve'
    #number of trials
    rows=0
    #number of data pts
    cols=0
    control=np.zeros((3,830))
    num_trials=0
    #the following arrays store the strings that correspond to the names of each file.
    #They are sorted into arrays based on type for easier sorting
    #all keys
    keys=[]
    #keys of all inlet directional tests
    keys_of_inlets=[]
    #keys of all outlet directional tests
    keys_of_outlets=[]
    #keys of aperture sizes (500 mm^2, 300 mm^2, 800 mm^2)
    keys_of_500=[]
    keys_of_300=[]
    keys_of_800=[]
    #keys of speeds (8 m/s, 20 m/s, 70 m/s)
    keys_of_8ms=[]
    keys_of_20ms=[]
    keys_of_70ms=[]
    #keys of thicknesses (.01 cm, .02 cm, .03 cm)
    keys_of_002=[]
    keys_of_001=[]
    keys_of_003=[]
    #keys of # of leaflets (4,8,10)
    keys_of_8leaf=[]
    keys_of_10leaf=[]
    keys_of_4leaf=[]
    #dictionary of averages, where the key is the filename
    fdict={}
    xdict={}
    #dictionary of raw vales, where the key is the filename
    fdictraw={}
    xdictraw={}
    #dictionary of standard deviations, where the key is the filename
    std={}
    
    #iterate through each test name in the folder
    for testing in os.listdir(mts_data_path):
        if testing!='.DS_Store' :
            print(testing)
            keys.append(testing)
            #sort the tests based on their speed, thickness, number of leaflets, and aperture size
            if("001" in testing):
                keys_of_001.append(testing)
            if("002" in testing):
                keys_of_002.append(testing)
            if("003" in testing):
                keys_of_003.append(testing)
            if("500" in testing):
                keys_of_500.append(testing)
            if("300" in testing):
                keys_of_300.append(testing)
            if("800" in testing):
                keys_of_800.append(testing)
            if("8ms" in testing):
                keys_of_8ms.append(testing)
            if("20ms" in testing):
                keys_of_20ms.append(testing)
            if("70ms" in testing):
                keys_of_70ms.append(testing)
            if("in_out" in testing):
                keys_of_outlets.append(testing)
            if("in_in" in testing):
                keys_of_inlets.append(testing)
            if("8leaf" in testing):
                keys_of_8leaf.append(testing)
            if("4leaf" in testing):
                keys_of_4leaf.append(testing)
            if("10leaf" in testing):
                keys_of_10leaf.append(testing)
            newpath=mts_data_path + '/'+testing
            #make temporary arrays
            num_trials=0
            tempfdictraw=np.zeros((5,830))
            xdictraw[testing]=np.zeros((5,830))
            for filename in os.listdir(newpath):
                print(filename)
                if(filename!= '.DS_Store'):
                    updated_path=newpath+ '/' + filename
                    #iterate through all 5 trials
                    for temp in os.listdir(updated_path):
                        if(temp!= '.DS_Store'):
                            x1, f1, t1= parse_mts_data_csv(updated_path + '/' + temp)
                            #fill arrays
                            for index in range(len(f1)):
                                tempfdictraw[num_trials][index]=f1[index]
                                xdictraw[testing][num_trials][index]=x1[index]
                            num_trials=num_trials+1
            #store raw data and standard deviation
            fdictraw[testing]=tempfdictraw
            temparray=np.zeros(830)
            for index in range(830):
                value=np.std([tempfdictraw[0][index],tempfdictraw[1][index],tempfdictraw[2][index],tempfdictraw[3][index],tempfdictraw[4][index]])
                temparray[index]=value
            std[testing]=temparray
            totalf=np.zeros(830)
            totalx=np.zeros(830)
            #compute averages
            for i in range(5):
                totalf=totalf+tempfdictraw[i]
                totalx=totalx+xdictraw[testing][i]
            fdict[testing]=totalf/5
            xdict[testing]=totalx/5
            num_trials=0
        
    
    #plot all outlets
    for key in keys_of_outlets:
        line=plt.plot(xdict[key],fdict[key], label=key)             
    leg = plt.legend(loc='lower right')
    plt.show()
    #plot apertures
    #plot_apertures(xdictraw,fdictraw,std,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets)
    #plot thicknesses
    plot_thickness(xdictraw,fdictraw,std,keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets)
    #plot num leaflets
    #plot_num_leaflets(xdictraw,fdictraw,std,keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets)

    

if __name__ == "__main__":
    main()

