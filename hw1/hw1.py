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
		#print (datar)
		#datar.rsplit()
		#ss.rsplit(" ")
		
		#print (len(datar))
		data.append(datar.split(","))
		#data.append(data1)
		#data1=[]
#print data
file.close()
"""
for x in data:
	print (x)
print (len(data))
"""

#for Average monthly income
Amale_smoke_population = []
Afemale_smoke_population = []
At=[]
Atotal_population = []
Asmo_popu_eachclass = []
Ap_total = 0
for i in range(12,15):
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
                #print (man_smo_p)
                woman_smo_p = woman_p*woman_smo_r/100
                #print (woman_smo_p)
                total_p = man_p+woman_p
                #print (total_p)
                #print (man_smo_p+woman_smo_p)
                Atotal_smo_r = (man_smo_p + woman_smo_p)/total_p*100
                Atotal_population.append(Atotal_smo_r)
                Amale_smoke_population.append(str(man_smo_r))
                Afemale_smoke_population.append(str(woman_smo_r))
                At.append(str(data[i][0]))
                Asmo_popu_eachclass.append(man_smo_p+woman_smo_p)
                Ap_total=Ap_total+total_p
Alist1 = [float(x) for x in Amale_smoke_population]
Alist2 = [float(x) for x in Afemale_smoke_population]
Alist3 = [float(x) for x in Atotal_population]

#for Working Environment
Wmale_smoke_population = []
Wfemale_smoke_population = []
Wt=[]
Wtotal_population = []
Wsmo_popu_eachclass = []
Wp_total = 0
for i in range(8,11):
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
                #print (man_smo_p)
                woman_smo_p = woman_p*woman_smo_r/100
                #print (woman_smo_p)
                total_p = man_p+woman_p
                #print (total_p)
                #print (man_smo_p+woman_smo_p)
                Wtotal_smo_r = (man_smo_p + woman_smo_p)/total_p*100
                Wtotal_population.append(Wtotal_smo_r)
                Wmale_smoke_population.append(str(man_smo_r))
                Wfemale_smoke_population.append(str(woman_smo_r))
                Wt.append(str(data[i][0]))
                Wsmo_popu_eachclass.append(man_smo_p+woman_smo_p)
                Wp_total=Wp_total+total_p
Wlist1 = [float(x) for x in Wmale_smoke_population]
Wlist2 = [float(x) for x in Wfemale_smoke_population]
Wlist3 = [float(x) for x in Wtotal_population]

#for Education level
male_smoke_population = []
female_smoke_population = []
t=[]
total_population = []#store ratio within each class
smo_popu_eachclass = []#for pie chart
p_total=0;
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
		#print (man_smo_p)
		woman_smo_p = woman_p*woman_smo_r/100 
		#print (woman_smo_p)
		total_p = man_p+woman_p
		#print (total_p)
		#print (man_smo_p+woman_smo_p)
		total_smo_r = (man_smo_p + woman_smo_p)/total_p*100 
		total_population.append(total_smo_r)
		male_smoke_population.append(str(man_smo_r))
		female_smoke_population.append(str(woman_smo_r))
		t.append(str(data[i][0]))
		smo_popu_eachclass.append(man_smo_p+woman_smo_p)
		p_total=p_total+total_p

#print (total_population)
#print (t)
#print (male_smoke_population)
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
flag=1
while flag<len(sys.argv):
	command=sys.argv[flag]
	
	#bar chart
	#plt.plot(t,list1)
	fig, ax=plt.subplots()
	if command[2]=='b':
		width=0.25  #the width of the bars
		if command[1]=='E':
			l1=list1
			l2=list2
			l3=list3
			tt=t
			ax.set_xlabel("Education level")
			ax.set_title("Smoking percentage vs Education level")
		elif command[1]=='W':
			l1=Wlist1
			l2=Wlist2
			l3=Wlist3
			tt=Wt
			ax.set_xlabel("Working environment")
			ax.set_title("Smoking percentage vs Working environment")
		else: 
			l1=Alist1
			l2=Alist2
			l3=Alist3
			tt=At
			ax.set_xlabel("Average monthly income")
			ax.set_title("Smoking percentage vs Average monthly income")
		ind=range(len(l1))  #the x locations of the group
		ind_left = ind
		ind_middle = [x+width for x in ind]
		ind_right = [x+width*2 for x in ind]
		rects1 = ax.bar(ind_left ,l1,width,color='b')
		rects2 = ax.bar(ind_middle ,l2,width,color='r')
		rects3 = ax.bar(ind_right, l3,width,color='y')
		ax.set_xticks(ind_middle)

		ax.set_xticklabels(tt,minor=False)
		for x,y in enumerate(l1):
			plt.text(x,y,'%.1f' % y,ha="center",va="bottom")
		for x,y in enumerate(l2):
			plt.text(x+width,y,'%.1f' % y, ha="center", va="bottom")
		for x,y in enumerate(l3):
			plt.text(x+2*width,y,'%.1f' % y,ha="center",va="bottom")
		ax.set_ylabel("Smoking Percentage(%)")
		"""
		#plt.plot(mm,list1,'r')
		#plt.xticks(mm,t,rotation="vertical")
		"""
		label_string=['Male','Female','Total']
		plt.legend(handles=[rects1,rects2,rects3],labels=label_string)
		plt.show()

	#line chart
	#fig ,ax=plt.subplots()
	if command[2]=='l':
		if command[1]=='E':
			ind=[x for x in range(len(list1))]
			l1=list1
			l2=list2
			l3=list3
			tt=t
			plt.title("Smoking percentage vs Education level")
			plt.xlabel("Education level")
		elif command[1]=='W':
			ind=[x for x in range(len(Wlist1))]
			l1=Wlist1
			l2=Wlist2
			l3=Wlist3
			tt=Wt
			plt.title("Smoking percentage vs Working environment")
			plt.xlabel("Working environment")
		else:
			ind=[x for x in range(len(Alist1))]
			l1=Alist1
			l2=Alist2
			l3=Alist3
			tt=At
			plt.title("Smoking percentage vs Average monthly income")
			plt.xlabel("Average monthly income")

		a,=plt.plot(ind,l1,color='r')
		b,=plt.plot(ind,l2,color='g')
		c,=plt.plot(ind,l3,color='b')
		ax.set_xticks(ind)
		ax.set_xticklabels(tt,minor=False)

		plt.ylabel("Smoking Percentage(%)")
		label_string=['Male','Female','Total']
		plt.legend(handles=[a,b,c],labels=label_string)

		for x,y in enumerate(l1):
			plt.text(x,y,'%.1f' % y,ha="center",va="bottom")
		for x,y in enumerate(l2):
			plt.text(x,y,'%.1f' % y,ha="center",va="bottom")
		for x,y in enumerate(l3):
			plt.text(x,y,'%.1f' % y,ha="center",va="bottom")
		ax.set_ylim(ymin=0)
		plt.show()



	#pie chart
	#smoking percectage of every classes
	if command[2]=='p':
		if command[1]=='E':
			aa=smo_popu_eachclass
			total = p_total
			colors=["blue","orange","green","red","purple"]
			label=t
			plt.title("Proportion of different education level in smoking population")
		elif command[1]=='W':
			aa=Wsmo_popu_eachclass
			total = Wp_total
			colors=["red","orange","green"]
			label=Wt
			plt.title("Proportion of different working environment in smoking population")
		else:
			aa=Asmo_popu_eachclass
			total = Ap_total
			colors=["red","orange","green"]
			label=At
			plt.title("Proportion of different average monthly income in smoking population")
		listp=[float(x)*100/total for x in aa]
		#labels=t
		#colors=["blue","orange","green","red","purple"]
		patches,l_text,p_text = plt.pie(listp,labels=label,colors=colors,labeldistance=1.1,autopct="%3.1f%%",shadow=False,pctdistance=0.6)

		for x in l_text:
			x.set_size=(30)
		for x in p_text:
			x.set_size=(20)
		plt.axis("equal")
		#plt.legend()
		plt.show()

	flag=flag+1





