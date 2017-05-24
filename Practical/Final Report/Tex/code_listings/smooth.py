import numpy as np
import csv

reader=csv.reader(open('Motor_start_all.tsv' ,"rb"),delimiter='	')
x = list(reader)
data = np.array(x)
rows = data.shape[0]
arr_time = data[:-(26),0].astype(float)
arr_volt = data[:,1].astype(float)
arr_rpm = data[:,2].astype(float)

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

arr_volt_smooth = smooth(arr_volt,1000)
arr_rpm_smooth = smooth(arr_rpm,1000)




f1 = open('Motor_start_combined_smoothed.tsv',"wb")
writer = csv.writer(f1,delimiter = "	")
for i in range(0,len(arr_time)):
	writer.writerow((arr_time[i]-26,arr_volt_smooth[i],arr_rpm_smooth[i]))
	





	
	

	
