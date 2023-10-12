from fcfs import FCFS
from rr import RR

class Process:
  def __init__(self, pid, arrivalTime, burstTime):
    self.pid = pid
    self.arrivalTime = arrivalTime
    self.burstTime = burstTime
    self.startTime = None
    self.endTime = None
    self.waitingTime = 0
    self.tempBurstTime = burstTime

def main():
#   The first line contains three integers separated by space, 𝑋 𝑌 𝑍.
# 𝑋 denotes the CPU scheduling algorithm.

# 𝑌 denotes the number of processes where 3 ≤𝑌 ≤100

# 𝑍 denotes a time quantum value (applicable for Round-Robin algorithm only), where 1 ≤ 𝑍 ≤ 100. 
# If the CPU scheduling algorithm indicated by the value of 𝑋 is not the Round-Robin algorithm, this value must be set to 1 but ignored.
  q = []
  x, y, z = input("Enter X, Y, Z: ").split()
  x = int(x)
  y = int(y)
  z = int(z)
# takes y number of processes
  for _ in range(y):
    pid, arrivalTime, burstTime = input("Enter processes: ").split()
    process = Process(pid, arrivalTime, burstTime)
    q.append(process)

  if x == 0:
    fcfs = FCFS(q)
    fcfs.start()
  
  if x == 3:
    rr = RR(q, z)
    rr.start()

if __name__ == "__main__":
    main()