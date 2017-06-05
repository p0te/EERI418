import numpy as np
import csv

reader=csv.reader(open('run_3_tacho.tsv' ,"rb"),delimiter='	')
x = list(reader)
data = np.array(x)
rows = data.shape[0]
arr = data[:,0].astype(float)


def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

arr_smooth = smooth(arr,20)





f1 = open('run_3_tacho_smoothed.tsv',"w")
for i in range(0,len(arr)):
	f1.write(str(arr_smooth[i]))
	f1.write('\n')
	





	
	

	
