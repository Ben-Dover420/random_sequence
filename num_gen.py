import numpy as np
import random

start, stop = 1, 0

# Asks for start and end value
while start >= stop:
    start = int(input("Start value of intervall: "))
    stop = int(input("End value of intervall: "))

    if start >= stop: # If start value is greater than end value
        print("End value has to be greater than start value \n")

numbers = np.arange(start, stop + 1) # [start, stop]
length = len(numbers)

print(f"Numbers array: {numbers}")
print(f"Current length: {length}")

index = random.randint(0, length - 1) # Randomly generates index for numbers list
chosen_num = numbers[index]


print(f"Chosen number: {chosen_num}")

numbers = np.delete(numbers, chosen_num) # Removes chosen number from numbers array 
length = len(numbers) # New length

print(f"Numbers array: {numbers}")
print(f"Current length: {length}")


#while length > 0:
