class SJF:
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
      # for p in self.queue:
      #   print(f'Starting Queue: {p.__dict__}')
      # for p in self.readyQueue:
      #   print(f'Ready Queue: {p.__dict__}')
      

      while self.queue and self.shortestArrivalTime() == self.time:
        process, pidx = self.firstArrivedProcess()
        self.readyQueue.append(process)
        self.queue.pop(pidx)

      if processTime == 0 and ongoingProcess:
      # end the process once its process time is up
      # add the end time of the process
        ongoingProcess.endTime.append(self.time)
        # print(f'Ongoing process ended: {ongoingProcess.__dict__}')
        self.finishedProcesses.append(ongoingProcess)
        ongoingProcess = None

      # find the process that has the minimum burst time
      # check if the queue is not empty and no currently running processes

      if self.readyQueue and not ongoingProcess:
        # get the process that has the minimum burst time and assign it to ongoingProcess
        # add the start time of the process
        ongoingProcess, idx = self.minReadyProcess() 
        self.readyQueue.pop(idx)
        ongoingProcess.startTime.append(self.time)

        processTime = int(ongoingProcess.burstTime)
        # print(f'Ongoing process started: {ongoingProcess.__dict__}')

      self.time += 1

      #if there is an ongoing process reduce time allocated
      if ongoingProcess:
          processTime -= 1
        

  def calculateWaitTime(self):
      self.finishedProcesses.sort(key=lambda x:int(x.pid))

      for x in self.finishedProcesses:
          x.waitingTime = int(x.endTime[-1]) - int(x.arrivalTime) - int(x.burstTime)

  def printOutput(self):
      waitingTimeSum = 0
      for x in self.finishedProcesses:
          print(f'{x.pid}', end="")
          for y,z in zip(x.startTime,x.endTime):
              print(f' start time: {y} end time: {z} |', end="")
          print(f' Waiting time: {x.waitingTime}')
          waitingTimeSum += x.waitingTime 

      waitingTimeAve = waitingTimeSum/len(self.finishedProcesses)
      
      print(f'Average waiting time: {waitingTimeAve}')
  
  def minReadyProcess(self):
    # returns the process that has the minimum burst time and its index
    minp = self.readyQueue[0]
    i = 0
    idx = 0
    for p in self.readyQueue:
      if int(p.burstTime) < int(minp.burstTime):
        minp = p
        idx = i
      i += 1
    
    return minp, idx

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