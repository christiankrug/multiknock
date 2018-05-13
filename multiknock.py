import time
import subprocess
NextURLNo = 0
MaxProcesses = 20
with open("airlines.txt") as f:
    urllist = f.read().splitlines()
MaxUrls = len(urllist)
Processes = []

def StartNew():
   """ Start a new subprocess if there is work to do """
   global NextURLNo
   global Processes

   if NextURLNo < MaxUrls:
      proc = subprocess.Popen(['knockpy', '-c', urllist[NextURLNo]])
      print ("Started to Process 	#"+NextURLNo+"/"+MaxUrls, urllist[NextURLNo])
      NextURLNo += 1
      Processes.append(proc)

def CheckRunning():
   """ Check any running processes and start new ones if there are spare slots."""
   global Processes
   global NextURLNo

   for p in reversed(range(len(Processes))): # Check the processes in reverse order
      if Processes[p].poll() is not None: # If the process hasn't finished will return None
         del Processes[p] # Remove from list - this is why we needed reverse order

   while (len(Processes) < MaxProcesses) and (NextURLNo < MaxUrls): # More to do and some spare slots
      StartNew()

if __name__ == "__main__":
   CheckRunning() # This will start the max processes running
   while (len(Processes) > 0): # Some thing still going on.
      time.sleep(0.1) # You may wish to change the time for this
      CheckRunning()

   print ("Done!")
