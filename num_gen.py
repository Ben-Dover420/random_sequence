import numpy as np

def number_generator(start, stop):
    # Asks for start and end value
    while start >= stop:
        start = int(input("Start value of intervall: "))
        stop = int(input("End value of intervall: "))

        if start >= stop: # If start value is greater than end value
            print("End value has to be greater than start value \n")

    numbers = np.arange(start, stop + 1) # [start, stop]
    length = len(numbers)

    while length > 0:
        index = np.random.randint(0, length) # Randomly generates index for numbers array
        chosen_number = numbers[index] # The chosen number from index

        print(f"Number {chosen_number}")

        numbers = np.delete(numbers, index) # Deletes chosen number from numbers array and replaces previous array
        length -= 1 # Length of numbers array has descreased by one. 