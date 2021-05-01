"""
***************************************************************
* Class Name: Queue
* Author: Brogan Avery
* Created: 2021-02-13
***************************************************************
"""
from QueueLab.LabCode.QueueFullException import QueueFullException
from QueueLab.LabCode.QueueEmptyException import QueueEmptyException

class Queue:
    def __init__(self, max_size=5):
        self.head = 0 # the next item to come out of queue
        self.tail = -1 # last item put in and last to come out
        self.size = 0 # how many memory boxes are currently in use
        self.max_size = max_size # this is the max amount of elements the queue can hold
        self.items = ["" for x in range(max_size)] # the queue array

    def is_empty(self):
        """
        Function to check if associated list is empty.
        :return: Returns a bool.
        """
        # Return statement.
        return self.size == 0 #  if the size of the queue is 0 it means that none of the boxes in the array are being occupied

    def is_full(self):
        """
        Function to check if associated list is full.
        :return: Returns a bool.
        """
        # Return statement.
        return self.size == self.max_size # this does the opposite of is_empty so if all the memory spots in the array are full nothing else can fit in it

    def enqueue(self, item): # puts an item in the line (end of queue)
        """
        Default enqueue function for stack emulation.
        :param item: Required string.
        :return: No return.
        """
        if not self.is_full(): # makes sure there is available space in queue array
            if self.is_empty(): # adding to the line when the queue is empty
                self.head = 0      # the first three just make sure it is initialized back to the values for an empty queue
                self.tail = -1
                self.size = 0
                self.tail += 1 # says the tail is now the last (but also the first here) element in the queue by pointing to the index that comes right  after the current index of tail
                self.size += 1 # also keeps track that the queue just grew by one size
                self.items[self.tail] = item # puts what ever value we want to add to end of line by putting it in the index of the new tail that was just changed
            else:
                if self.tail + 1 == self.max_size:   # if the tail is already pointing to the last (via the second to last of where it is now) possible index (the max size), it will not re-assign tail to the next index over since that would be out side the bounds of the array
                    self.tail = 0   # does not change so that if we tried to add another after this it would error
                    self.size += 1  # grows so it will now be == to maxSize
                    self.items[self.tail] = item # puts what ever value we want to add to end of line by putting it in the index of the new tail that was just changed
                else: # this would be the most normal outcome. for if the queue was not empty, full, or almost full
                    self.tail += 1   # same as if the queue was empty only the tail just keeps getting tacked onto end
                    self.size += 1
                    self.items[self.tail] = item  # puts what ever value we want to add to end of line by putting it in the index of the new tail that was just changed  
        else:
            # Raise exception.
            raise QueueFullException

    def dequeue(self):    # this is very much like the opposite of enqueue
        """
        Default dequeue function for stack data type.
        :return: No return.
        """
        item_str = "" # string to hold the content of head index

        if not self.is_empty(): # in the case the queue is not empty
            if self.is_full():   # removing from the queue when it is full
                if self.head + 1 == self.max_size: # when everything has almost gone through and out the queue
                    item_str = self.items[self.head]   # captures the value in the head index
                    self.items[self.head] = ""  # to "remove" it from the queue, once the value is captured, the head index is set back to empty
                    self.head = 0  # set back to zero when everything has been pushed through
                    self.size -= 1  # reflects an element has been pushed through and out of the queue so the size shrinks by one
                else:
                    item_str = self.items[self.head]   # captures the value in the head index
                    self.items[self.head] = ""  # to "remove" it from the queue, once the value is captured, the head index is set back to empty
                    self.head += 1   # makes the head point to the next element coming up in the line ( so the next index over)
                    self.size -= 1   # reflects an element has been pushed through and out of the queue so the size shrinks by one
            else:  # in the case the queue is not empty
                if self.head + 1 == self.max_size:   # when everything has almost gone through and out the queue
                    item_str = self.items[self.head]   # captures the value in the head index
                    self.items[self.head] = ""   # to "remove" it from the queue, once the value is captured, the head index is set back to empty
                    self.head = 0  # making sure this is at 0
                    self.tail = 0   # shows the tail and head are the same and that the queue is empty
                    self.size -= 1   # reflects an element has been pushed through and out of the queue so the size shrinks by one
                else: # this would be the most normal outcome. for if the queue was not empty, full, or close to empty
                    item_str = self.items[self.head]
                    self.items[self.head] = ""  # captures the value in the head index 
                    self.head += 1   # makes the head point to the next element coming up in the line ( so the next index over)
                    self.size -= 1   # reflects an element has been pushed through and out of the queue so the size shrinks by one
        else:
            # Raise exception.
            raise QueueEmptyException()

        # Return statement.
        return item_str

    def peek(self):
        """
        The selection logic is necessary to determine if the stack is empty,
        since attempting to read an object from an empty stack will raise an
        exception.
        :return: Returns a str.
        """
        # Local variable declaration and initialization.
        item_str = ""     # string var to capture the value in the head index
        if not self.is_empty():
            item_str = self.items[self.head]  # captures the value in the head index if there is something there
        else:
            # Raises exception.
            raise QueueEmptyException()

        # Return statement.
        return item_str

    def get_size(self):
        """
        This function returns the size of a queue.
        :return: Returns an int.
        """
        # Return statement.
        return self.size   # returns the current size of the queue

    def print_queue(self):
        """
        This function first checks to see if the queue is empty using the
        is_empty function.  If the queue is not empty, then the entire contents
        of the queue is compiled to a string from head to tail; otherwise,
        it raises an exception.
        :return: Returns a str.
        """
        # Variable declaration and initialization.
        queue_str = ""
        if not self.is_empty():
            if self.is_full():
                if self.head == 0:
                    for objects in self.items:
                        queue_str += objects + "\n"
                elif self.head + 1 == self.max_size:
                    queue_str += self.items[self.head] + "\n"
                    for objects in range(0, self.tail + 1):
                        queue_str += self.items[objects] + "\n"
                else:
                    for objects in range(self.head, self.max_size):
                        queue_str += self.items[objects] + "\n"
                    for objects in range(0, self.tail + 1):
                        queue_str += self.items[objects] + "\n"
            else:
                if self.size == 1:
                    queue_str += self.items[self.head] + "\n"
                elif self.head == 0:
                    for objects in range(0, self.tail + 1):
                        queue_str += self.items[objects] + "\n"
                elif self.head + 1 == self.max_size:
                    queue_str += self.items[self.head] + "\n"
                    for objects in range(0, self.tail + 1):
                        queue_str += self.items[objects] + "\n"
                else:
                    for objects in range(self.head, self.max_size):
                        queue_str += self.items[objects] + "\n"
                    for objects in range(0, self.tail + 1):
                        queue_str += self.items[objects] + "\n"
        else:
            queue_str = "Queue is Empty"

        # Return statement.
        return queue_str
