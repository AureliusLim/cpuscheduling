class RR:
    def __init__(self, queue, timeQuantum):
        self.queue = queue
        self.timeQuantum = timeQuantum
        self.readyQueue = []
        self.finishedProcesses = []
        self.time = 0
    

    def start(self):
        self.queue.sort(key=lambda x:x.arrivalTime)
        self.processStart()
        self.calculateWaitTime()
        self.printOutput()

    def processStart(self):
        timeGiven = self.timeQuantum
        ongoingProcess = None

        #while there is a queue or process 
        while(self.queue or self.readyQueue or  ongoingProcess):
            #if queue is not empty and processes in queue arrived, add to ready queue
            if(self.queue and int(self.queue[0].arrivalTime) <= self.time):
                while(self.queue and int(self.queue[0].arrivalTime) <= self.time):
                    process = self.queue.pop(0)
                    self.readyQueue.append(process)
            
            #if readyqueue is not empty and there isnt any ongoing processes
            if not ongoingProcess and self.readyQueue:
                #assign ongoing process
                ongoingProcess = self.readyQueue.pop(0)
                if(ongoingProcess.startTime == None):
                    ongoingProcess.startTime = self.time

                #print(f'NEW ONGOING PROCESS: pId: {ongoingProcess.pid} Curr time: {self.time}')

                timeGiven = min(self.timeQuantum, int(ongoingProcess.tempBurstTime))

            #if there is an ongoing process
            if ongoingProcess:
                self.time += 1
                timeGiven -= 1
                ongoingProcess.tempBurstTime = int(ongoingProcess.tempBurstTime)-1
                if(timeGiven == 0): 
                    #print(f'FINISHED ONGOING PROCESS: pId: {ongoingProcess.pid} Curr time: {self.time}')
                    if(int(ongoingProcess.tempBurstTime)>0):
                        self.readyQueue.append(ongoingProcess)
                    else:
                        ongoingProcess.endTime = self.time
                        self.finishedProcesses.append(ongoingProcess)
                    ongoingProcess = None
                    timeGiven = self.timeQuantum
            else:
                self.time += 1

    def calculateWaitTime(self):
        self.finishedProcesses.sort(key=lambda x:x.pid)

        for x in self.finishedProcesses:
            x.waitingTime = int(x.endTime) - int(x.arrivalTime) - int(x.burstTime)

    def printOutput(self):
        for x in self.finishedProcesses:
            print(f'{x.pid} start time: {x.startTime} end time: {x.endTime} | Waiting time: {x.waitingTime}')

        waitingTimeAve = sum(x.waitingTime for x in self.finishedProcesses)/len(self.finishedProcesses)
        
        print(f'Average waiting time: {waitingTimeAve}')
