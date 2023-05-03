import numpy as np

start, stop = 1,0

while start >= stop:
    start = int(input("Start value of intervall: "))
    stop = int(input("End value of intervall: "))
    if start >= stop:
        print("You stupid bastard, you've got no brain \n")

numbers = np.arange(start, stop+1)