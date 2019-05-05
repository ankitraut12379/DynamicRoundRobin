import time
import heapq
def Scheduling(Arrival,Burst):
	clock=0
	n=len(Arrival)
	ReadyQueue=[]
	heapq.heapify(ReadyQueue)
	Completion=[0 for i in range(len(Burst))]	# clock time at completion
	Copy=[]		# to detect if a process is already transferred to ReadyQueue
	for i in range(len(Arrival)):	#puting in process with arrival time minimum in ReadyQueue
		if Arrival[i]==0:
			heapq.heappush(ReadyQueue,[Burst[i],i])
			n=n-1
			Copy.append(i)
	timequanta=average(ReadyQueue)
	while len(ReadyQueue)!=0 or (n!=0):	#Implementation
		i=heapq.heappop(ReadyQueue)
		if i[0]<=timequanta:
			clock=clock+i[0]
			Completion[i[1]]=clock
			for i in range(len(Arrival)):# Appending arrived processes in ReadyQueue
				if Arrival[i]<=clock and (i not in Copy) :
					heapq.heappush(ReadyQueue,[Burst[i],i])
					n=n-1
					Copy.append(i)
					timequanta=average(ReadyQueue)
			if len(ReadyQueue)==0 and n!=0: # While CPU is idle
				l=len(Copy)
				x=Arrival[l]
				heapq.heappush(ReadyQueue,[Burst[l],l])
				clock=Arrival[l]
				Copy.append(l)
				n=n-1
		else:
			i[0]=i[0]-timequanta
			clock=clock+timequanta
			if (Burst[i[1]]-i[0])>timequanta:
				heapq.heappush(ReadyQueue,i)
			else:
				clock=clock+i[0]
				Completion[i[1]]=clock
				if len(ReadyQueue)==0 and n!=0: # While CPU is IDLE
					l=len(Copy)
					x=Arrival[l]
					heapq.heappush(ReadyQueue,[Burst[l],l])
					clock=Arrival[l]
					Copy.append(l)
					n=n-1
			for i in range(len(Arrival)):	# Appending arrived Processes in ReadyQueue
				if Arrival[i]<=clock and (i not in Copy):
					heapq.heappush(ReadyQueue,[Burst[i],i])
					n=n-1
					timequanta=average(ReadyQueue)

	print(Completion)		
	Waiting=[]
	TurnAround=[]
	for i in range(len(Completion)): #Calculation of AWT and ATT
		Waiting.append(Completion[i]-Arrival[i]-Burst[i])
		TurnAround.append(Completion[i]-Arrival[i])
	print('Average Waiting Time is : ',sum(Waiting)/(len(Arrival)),'\nAverage TurnAround Time is :',sum(TurnAround)/len(Arrival))


def average(ReadyQueue):#Function to calculate average of burst time of processes present in ReadyQueue
	average=0
	for i in ReadyQueue:
		average=average+i[0]
	return average/len(ReadyQueue)




'''Calling Function and Calculating Time Taken'''
def main():
	Arrival=[0,1,2,3,9,1000]
	Burst=[5,10,5,9,4,11919191]
	x=time.time()
	m=min(Arrival)
	for i in range(len(Arrival)):
		Arrival[i]=Arrival[i]-m
	print(Arrival)
	Scheduling(Arrival,Burst)
	y=(time.time()-x)
	print(y) #Time taken
if __name__ == '__main__':
	main()