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

def avg(arr):
    arr_to_return=np.zeros(len(arr[0]))
    for i in range(len(arr_to_return)):
        for j in range(len(arr)):
            arr_to_return[i]=arr_to_return[i]+arr[j][i]
    arr_to_return=arr_to_return/len(arr)
    return arr_to_return
def conv(s):
    try:
        s=float(s)
    except ValueError:
        pass    
    return s
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
def plot_thickness(keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets):
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
                            line=plt.plot(xdict[key],fdict[key], label=key)           
            leg = plt.legend(loc='lower right')
            plt.title(title_speed+", 8leaf, 500mm2, .001vs.002vs.003"+title_or)
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
            plt.xlim(0, 80)
            plt.show()
def plot_num_leaflets(keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets):
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
                            line=plt.plot(xdict[key],fdict[key], label=key)           
            leg = plt.legend(loc='lower right')
            plt.title(title_speed+", 500mm2, .002in, 4 vs 8 vs 10"+title_or )
            plt.xlim(0, 80)
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
            plt.show()
def plot_apertures(std,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets):
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
                            line=plt.plot(xdict[key],fdict[key], label=key)  
                            print(fdict[key]-std[key])
                            print(fdict[key]+std[key])
                            test=fdict[key]-std[key]
                            testy=fdict[key]+std[key]
                            plt.fill_between(xdict[key], test, testy)
                            #line=plt.plot(xdict[key],std[key], label= "std of "+key)         
            leg = plt.legend(loc='lower right')
            plt.title(title_speed+", 8leaf, .002in, 300vs.500vs.800"+title_or +" at 300,500,800")
            plt.xlim(0, 80)
            plt.show()
            for key in orientation:
            #plot 70m/s, 8leaf, .002in, 300vs.500vs.800 oulets subtracted by no leaf at 300,500,800
                if(keys_of_8leaf.count(key)!=0):
                    if(speed.count(key)!=0):
                        if(keys_of_002.count(key)!=0):
                            thing_to_subtract=get_thing_to_subtract("aperture",key,title_speed[0:2])
                            line=plt.plot(xdict[key],fdict[key]-fdict[thing_to_subtract], label=key)           
            leg = plt.legend(loc='lower right')
            plt.title(title_speed+", 8leaf, .002in, 300vs.500vs.800"+title_or +"subtracted by no leaf at 300,500,800")
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
    #get control to subtract
    for filename in os.listdir(path_of_control):
                if(filename!= '.DS_Store' ):
                    updated_path=path_of_control+ '/' + filename
                    for folder in os.listdir(updated_path):
                        if(folder!= '.DS_Store'):
                            x1, f1, t1= parse_mts_data_csv(updated_path + '/' + folder )
                            #print(control)
                            #print(len(control[0]))
                            for index in range(len(f1)):
                                control[0][index]=control[0][index]+f1[index]
                                control[1][index]=control[0][index]+x1[index]
                            num_trials=num_trials+1
    avg_control= control/num_trials
   # print(avg_control)
    #print(avg_control)
    keys=[]
    keys_of_inlets=[]
    keys_of_500=[]
    keys_of_300=[]
    keys_of_800=[]
    keys_of_8ms=[]
    keys_of_20ms=[]
    keys_of_002=[]
    keys_of_001=[]
    keys_of_003=[]
    keys_of_70ms=[]
    keys_of_outlets=[]
    keys_of_8leaf=[]
    keys_of_10leaf=[]
    keys_of_4leaf=[]
    fdict={}
    std={}
    xdict={}
    for testing in os.listdir(mts_data_path):
        #count=count+1
        if testing!='.DS_Store' :
            print(testing)
            keys.append(testing)
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
            ftemparray=np.zeros(830)
            xtemparray=np.zeros(830)
            stdtemparray=np.zeros((5,830))
            num_trials=0
            for filename in os.listdir(newpath):
                print(filename)
                if(filename!= '.DS_Store'):
                    updated_path=newpath+ '/' + filename
                    for temp in os.listdir(updated_path):
                        if(temp!= '.DS_Store'):
                            x1, f1, t1= parse_mts_data_csv(updated_path + '/' + temp)
                            for index in range(len(f1)):
                                ftemparray[index]=ftemparray[index]+f1[index]
                                xtemparray[index]=xtemparray[index]+x1[index]
                            num_trials=num_trials+1
            
            print(num_trials)
            fdict[testing]=ftemparray/num_trials
            xdict[testing]=xtemparray/num_trials
            num_trials=0
            for filename in os.listdir(newpath):
                print(filename)
                if(filename!= '.DS_Store'):
                    updated_path=newpath+ '/' + filename
                    for temp in os.listdir(updated_path):
                        if(temp!= '.DS_Store'):
                            x1, f1, t1= parse_mts_data_csv(updated_path + '/' + temp)
                            for index in range(len(f1)):
                                stdtemparray[num_trials,index]=(fdict[testing][index]-f1[index])**2

                            num_trials=num_trials+1
                    print(num_trials)
                    for n in range(num_trials-1):
                        std[testing]=stdtemparray[n]
    
    #plot all outlets
    for key in keys_of_outlets:
        line=plt.plot(xdict[key],fdict[key], label=key)             
    leg = plt.legend(loc='lower right')
    plt.show()
    #plot apertures
    plot_apertures(std,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets)
    #plot thicknesses
    plot_thickness(keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets)
    #plot num leaflets
    plot_num_leaflets(keys_of_500,keys_of_70ms,keys_of_20ms,keys_of_8ms,keys_of_8leaf,keys_of_002,xdict,fdict,keys_of_outlets,keys_of_inlets)

   

    #thing_to_plot='70ms_8leaf_300mm2_002in_out'
    #line=plt.plot(xdict[thing_to_plot],fdict[thing_to_plot], label=thing_to_plot)
    #thing_to_plot='70ms_8leaf_500mm2_002in_out'
    #line=plt.plot(xdict[thing_to_plot],fdict[thing_to_plot], label=thing_to_plot)
    #thing_to_plot='70ms_8leaf_800mm2_002in_out'
    #line=plt.plot(xdict[thing_to_plot],fdict[thing_to_plot], label=thing_to_plot)
    #plt.title("8 leaf 70 ms varying aperture outlet")
    #plt.show()

    

if __name__ == "__main__":
    main()

