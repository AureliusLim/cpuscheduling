class SRTF:
  def __init__(self, queue):
    self.queue = queue
    self.readyQueue = []
    self.finishedProcesses = []
    self.time = 0

  def start(self):
      self.processStart()
      self.calculateWaitTime()
      self.printOutput()

  def processStart(self):
    ongoingProcess = None
    processTime = 0
    # check if there are any remaining or current processes
    while self.queue or self.readyQueue or ongoingProcess:
      # check if there is a process in the initial queue and the shortest arrivaltime of the process in the queue is equal to the counter time
      # and append it to the ready queue
      # print(f'arrival time: {self.shortestArrivalTime()}')
      #for p in self.queue:
      #  print(f'Starting Queue: {p.__dict__}')
      #for p in self.readyQueue:
      #  print(f'Ready Queue: {p.__dict__}')
      

      while self.queue and self.shortestArrivalTime() == self.time:
        process, pidx = self.firstArrivedProcess()
        self.readyQueue.append(process)
        # print(f'Queue: {self.queue.pop(pidx).__dict__}')
        self.queue.pop(pidx)

      if ongoingProcess:
        if processTime == 0:
          # end the process once its process time is up
          # add the end time of the process
          ongoingProcess.endTime.append(self.time)
          # print(f'Ongoing process ended: {ongoingProcess.__dict__}')
          self.finishedProcesses.append(ongoingProcess)
          self.readyQueue.remove(ongoingProcess)
          ongoingProcess = None
        elif self.readyQueue:
          if processTime>int(self.minReadyProcess().tempBurstTime): #so every second we compare the current process remaining burst time to the ones in ready queue instead of only when its finished
            ongoingProcess.endTime.append(self.time)
            # print(f'Ongoing process temporarily ended and back to ready queue: {ongoingProcess.__dict__}') #technically it never left ready queue
            ongoingProcess = None



      # find the process that has the minimum burst time
      # check if the queue is not empty and no currently running processes

      if self.readyQueue and not ongoingProcess:
        # get the process that has the minimum burst time and assign it to ongoingProcess
        # add the start time of the process
        ongoingProcess = self.minReadyProcess() 
        # print(f'Ready Queue: {self.readyQueue.pop(idx).__dict__}')
        ongoingProcess.startTime.append(self.time)

        processTime = int(ongoingProcess.tempBurstTime)
        # print(f'Ongoing process started: {ongoingProcess.__dict__}')

      self.time += 1
      # print(f'counter: {self.time}')

      #if there is an ongoing process reduce time allocated
      if ongoingProcess:
          processTime -= 1
          ongoingProcess.tempBurstTime = processTime
          #print(f'process time: {processTime}')
        

  def calculateWaitTime(self):
      self.finishedProcesses.sort(key=lambda x:int(x.pid))

      for x in self.finishedProcesses:
          x.waitingTime = int(x.endTime[-1]) - int(x.arrivalTime) - int(x.burstTime)

  def printOutput(self):
      self.finishedProcesses.sort(key=lambda x:int(x.pid))
      waitingTimeSum = 0
      for x in self.finishedProcesses:
        lastEndTime = x.arrivalTime
        for y,z in zip(x.startTime,x.endTime):
          print(f'{x.pid} start time: {y} end time: {z} | Waiting time: {y-int(lastEndTime)}')
          lastEndTime = z
        waitingTimeSum += x.waitingTime

      waitingTimeAve = waitingTimeSum/len(self.finishedProcesses)
      
      print(f'Average waiting time: {waitingTimeAve}')
  
  def minReadyProcess(self):
    # returns the process that has the minimum remaining burst time
    minp = self.readyQueue[0]
    for p in self.readyQueue:
      if int(p.tempBurstTime) < int(minp.tempBurstTime):
        minp = p
    
    return minp

  def firstArrivedProcess(self):
    # returns the process that has the shortest arrival time and its index
    minp = self.queue[0]
    i = 0
    idx = 0
    for p in self.queue:
      if int(p.arrivalTime) < int(minp.arrivalTime):
        minp = p
        idx = i
      i += 1
    
    return minp, idx
  
  def shortestArrivalTime(self):
    # returns the shortest arrival time
    minp = self.queue[0]
    for p in self.queue:
      if int(p.arrivalTime) < int(minp.arrivalTime):
        minp = p
    
    return int(minp.arrivalTime)