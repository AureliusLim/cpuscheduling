import sys
from fcfs import FCFS
from sjf import SJF
from srtf import SRTF
from rr import RR

class Process:
  def __init__(self, pid, arrivalTime, burstTime):
    self.pid = pid
    self.arrivalTime = arrivalTime
    self.burstTime = burstTime
    self.startTime = []
    self.endTime = []
    self.waitingTime = 0
    self.tempBurstTime = burstTime

#Return true if valid else false
def checkValidInputs(input):
  # Check if only 3 inputs per line
  x = input.split()
  if len(x) != 3:
    print("Invalid input: Only 3 inputs per line allowed")
    return False
  
  # Check if integer input
  try:
    inputList = [int(y) for y in x]
  except ValueError:
    print("Invalid input: Noninteger input is not allowed")
    return False
  
  # Check for negative nonzero inputs
  for i in inputList:
    if i < 0:
      print("Invalid input: Negative inputs is not allowed")
      return False
    
  # Check if last input is greater than 0
  if inputList[-1] <= 0:
    print("Invalid input: Burst time should be greater than 0")
    return False 

  return True

#Return true if valid else false
def checkValidFirstLine(input):
  x,y,z = input.split()
  x,y,z = int(x),int(y),int(z)
  
  #check if algorithm id is between 0 and 3
  if x < 0 or x > 3:
    print("Invalid input: Invalid scheduling algorithm id")
    return False
  #check if number of processes is between 3 and 100
  elif y < 3 or y > 100:
    print("Invalid input: Number of processes should only be between 3 and 100 inclusively")
    return False
  #check if time quantum is between 1 and 100
  elif z < 1 or z > 100:
    print("Invalid input: Time quantum should only be between 1 and 100 inclusively")
    return False
  
  return True

# Return true if not duplicate id else false
def checkDuplicateId(input, idList):
  # Check inputted ID is not in id list (Checking for unique id)
  id = input.split()[0]

  if id in idList:
    print("Invalid input: Duplicate Process ID is not allowed")
    return False
  
  return True

def main():
#   The first line contains three integers separated by space, 𝑋 𝑌 𝑍.
# 𝑋 denotes the CPU scheduling algorithm.

# 𝑌 denotes the number of processes where 3 ≤𝑌 ≤100

# 𝑍 denotes a time quantum value (applicable for Round-Robin algorithm only), where 1 ≤ 𝑍 ≤ 100. 
# If the CPU scheduling algorithm indicated by the value of 𝑋 is not the Round-Robin algorithm, this value must be set to 1 but ignored.
  q = []
  ids = []
  tempInputs = input().strip()

  while not checkValidInputs(tempInputs) or not checkValidFirstLine(tempInputs):
      sys.stdin.flush()
      tempInputs = input().strip()

  x,y,z = tempInputs.split()

  x = int(x)
  y = int(y)
  z = int(z)

  if x != 3:
    z = 1
# Takes y number of processes
  for _ in range(y):
  
    sys.stdin.flush()
    tempInputs = input().strip()

    while not checkValidInputs(tempInputs) or not checkDuplicateId(tempInputs, ids):
      sys.stdin.flush()
      tempInputs = input().strip()

    pid, arrivalTime, burstTime = tempInputs.split()
    process = Process(pid, arrivalTime, burstTime)
    ids.append(process.pid)
    q.append(process)

  if x == 0:
    fcfs = FCFS(q)
    fcfs.start()
  elif x == 1:
    sjf = SJF(q)
    sjf.start()
  elif x == 2:
    srtf = SRTF(q)
    srtf.start()
  elif x == 3:
    rr = RR(q, z)
    rr.start()

if __name__ == "__main__":
    main()