import sys
lenargv=len(sys.argv)
print(lenargv)
def printa():
	print ("a")
def printb():
	print("b")
def printc():
	print("c")
options={
	'a':printa,
	'b':printb,
	'c':printc,
}
i=1;
while i<lenargv:
	options[sys.argv[i]]()
	print ("sys.argv content",sys.argv[i])
	i=i+1
#print (sys.argv[2])
#print (sys.argv[3])
	
