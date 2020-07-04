# PrinterSimulation.py

from classes import Queue
import random


# If 20 tasks are generated per hour,
# on average, 1 task will be generated every 3 minutes, or 180 seconds
# Therefore, every second, the chance of a task will be 1/180

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.CurrentTask = None
        self.timeremaining = 0

    def tick(self):
        # Method for doing one unit of printing
        if self.CurrentTask is not None:
            self.timeremaining -= 1
            if self.timeremaining <= 0:
                self.CurrentTask = None

    def busy(self):
        if self.CurrentTask is None:
            return False
        else:
            return True

    def startNext(self, newtask):
        self.CurrentTask = newtask
        self.timeremaining  = newtask.getPages() * 60 / self.pagerate

class Task:
    def __init__(self,time):
        self.pages = random.randint(1,21)
        self.timestamp = time

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp


def simulation(duration,pagesPerMinute):

    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waiting_times = []

    for CurrentSecond in range(duration):
        if newtask():
            task = Task(CurrentSecond)
            printQueue.enqueue(task)
        if (not labPrinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.dequeue()
            waiting_times.append(nexttask.waitTime(currenttime=CurrentSecond))
            labPrinter.startNext(nexttask)

            labPrinter.tick()
        averageWait = sum(waiting_times) / len(waiting_times)

        print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newtask():
    num = random.randint(1,180)

    if num == 180:
        return True
    else:
        return False

