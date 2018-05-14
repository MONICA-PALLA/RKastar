from numpy import *
import matplotlib.pyplot as plt


def cityReadSACO():
	x,y=loadtxt('city_data.txt', unpack = True)
	order=loadtxt('Data.txt')
	#d = loadtxt('phero.txt', unpack= True)
	print order
	x1=[]
	y1=[]
#	print d.shape
	for RM in order:
	#	print "RK : %d" % RK
	#	print "order : %s" % order
		x1.append(x[int(RM)])
		y1.append(y[int(RM)])
	x1.append(x[int(order[0])])
	y1.append(y[int(order[0])])
	plt.figure('S-ACO', (8,6), 80, 'w', 'k')	
	plt.plot(x1,y1, marker='x', linestyle = '--', color = 'r', label = 'S-ACO')
	for RM in range(len(order)):
		plt.text(x1[RM],y1[RM],int(order[RM]+1))
	plt.show() 

def main():
    cityReadSACO()


if __name__=="__main__":
	main()
