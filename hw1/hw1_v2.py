#/usr/bin/python
import urllib
#import csv
import ssl
import sys
import matplotlib.pyplot as plt
#from pyplot import *

ssl._create_default_https_context = ssl._create_unverified_context

link = "https://ceiba.ntu.edu.tw/course/481ea4/hw1_data.csv"
#file=urllib.urlopen(link)
urllib.request.urlretrieve(link,"hw1_data")
#myfile=file.read()
#print myfile
#reader = csv.reader(file("hw1_data.csv"))
#file=open("hw1_data","r")
i=0;
data=[]
data1=[]
with open("hw1_data","r") as file:
	while True:
		datar=file.readline()
		if not datar: break
		#ss=datar
		if datar == "\n":
			continue
		datar.rsplit()
		datar=datar[:len(datar)-1]
		datar.rsplit(' ')
		print (datar)
		#datar.rsplit()
		#ss.rsplit(" ")
		
		print (len(datar))
		data.append(datar.split(","))
		#data.append(data1)
		#data1=[]
"""
		data1.append(datar.split(","))
		#print data1
		ss=data1[i][3]
		data1[i].pop()
		ss.rsplit("\n")
		data1[i].extend(ss)
		i=i+1
		data.append(data1)
		data1=[]
"""
#print data
file.close()
for x in data:
	print (x)
print (len(data))
"""
print "\n=========================\n"

string="abc,defghijklmnopqrstuvwxyz"
string2="aaaaaaaaaaaa,aaaaaa"
ss=[]
ss.append(string.split(","))
ss.append(string.split(","))
print ss
"""
#ParseData=[]
#for line in reader:
#	print line

#print(file.read())
#for line in file:
#	x=line.split(',')[3]
#	print(x)

#s=file.split("\n")
#for line in s:
#	print(line)

male_smoke_population = []
female_smoke_population = []
t=[]
total_population = []
tmp=0
for i in range(2,7):
	try:
		man_p=float(data[i][1])
	except ValueError:
		pass
	else:
		#deal with total population ratio
		man_p       = float(data[i][1])
		woman_p     = float(data[i][3])
		man_smo_r   = float(data[i][2])
		woman_smo_r = float(data[i][4])
		man_smo_p   = man_p*man_smo_r/100
		print (man_smo_p)
		woman_smo_p = woman_p*woman_smo_r/100 
		print (woman_smo_p)
		total_p = man_p+woman_p
		print (total_p)
		print (man_smo_p+woman_smo_p)
		total_smo_r = (man_smo_p + woman_smo_p)/total_p*100 
		#print total_smo_r
		#only store ratio
		total_population.append(total_smo_r)
		#tmp=float(data[i][2])*value/100
		male_smoke_population.append(str(man_smo_r))
		#value=float(data[i][3])
		#tmp=float(data[i][4])*value/100
		female_smoke_population.append(str(woman_smo_r))
		#print data[i][0]
		t.append(str(data[i][0]))
print (total_population)
print (t)
print (male_smoke_population)
list1 = [float(x) for x in male_smoke_population]
#print list1
#mm=[x for x in range(len(t))]
list2 = [float(x) for x in female_smoke_population]
list3 = [float(x) for x in total_population]
"""
plt.bar(range(len(list1)),list1)
plt.bar(range(len(list2)),list2)
plt.bar(range(len(list3)),list3)
plt.xticks(range(len(list1)),t,size='small')
"""
#plt.plot(t,list1)
width=0.25  #the width of the bars
ind=range(len(list1))  #the x locations of the group
ind_left = ind
ind_middle = [x+width for x in ind]
ind_right = [x+width*2 for x in ind]
#ind_add_width=[x-width for x in ind]	
#ind_add_width2=[x+width/2 for x in ind]
fig, ax=plt.subplots()
rects1 = ax.bar(ind_left ,list1,width,color='b')
rects2 = ax.bar(ind_middle ,list2,width,color='r')
rects3 = ax.bar(ind_right, list3,width,color='y')
ax.set_xticks(ind_middle)

#fig.canvas.draw()
#labels=[item.get_text() for item in ax.get_xticklabels()]
#labels[1]="testing"
#plt.plot(mm,list1)
#ax.set_xticks(list1)
ax.set_xticklabels(t,minor=False)

"""
plt.plot(mm,list1,'r')
plt.xticks(mm,t,rotation="vertical")
"""
plt.legend()
plt.show()



