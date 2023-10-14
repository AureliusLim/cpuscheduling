class SJF:
  def __init__(self, queue):
    self.queue = queue
    self.readyQueue = []
    self.finishedProcesses = []
    self.time = 0

  def start(self):
    pass

  def processStart(self):
    ongoingProcess = None
    # check if there are any remaining or current processes
    while self.queue or self.readyQueue or ongoingProcess:
      # check if there is a process in the initial queue and the shortest arrivaltime of the process in the queue is equal to the counter time
      # and append it to the ready queue
      while self.queue and self.shortestArrivalTime == self.time:
        process, pidx = self.firstArrivedProcess()
        self.readyQueue.append(process)
        self.queue.pop(pidx)
      # find the process that has the minimum burst time
      # check if the queue is not empty and no currently running processes
      if self.readyQueue and not ongoingProcess:
        # get the process that has the minimum burst time and assign it to ongoingProcess
        # add the start time of the process
        ongoingProcess, idx = self.minReadyProcess() 
        self.readyQueue.pop(idx)
        ongoingProcess.startTime.append(self.time)

      elif ongoingProcess:
      # end the process once it is done processing
      # add the end time of the process
        ongoingProcess = None
        ongoingProcess.endTime.append(self.time)

      self.time += 1
        

  def calculateWaitTime(self):
    pass
   
  def printOutput(self):
    pass  
  
  def minReadyProcess(self):
    # returns the process that has the minimum burst time and its index
    minp = self.readyQueue[0]
    i = 0
    for p in self.readyQueue:
      if p.burstTime < minp:
        minp = p
        idx = i
      i += 1
    
    return minp, idx

  def firstArrivedProcess(self):
    # returns the process that has the shortest arrival time and its index
    minp = self.queue[0]
    i = 0
    for p in self.queue:
      if p.arrivalTime < minp:
        minp = p
        idx = i
      i += 1
    
    return minp, idx
  
  def shortestArrivalTime(self):
    # returns the shortest arrival time
    minp = self.queue[0]
    for p in self.queue:
      if p.arrivalTime < minp:
        minp = p
    
    return minp.arrivalTime