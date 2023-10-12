class FCFS:
  def __init__(self, queue):
    self.queue = queue

  def start(self):
    print(self.queue[0].pid)
    print(self.queue[0].arrivalTime)
    print(self.queue[0].burstTime)
    # prints all executed processes
