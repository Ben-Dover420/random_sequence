import numpy as np

def randSeq(start, stop):
    if start.isnumeric() and stop.isnumeric(): # If stop and start are numbers
        first, end = int(start), int(stop)
        random_numbers = [] # Empty array 
        numbers = np.arange(first, end + 1) # [start, stop]
        length = len(numbers)

        while length > 0:
            index = np.random.randint(0, length) # Randomly generates index for numbers array
            random_numbers.append(numbers[index]) # The chosen number from index

            numbers = np.delete(numbers, index) # Deletes chosen number from numbers array and replaces previous array
            length -= 1 # Length of numbers array has descreased by one.

        return random_numbers
    
    if start.isalpha() and stop.isalpha(): # If stop and start are letters
        print("no")
        return [0]