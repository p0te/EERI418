import numpy as np
import csv

reader=csv.reader(open('test.csv' ,"rb"),delimiter='	')
x = list(reader)
data = np.array(x)
rows = data.shape[0]
arr_time = data[:,0].astype(float)
arr_col1 = data[:,1].astype(float)

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

arr_col1_smooth = smooth(arr_volt,1000)



f = open('output.csv',"wb")
writer = csv.writer(f,delimiter = "	")
for i in range(0,len(arr_time)):
	writer.writerow((arr_time[i],arr_col1_smooth[i]))

print arr_time
print arr_volt


	
	

	
