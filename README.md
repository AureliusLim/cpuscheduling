## About the project
A project that simulates the following CPU scheduling algorithms:

• First-Come-First-Serve (FCFS)

• Shortest-Job First (SJF)

• Shortest-Remaining-Time-First (SRTF)

• Round-Robin (RR)


## Input
The program reads the following from standard input:

• The first line contains three integers separated by space, 𝑋 𝑌 𝑍.

• 𝑋 denotes the CPU scheduling algorithm.

• 𝑌 denotes the number of processes where 3 ≤𝑌 ≤100

• 𝑍 denotes a time quantum value (applicable for Round-Robin algorithm only), where 1 ≤ 𝑍 ≤ 100. If the CPU scheduling algorithm indicated by the value of 𝑋 is not the Round-Robin algorithm, this value must be set to 1 but ignored.

• See Table 1 below for the CPU scheduling algorithm and the corresponding value of 𝑋.

CPU Scheduling Algorithm	| Value of X
|------|----|
FCFS | 0
SJF |	1
SRTF |	2
RR	| 3

Table 1. CPU Scheduling Algorithms and their corresponding value of 𝑋.

• There will be 𝑌 lines of space-separated integers 𝐴 𝐵 𝐶 where 𝐴 is the process ID, 𝐵 is the arrival time, and 𝐶 is the burst time.

## Output
The output of the program should include 𝑌 lines of processes with the process ID, start time, end time, and total waiting time where start time, end time, waiting time ≥ 0. If there are multiple start and end times for each process, display them in order. The output should be sorted according to the process ID. An additional last line at the end is the average waiting time of the processes. See the table with the sample input and output below.

### Sample input
```
0 4 20
1 0 19
2 11 1
3 16 10
4 20 2
```

### Sample output
```
1 start time: 0 end time: 19 | Waiting time: 0
2 start time: 19 end time: 20 | Waiting time: 8
3 start time: 20 end time: 30 | Waiting time: 4
4 start time: 30 end time: 32 | Waiting time: 10
Average waiting time: 5.5
```

## Running the app
To run the app, enter this command in the terminal:

```
python app.py
```

If you don't like typing your inputs in the terminal, you can place them in a file called `input.txt` and run this command.

```
python app.py < input.txt 
```