class RR:
    def __init__(self, queue, timeQuantum):
        self.queue = queue
        self.timeQuantum = timeQuantum
        self.readyQueue = []
        self.finishedProcesses = []
        self.time = 0
    

    def start(self):
        self.queue.sort(key=lambda x:(int(x.arrivalTime), int(x.pid)))
        self.processStart()
        #self.calculateWaitTime()
        self.printOutput()

    def processStart(self):
        timeGiven = self.timeQuantum
        ongoingProcess = None

        #while there is a queue or process 
        while(self.queue or self.readyQueue or ongoingProcess):
            
            #if queue is not empty and processes in queue arrived, add to ready queue
            while(self.queue and int(self.queue[0].arrivalTime) <= self.time):
                process = self.queue.pop(0)
                self.readyQueue.append(process)
            
            #ongoing process gets added last to ready queue if arrival time of new process is equal to end time of ongoing process
            if(ongoingProcess and timeGiven == 0): 
                    #print(f'FINISHED ONGOING PROCESS: pId: {ongoingProcess.pid} Curr time: {self.time}')
                    ongoingProcess.endTime.append(self.time)
                    
                    if(int(ongoingProcess.tempBurstTime)>0):
                        self.readyQueue.append(ongoingProcess)
                    else:
                        self.finishedProcesses.append(ongoingProcess)
                    ongoingProcess = None
            
            #if readyqueue is not empty and there isnt any ongoing processes
            if not ongoingProcess and self.readyQueue:
                #assign ongoing process
                ongoingProcess = self.readyQueue.pop(0)
                ongoingProcess.startTime.append(self.time)

                #print(f'NEW ONGOING PROCESS: pId: {ongoingProcess.pid} Curr time: {self.time}')

                timeGiven = min(self.timeQuantum, int(ongoingProcess.tempBurstTime))
            
            self.time += 1

            #if there is an ongoing process reduce time allocated
            if ongoingProcess:
                timeGiven -= 1
                ongoingProcess.tempBurstTime = int(ongoingProcess.tempBurstTime)-1

    # def calculateWaitTime(self):
    #     self.finishedProcesses.sort(key=lambda x:int(x.pid))

    #     for x in self.finishedProcesses:
    #         x.waitingTime = int(x.endTime[-1]) - int(x.arrivalTime) - int(x.burstTime)

    def printOutput(self):
        self.finishedProcesses.sort(key=lambda x:int(x.pid))
        waitingTimeSum = 0
        for x in self.finishedProcesses:
            for idx, (y,z) in enumerate(zip(x.startTime,x.endTime)):
                print(f'{x.pid}', end="")
                if idx == 0:
                    prevEnd = x.arrivalTime
                else:
                    prevEnd = x.endTime[idx-1]
                waitingTime = int(y) - int(prevEnd)
                x.waitingTime += waitingTime
                print(f' start time: {y} end time: {z} |', end="")
                print(f' Waiting time: {x.waitingTime}')
            waitingTimeSum += x.waitingTime 

        waitingTimeAve = waitingTimeSum/len(self.finishedProcesses)
        
        print(f'Average waiting time: {waitingTimeAve}')
