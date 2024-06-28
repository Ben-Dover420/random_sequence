import numpy as np

def randSeq(start, stop): # Handles the default cases: numbers and letters. 
    random = []
    first = ord(start) if start.isalpha() else int(start)
    end = ord(stop) if stop.isalpha() else int(stop)
    elements = np.arange(first, end + 1) # [first, end]
    length = len(elements)

    while length > 0: 
        index = np.random.randint(0, length) # Randomly generates index for numbers array
        random.append(elements[index]) # The chosen number from index

        elements = np.delete(elements, index) # Deletes chosen number from numbers array and replaces previous array
        length -= 1 # Length of numbers array has descreased by one.
    
    random = [chr(element) for element in random] if start.isalpha() and stop.isalpha() else random # Converts back to unicode if we are randomising letters.

    return random