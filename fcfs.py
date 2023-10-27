class FCFS:
  def __init__(self, queue):
    self.queue = queue
    self.timeCounter = 0
    self.totalWaiting = 0
    self.averageWaiting = 0
  def start(self):
    self.processStart()
    self.calculateWaitTime()
    self.printOutput()
  

  def processStart(self):
    #sufficient because fcfs is non preemptive so it will finish executing task before moving to the next
    self.queue.sort(key=lambda x:(int(x.arrivalTime), int(x.pid)))

    for process in range(0, len(self.queue)):
      if(int(self.queue[process].arrivalTime) > self.timeCounter):
         self.timeCounter += int(self.queue[process].arrivalTime)
      self.queue[process].startTime.append(self.timeCounter)
      self.timeCounter += int(self.queue[process].burstTime)
      self.queue[process].endTime.append(self.timeCounter)
      self.queue[process].waitingTime = int(self.queue[process].endTime[0]) - int(self.queue[process].burstTime) - int(self.queue[process].arrivalTime)

  def calculateWaitTime(self):
    for process in range(0, len(self.queue)):
      self.totalWaiting += int(self.queue[process].waitingTime)

    self.averageWaiting = self.totalWaiting / len(self.queue)

  def printOutput(self):
      self.queue.sort(key = lambda x:(int(x.pid), int(x.arrivalTime)))

      for x in self.queue:
          print(f'{x.pid}', end="")
          for y,z in zip(x.startTime,x.endTime):
              print(f' start time: {y} end time: {z} |', end="")
          print(f' Waiting time: {x.waitingTime}')

      
      print(f'Average waiting time: {self.averageWaiting}')
