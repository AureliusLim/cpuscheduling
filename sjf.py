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
      # check if there is a process in the initial queue and append it to the ready queue once the time of a process has elapsed
      while self.queue:
        process = self.queue.pop(0)
        self.readyQueue.append(process)
      # find the process that has the minimum burst time
      # check if the queue is not empty and no currently running processes
      if self.readyQueue and not ongoingProcess:
        # get the process that has the minimum burst time and assign it to ongoingProcess
        ongoingProcess = self.minReadyProcess() 

        

  def calculateWaitTime(self):
    pass
   
  def printOutput(self):
    pass  
  
  def minReadProcess(self):
    # returns the process that has the minimum burst time
    minp = self.readyQueue[0]
    for p in self.readyQueue:
      if p.burstTime < minp:
        minp = p

    return minp
